import json
import random
import uuid
import logging
from collections import OrderedDict

import docker
from flask import current_app

from CTFd.utils import get_config

from .cache import CacheProvider
from .exceptions import WhaleError

# Настройка логгера
logger = logging.getLogger("whale")
logger.setLevel(logging.DEBUG)

# Создаем обработчик для вывода логов в файл
file_handler = logging.FileHandler('/var/log/CTFd/whale.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_docker_client():
    try:
        if get_config("whale:docker_use_ssl", False):
            tls_config = docker.tls.TLSConfig(
                verify=True,
                ca_cert=get_config("whale:docker_ssl_ca_cert") or None,
                client_cert=(
                    get_config("whale:docker_ssl_client_cert"),
                    get_config("whale:docker_ssl_client_key")
                ),
            )
            client = docker.DockerClient(
                base_url=get_config("whale:docker_api_url"),
                tls=tls_config,
            )
        else:
            client = docker.DockerClient(base_url=get_config("whale:docker_api_url"))

        logger.debug("Docker client initialized successfully.")
        return client
    except Exception as e:
        logger.error(f"Docker Connection Error: {e}")
        raise WhaleError(
            'Docker Connection Error\n'
            'Please ensure the docker api url (first config item) is correct\n'
            'if you are using unix:///var/run/docker.sock, check if the socket is correctly mapped'
        )


class DockerUtils:
    @staticmethod
    def init():
        try:
            DockerUtils.client = get_docker_client()
            logger.debug("DockerUtils initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize DockerUtils: {e}")
            raise

        credentials = get_config("whale:docker_credentials")
        if credentials and credentials.count(':') == 1:
            try:
                DockerUtils.client.login(*credentials.split(':'))
                logger.debug("Logged in to Docker Hub successfully.")
            except Exception as e:
                logger.error(f"Failed to login to Docker Hub: {e}")
                raise WhaleError('docker.io failed to login, check your credentials')

    @staticmethod
    def add_container(container):
        logger.debug(f"Adding container for user {container.user_id} with UUID {container.uuid}")
        if container.challenge.docker_image.startswith("{"):
            DockerUtils._create_grouped_container(DockerUtils.client, container)
        else:
            DockerUtils._create_standalone_container(DockerUtils.client, container)

    @staticmethod
    def _create_standalone_container(client, container):
        logger.debug(f"Creating standalone container for user {container.user_id} with UUID {container.uuid}")
        dns = get_config("whale:docker_dns", "").split(",")
        node = DockerUtils.choose_node(
            container.challenge.docker_image,
            get_config("whale:docker_swarm_nodes", "").split(",")
        )
        logger.debug(f"Using node: {node}")

        try:
            client.services.create(
                image=container.challenge.docker_image,
                name=f'{container.user_id}-{container.uuid}',
                env={'FLAG': container.flag}, dns_config=docker.types.DNSConfig(nameservers=dns),
                networks=[get_config("whale:docker_auto_connect_network", "ctfd_frp-containers")],
                resources=docker.types.Resources(
                    mem_limit=DockerUtils.convert_readable_text(
                        container.challenge.memory_limit),
                    cpu_limit=int(container.challenge.cpu_limit * 1e9)
                ),
                labels={
                    'whale_id': f'{container.user_id}-{container.uuid}'
                },  # for container deletion
                constraints=['node.labels.name==' + node],
                endpoint_spec=docker.types.EndpointSpec(mode='dnsrr', ports={})
            )
            logger.debug(
                f"Standalone container created successfully for user {container.user_id} with UUID {container.uuid}")
        except Exception as e:
            logger.error(f"Failed to create standalone container: {e}")
            raise

    @staticmethod
    def _create_grouped_container(client, container):
        logger.debug(f"Creating grouped container for user {container.user_id} with UUID {container.uuid}")
        range_prefix = CacheProvider(app=current_app).get_available_network_range()
        logger.debug(f"Using network range: {range_prefix}")

        try:
            ipam_pool = docker.types.IPAMPool(subnet=range_prefix)
            ipam_config = docker.types.IPAMConfig(
                driver='default', pool_configs=[ipam_pool])
            network_name = f'{container.user_id}-{container.uuid}'
            network = client.networks.create(
                network_name, internal=True,
                ipam=ipam_config, attachable=True,
                labels={'prefix': range_prefix},
                driver="overlay", scope="swarm"
            )
            logger.debug(f"Network {network_name} created successfully.")
        except Exception as e:
            logger.error(f"Failed to create network: {e}")
            raise

        dns = []
        containers = get_config("whale:docker_auto_connect_containers", "").split(",")
        for c in containers:
            if not c:
                continue
            network.connect(c)
            if "dns" in c:
                network.reload()
                for name in network.attrs['Containers']:
                    if network.attrs['Containers'][name]['Name'] == c:
                        dns.append(network.attrs['Containers'][name]['IPv4Address'].split('/')[0])
        logger.debug(f"Connected containers to network: {dns}")

        has_processed_main = False
        try:
            images = json.loads(
                container.challenge.docker_image,
                object_pairs_hook=OrderedDict
            )
            logger.debug(f"Parsed images: {images}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse challenge image: {e}")
            raise WhaleError(
                "Challenge Image Parse Error\n"
                "plase check the challenge image string"
            )

        for name, image in images.items():
            if has_processed_main:
                container_name = f'{container.user_id}-{uuid.uuid4()}'
            else:
                container_name = f'{container.user_id}-{container.uuid}'
                node = DockerUtils.choose_node(image, get_config("whale:docker_swarm_nodes", "").split(","))
                has_processed_main = True
            logger.debug(f"Creating container {container_name} with image {image} on node {node}")

            try:
                client.services.create(
                    image=image, name=container_name, networks=[
                        docker.types.NetworkAttachmentConfig(network_name, aliases=[name])
                    ],
                    env={'FLAG': container.flag},
                    dns_config=docker.types.DNSConfig(nameservers=dns),
                    resources=docker.types.Resources(
                        mem_limit=DockerUtils.convert_readable_text(
                            container.challenge.memory_limit
                        ),
                        cpu_limit=int(container.challenge.cpu_limit * 1e9)),
                    labels={
                        'whale_id': f'{container.user_id}-{container.uuid}'
                    },  # for container deletion
                    hostname=name, constraints=['node.labels.name==' + node],
                    endpoint_spec=docker.types.EndpointSpec(mode='dnsrr', ports={}))
                logger.debug(f"Container {container_name} created successfully.")
            except Exception as e:
                logger.error(f"Failed to create container {container_name}: {e}")
                raise

    @staticmethod
    def remove_container(container):
        whale_id = f'{container.user_id}-{container.uuid}'
        logger.debug(f"Removing container with whale_id: {whale_id}")

        try:
            for s in DockerUtils.client.services.list(filters={'label': f'whale_id={whale_id}'}):
                s.remove()
                logger.debug(f"Removed service: {s.name}")
        except Exception as e:
            logger.error(f"Failed to remove service: {e}")

        networks = DockerUtils.client.networks.list(names=[whale_id])
        if len(networks) > 0:  # is grouped containers
            auto_containers = get_config("whale:docker_auto_connect_containers", "").split(",")
            redis_util = CacheProvider(app=current_app)
            for network in networks:
                for container in auto_containers:
                    try:
                        network.disconnect(container, force=True)
                        logger.debug(f"Disconnected container {container} from network {network.name}")
                    except Exception as e:
                        logger.error(f"Failed to disconnect container {container}: {e}")
                redis_util.add_available_network_range(network.attrs['Labels']['prefix'])
                network.remove()
                logger.debug(f"Removed network: {network.name}")

    @staticmethod
    def convert_readable_text(text):
        lower_text = text.lower()

        if lower_text.endswith("k"):
            return int(text[:-1]) * 1024

        if lower_text.endswith("m"):
            return int(text[:-1]) * 1024 * 1024

        if lower_text.endswith("g"):
            return int(text[:-1]) * 1024 * 1024 * 1024

        return 0

    @staticmethod
    def choose_node(image, nodes):
        win_nodes = []
        linux_nodes = []
        for node in nodes:
            if node.startswith("windows"):
                win_nodes.append(node)
            else:
                linux_nodes.append(node)
        try:
            tag = image.split(":")[1:]
            if len(tag) and tag[0].startswith("windows"):
                return random.choice(win_nodes)
            return random.choice(linux_nodes)
        except IndexError:
            logger.error("No Suitable Nodes.")
            raise WhaleError(
                'No Suitable Nodes.\n'
                'If you are using Whale for the first time, \n'
                'Please Setup Swarm Nodes Correctly and Lable Them with\n'
                'docker node update --label-add "name=linux-1" $(docker node ls -q)'
            )