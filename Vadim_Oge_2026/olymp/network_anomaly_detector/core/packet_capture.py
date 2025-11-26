import asyncio
import socket
from collections import deque
from scapy.all import sniff, IP, TCP, UDP, Ether
from scapy.layers.inet6 import IPv6
import numpy as np

class PacketCapture:
    def __init__(self, config):
        self.config = config
        self.interface = config['capture']['interface']
        self.buffer_size = config['capture']['buffer_size']
        self.packet_queue = asyncio.Queue(maxsize=1000)
        self.is_capturing = False
        self.stats = {
            'total_packets': 0,
            'protocols': {},
            'source_ips': {},
            'dest_ips': {}
        }
    
    async def start_capture(self):
        """Асинхронный захват пакетов"""
        self.is_capturing = True
        loop = asyncio.get_event_loop()
        
        def packet_handler(packet):
            if self.is_capturing:
                asyncio.create_thread(self._process_packet(packet))
        
        # Захват пакетов в отдельном потоке
        await loop.run_in_executor(
            None, 
            lambda: sniff(
                iface=self.interface,
                prn=packet_handler,
                store=False
            )
        )
    
    async def _process_packet(self, packet):
        """Обработка отдельного пакета"""
        try:
            packet_data = self._extract_features(packet)
            if packet_data:
                await self.packet_queue.put(packet_data)
                self._update_stats(packet_data)
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def _extract_features(self, packet):
        """Извлечение признаков из пакета"""
        features = {
            'timestamp': packet.time,
            'size': len(packet),
            'protocol': 'unknown',
            'src_ip': '',
            'dst_ip': '',
            'src_port': 0,
            'dst_port': 0,
            'flags': 0,
            'ttl': 0
        }
        
        # Ethernet layer
        if Ether in packet:
            features['src_mac'] = packet[Ether].src
            features['dst_mac'] = packet[Ether].dst
        
        # IP layer
        if IP in packet:
            features['src_ip'] = packet[IP].src
            features['dst_ip'] = packet[IP].dst
            features['ttl'] = packet[IP].ttl
            features['protocol'] = 'IP'
        elif IPv6 in packet:
            features['src_ip'] = packet[IPv6].src
            features['dst_ip'] = packet[IPv6].dst
            features['protocol'] = 'IPv6'
        
        # Transport layer
        if TCP in packet:
            features['protocol'] = 'TCP'
            features['src_port'] = packet[TCP].sport
            features['dst_port'] = packet[TCP].dport
            features['flags'] = packet[TCP].flags
        elif UDP in packet:
            features['protocol'] = 'UDP'
            features['src_port'] = packet[UDP].sport
            features['dst_port'] = packet[UDP].dport
        
        return features
    
    def _update_stats(self, packet_data):
        """Обновление статистики"""
        self.stats['total_packets'] += 1
        
        # Статистика по протоколам
        protocol = packet_data['protocol']
        self.stats['protocols'][protocol] = self.stats['protocols'].get(protocol, 0) + 1
        
        # Статистика по IP-адресам
        src_ip = packet_data['src_ip']
        if src_ip:
            self.stats['source_ips'][src_ip] = self.stats['source_ips'].get(src_ip, 0) + 1
    
    async def get_packets(self):
        """Генератор для получения пакетов"""
        batch = []
        while self.is_capturing:
            try:
                packet = await asyncio.wait_for(
                    self.packet_queue.get(), 
                    timeout=1.0
                )
                batch.append(packet)
                
                if len(batch) >= self.buffer_size:
                    yield batch
                    batch = []
                    
            except asyncio.TimeoutError:
                if batch:
                    yield batch
                    batch = []
    
    def stop(self):
        self.is_capturing = False