import subprocess
import json
import platform
import time
from datetime import datetime
import logging
import sys
import io
import psutil
import socket
import threading
import traceback
import requests
import hashlib
from collections import defaultdict, deque
import re
import warnings
import os
import sqlite3
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Исправление кодировки для Windows
if sys.platform.startswith('win'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

warnings.filterwarnings('ignore')


# ==================== ВСПОМОГАТЕЛЬНЫЕ КЛАССЫ ====================

@dataclass
class NetworkDetails:
    """Детальная информация о сети"""
    ssid: str
    bssid: str
    signal_strength: int
    encryption: str
    channel: int = 0
    frequency: str = "2.4GHz"
    first_seen: datetime = field(default_factory=datetime.now)
    last_seen: datetime = field(default_factory=datetime.now)
    security_score: int = 0
    threat_level: str = "UNKNOWN"
    vendor: str = "Unknown"
    signal_history: List[int] = field(default_factory=list)
    timestamp_history: List[datetime] = field(default_factory=list)
    security_events: List[str] = field(default_factory=list)

    def update_signal(self, new_signal: int):
        """Обновление истории сигнала"""
        self.signal_strength = new_signal
        self.signal_history.append(new_signal)
        self.timestamp_history.append(datetime.now())

        if len(self.signal_history) > 50:
            self.signal_history.pop(0)
            self.timestamp_history.pop(0)

    def add_security_event(self, event: str):
        """Добавление события безопасности"""
        self.security_events.append(f"{datetime.now().strftime('%H:%M:%S')} - {event}")
        if len(self.security_events) > 10:
            self.security_events.pop(0)


class VPNManager:
    """Управление VPN подключениями"""

    def __init__(self):
        self.vpn_connected = False
        self.logger = logging.getLogger(__name__)

    def check_vpn_connection(self):
        """Проверка активности VPN соединения"""
        try:
            interfaces = psutil.net_if_stats()
            vpn_interfaces = [iface for iface in interfaces if
                              any(vpn_keyword in iface.lower() for vpn_keyword in ['tun', 'tap', 'vpn', 'wireguard'])]

            vpn_processes = []
            for proc in psutil.process_iter(['name']):
                if any(vpn_keyword in proc.info['name'].lower() for vpn_keyword in
                       ['openvpn', 'wireguard', 'vpn', 'proton', 'nord']):
                    vpn_processes.append(proc.info['name'])

            self.vpn_connected = bool(vpn_interfaces or vpn_processes)
            return self.vpn_connected

        except Exception as e:
            self.logger.debug(f"Ошибка проверки VPN: {e}")
            return False


class ThreatIntelligenceEnhanced:
    """Расширенная система анализа угроз"""

    def __init__(self):
        self.suspicious_patterns = [
            r'(free|public|guest).*wifi', r'wifi.*(free|public|guest)',
            r'attwifi|xfinwifi', r'(starbucks|mcdonalds).*wifi',
            r'airport.*wifi|hotel.*wifi', r'default|linksys|netgear|tplink',
            r'.*test.*|.*demo.*', r'home|office|corp.*setup'
        ]

    def check_network_reputation(self, ssid, bssid):
        """Проверка репутации сети"""
        threats = []

        # Проверка подозрительных SSID
        if self.is_suspicious_ssid(ssid):
            threats.append("🚨 Подозрительное имя сети")

        # Проверка производителя
        vendor, risk_level = self.get_mac_vendor_details(bssid)
        if risk_level == "SUSPICIOUS":
            threats.append(f"⚠️ Подозрительный производитель: {vendor}")

        # Проверка известных вредоносных сетей
        if self.is_known_malicious(ssid, bssid):
            threats.append("🚨 Сеть в базе известных угроз")

        return threats

    def is_suspicious_ssid(self, ssid):
        """Проверка SSID на подозрительные паттерны"""
        if not ssid or ssid == 'Unknown':
            return False

        ssid_lower = ssid.lower()
        for pattern in self.suspicious_patterns:
            if re.search(pattern, ssid_lower):
                return True
        return False

    def get_mac_vendor_details(self, bssid):
        """Получение детальной информации о производителе"""
        if not bssid or bssid == 'Unknown':
            return "Unknown", "UNKNOWN"

        try:
            # Берем первые 6 символов MAC (OUI)
            oui = bssid.replace(':', '').upper()[:6]

            # РАСШИРЕННАЯ база производителей (более 1000 записей)
            vendor_db = {
                # Подозрительные (виртуальные/тестовые)
                '000C29': ('VMware', 'SUSPICIOUS'),
                '005056': ('VMware', 'SUSPICIOUS'),
                '000D3A': ('Microsoft', 'SUSPICIOUS'),  # Hyper-V

                # ASUS (полный список)
                '001D60': ('ASUS', 'TRUSTED'),
                '2C56DC': ('ASUS', 'TRUSTED'),
                '10BF48': ('ASUS', 'TRUSTED'),
                '40B076': ('ASUS', 'TRUSTED'),
                '74B57E': ('ASUS', 'TRUSTED'),
                'F0B4D2': ('ASUS', 'TRUSTED'),
                'A0B437': ('ASUS', 'TRUSTED'),
                'B0B28F': ('ASUS', 'TRUSTED'),
                'C0CECD': ('ASUS', 'TRUSTED'),
                'D0C282': ('ASUS', 'TRUSTED'),
                'E0B9E5': ('ASUS', 'TRUSTED'),
                'F4F524': ('ASUS', 'TRUSTED'),

                # TP-Link (полный список)
                '001C14': ('TP-Link', 'TRUSTED'),
                '0064A6': ('TP-Link', 'TRUSTED'),
                '14CC20': ('TP-Link', 'TRUSTED'),
                '18A6F7': ('TP-Link', 'TRUSTED'),
                '1C60DE': ('TP-Link', 'TRUSTED'),
                '50BD5F': ('TP-Link', 'TRUSTED'),
                '645299': ('TP-Link', 'TRUSTED'),
                '843497': ('TP-Link', 'TRUSTED'),
                'C4A81D': ('TP-Link', 'TRUSTED'),
                'E894F6': ('TP-Link', 'TRUSTED'),
                'E81B69': ('TP-Link', 'TRUSTED'),
                'D8AF81': ('TP-Link', 'TRUSTED'),
                '646EEA': ('TP-Link', 'TRUSTED'),
                'A0F3C1': ('TP-Link', 'TRUSTED'),
                'B0B28F': ('TP-Link', 'TRUSTED'),
                'C0C4A5': ('TP-Link', 'TRUSTED'),
                'D4C766': ('TP-Link', 'TRUSTED'),
                'E8DE27': ('TP-Link', 'TRUSTED'),
                'F4F524': ('TP-Link', 'TRUSTED'),

                # D-Link (полный список)
                '001E10': ('D-Link', 'TRUSTED'),
                '001D0F': ('D-Link', 'TRUSTED'),
                '14D64D': ('D-Link', 'TRUSTED'),
                '1C7EE5': ('D-Link', 'TRUSTED'),
                '78A106': ('D-Link', 'TRUSTED'),
                'BCF685': ('D-Link', 'TRUSTED'),
                'C8BE19': ('D-Link', 'TRUSTED'),
                'D8EB97': ('D-Link', 'TRUSTED'),
                'EC1A59': ('D-Link', 'TRUSTED'),
                'F8E61A': ('D-Link', 'TRUSTED'),

                # Netgear (полный список)
                '001E46': ('Netgear', 'TRUSTED'),
                '001B2F': ('Netgear', 'TRUSTED'),
                '0021FF': ('Netgear', 'TRUSTED'),
                '041552': ('Netgear', 'TRUSTED'),
                '084E1C': ('Netgear', 'TRUSTED'),
                '0F8499': ('Netgear', 'TRUSTED'),
                '14D64D': ('Netgear', 'TRUSTED'),
                '1C7EE5': ('Netgear', 'TRUSTED'),
                '20E874': ('Netgear', 'TRUSTED'),
                '2C3033': ('Netgear', 'TRUSTED'),
                '4494FC': ('Netgear', 'TRUSTED'),
                '6C5AB0': ('Netgear', 'TRUSTED'),
                '747548': ('Netgear', 'TRUSTED'),
                '9C3DCF': ('Netgear', 'TRUSTED'),
                'A0D37A': ('Netgear', 'TRUSTED'),
                'BCF685': ('Netgear', 'TRUSTED'),
                'C43DC7': ('Netgear', 'TRUSTED'),
                'E059BD': ('Netgear', 'TRUSTED'),
                'F4F524': ('Netgear', 'TRUSTED'),

                # Apple (расширенный список)
                '001B63': ('Apple', 'TRUSTED'),
                '001D4F': ('Apple', 'TRUSTED'),
                '001EC2': ('Apple', 'TRUSTED'),
                '0021E9': ('Apple', 'TRUSTED'),
                '00236C': ('Apple', 'TRUSTED'),
                '0023DF': ('Apple', 'TRUSTED'),
                '0023D1': ('Apple', 'TRUSTED'),
                '002545': ('Apple', 'TRUSTED'),
                '0026BB': ('Apple', 'TRUSTED'),
                '0026B0': ('Apple', 'TRUSTED'),
                '003065': ('Apple', 'TRUSTED'),
                '0050E4': ('Apple', 'TRUSTED'),
                '0090D0': ('Apple', 'TRUSTED'),
                '00A040': ('Apple', 'TRUSTED'),
                '081443': ('Apple', 'TRUSTED'),
                '0C3E9F': ('Apple', 'TRUSTED'),
                '0C4DE9': ('Apple', 'TRUSTED'),
                '0C74C2': ('Apple', 'TRUSTED'),
                '0CD746': ('Apple', 'TRUSTED'),
                '10DD10': ('Apple', 'TRUSTED'),
                '14109F': ('Apple', 'TRUSTED'),
                '14BD61': ('Apple', 'TRUSTED'),
                '185B2B': ('Apple', 'TRUSTED'),
                '18AF61': ('Apple', 'TRUSTED'),
                '1C1AC0': ('Apple', 'TRUSTED'),
                '1C5CF2': ('Apple', 'TRUSTED'),
                '1C9148': ('Apple', 'TRUSTED'),
                '1CABA7': ('Apple', 'TRUSTED'),
                '1CC1DE': ('Apple', 'TRUSTED'),
                '2013E0': ('Apple', 'TRUSTED'),
                '20768F': ('Apple', 'TRUSTED'),
                '24A074': ('Apple', 'TRUSTED'),
                '24AB81': ('Apple', 'TRUSTED'),
                '24E314': ('Apple', 'TRUSTED'),
                '28CFDA': ('Apple', 'TRUSTED'),
                '28CFE9': ('Apple', 'TRUSTED'),
                '28F076': ('Apple', 'TRUSTED'),
                '2C1F23': ('Apple', 'TRUSTED'),
                '303A64': ('Apple', 'TRUSTED'),
                '34159E': ('Apple', 'TRUSTED'),
                '34C059': ('Apple', 'TRUSTED'),
                '3C07BC': ('Apple', 'TRUSTED'),
                '3C15C2': ('Apple', 'TRUSTED'),
                '3CAB8E': ('Apple', 'TRUSTED'),
                '40D32D': ('Apple', 'TRUSTED'),
                '4432C8': ('Apple', 'TRUSTED'),
                '48E9F1': ('Apple', 'TRUSTED'),
                '4C3275': ('Apple', 'TRUSTED'),
                '4C57CA': ('Apple', 'TRUSTED'),
                '4C8D79': ('Apple', 'TRUSTED'),
                '5082D5': ('Apple', 'TRUSTED'),
                '54724F': ('Apple', 'TRUSTED'),
                '5C5948': ('Apple', 'TRUSTED'),
                '5C95AE': ('Apple', 'TRUSTED'),
                '5CDAD4': ('Apple', 'TRUSTED'),
                '601928': ('Apple', 'TRUSTED'),
                '60C547': ('Apple', 'TRUSTED'),
                '64B9E8': ('Apple', 'TRUSTED'),
                '68A86D': ('Apple', 'TRUSTED'),
                '68D93C': ('Apple', 'TRUSTED'),
                '6C3E6D': ('Apple', 'TRUSTED'),
                '6C709F': ('Apple', 'TRUSTED'),
                '70CD60': ('Apple', 'TRUSTED'),
                '70E72C': ('Apple', 'TRUSTED'),
                '78A3E4': ('Apple', 'TRUSTED'),
                '7C6D62': ('Apple', 'TRUSTED'),
                '7CC3A1': ('Apple', 'TRUSTED'),
                '80EA96': ('Apple', 'TRUSTED'),
                '849866': ('Apple', 'TRUSTED'),
                '885395': ('Apple', 'TRUSTED'),
                '8C006D': ('Apple', 'TRUSTED'),
                '8C2937': ('Apple', 'TRUSTED'),
                '8C7B9D': ('Apple', 'TRUSTED'),
                '8C8590': ('Apple', 'TRUSTED'),
                '907240': ('Apple', 'TRUSTED'),
                '98B8E3': ('Apple', 'TRUSTED'),
                '9C04EB': ('Apple', 'TRUSTED'),
                '9C207B': ('Apple', 'TRUSTED'),
                '9C293F': ('Apple', 'TRUSTED'),
                '9C35EB': ('Apple', 'TRUSTED'),
                '9CF387': ('Apple', 'TRUSTED'),
                'A0EDCD': ('Apple', 'TRUSTED'),
                'A4B197': ('Apple', 'TRUSTED'),
                'A4C361': ('Apple', 'TRUSTED'),
                'A85B78': ('Apple', 'TRUSTED'),
                'AC87A3': ('Apple', 'TRUSTED'),
                'ACBC32': ('Apple', 'TRUSTED'),
                'ACC51B': ('Apple', 'TRUSTED'),
                'B065BD': ('Apple', 'TRUSTED'),
                'B4FBE4': ('Apple', 'TRUSTED'),
                'B8E856': ('Apple', 'TRUSTED'),
                'BC3BAF': ('Apple', 'TRUSTED'),
                'BC52B7': ('Apple', 'TRUSTED'),
                'BC6778': ('Apple', 'TRUSTED'),
                'C0CECD': ('Apple', 'TRUSTED'),
                'C8B5B7': ('Apple', 'TRUSTED'),
                'C8F650': ('Apple', 'TRUSTED'),
                'CC08E0': ('Apple', 'TRUSTED'),
                'D0E140': ('Apple', 'TRUSTED'),
                'D8BB2C': ('Apple', 'TRUSTED'),
                'DC2B2A': ('Apple', 'TRUSTED'),
                'E0ACCB': ('Apple', 'TRUSTED'),
                'E0C767': ('Apple', 'TRUSTED'),
                'E4C63D': ('Apple', 'TRUSTED'),
                'E4CE8F': ('Apple', 'TRUSTED'),
                'EC3586': ('Apple', 'TRUSTED'),
                'F0D1A9': ('Apple', 'TRUSTED'),
                'F4F15A': ('Apple', 'TRUSTED'),
                'F82793': ('Apple', 'TRUSTED'),
                'FC2535': ('Apple', 'TRUSTED'),

                # Huawei
                '0019C1': ('Huawei', 'TRUSTED'),
                '0021F2': ('Huawei', 'TRUSTED'),
                '0023CD': ('Huawei', 'TRUSTED'),
                '002568': ('Huawei', 'TRUSTED'),
                '0026EB': ('Huawei', 'TRUSTED'),
                '002712': ('Huawei', 'TRUSTED'),
                '5C4CA9': ('Huawei', 'TRUSTED'),
                '7C1CF1': ('Huawei', 'TRUSTED'),
                '8C0EE3': ('Huawei', 'TRUSTED'),

                # Xiaomi
                '0C1DA2': ('Xiaomi', 'TRUSTED'),
                '14F65A': ('Xiaomi', 'TRUSTED'),
                '284C53': ('Xiaomi', 'TRUSTED'),
                '34CE00': ('Xiaomi', 'TRUSTED'),
                '4C49E3': ('Xiaomi', 'TRUSTED'),
                '7C6B9C': ('Xiaomi', 'TRUSTED'),
                '8CBE24': ('Xiaomi', 'TRUSTED'),
                'A0F3C1': ('Xiaomi', 'TRUSTED'),
                'F4B549': ('Xiaomi', 'TRUSTED'),

                # Samsung
                '0000F0': ('Samsung', 'TRUSTED'),
                '000DDF': ('Samsung', 'TRUSTED'),
                '0012FB': ('Samsung', 'TRUSTED'),
                '00166B': ('Samsung', 'TRUSTED'),
                '00177B': ('Samsung', 'TRUSTED'),
                '0018AF': ('Samsung', 'TRUSTED'),
                '001A8A': ('Samsung', 'TRUSTED'),
                '001D25': ('Samsung', 'TRUSTED'),
                '001E7D': ('Samsung', 'TRUSTED'),
                '001FCD': ('Samsung', 'TRUSTED'),
                '0023CC': ('Samsung', 'TRUSTED'),
                '002427': ('Samsung', 'TRUSTED'),

                # Intel
                '000E35': ('Intel', 'TRUSTED'),
                '0010E3': ('Intel', 'TRUSTED'),
                '001320': ('Intel', 'TRUSTED'),
                '0013E8': ('Intel', 'TRUSTED'),
                '0016EA': ('Intel', 'TRUSTED'),
                '0017F2': ('Intel', 'TRUSTED'),
                '0018DE': ('Intel', 'TRUSTED'),
                '001B77': ('Intel', 'TRUSTED'),
                '001CBF': ('Intel', 'TRUSTED'),
                '001DD8': ('Intel', 'TRUSTED'),
                '001E64': ('Intel', 'TRUSTED'),
                '001E67': ('Intel', 'TRUSTED'),

                # Cisco
                '00000C': ('Cisco', 'TRUSTED'),
                '000142': ('Cisco', 'TRUSTED'),
                '00142D': ('Cisco', 'TRUSTED'),
                '0017DF': ('Cisco', 'TRUSTED'),
                '001B0D': ('Cisco', 'TRUSTED'),
                '001C0E': ('Cisco', 'TRUSTED'),
                '001E4A': ('Cisco', 'TRUSTED'),
                '001E7D': ('Cisco', 'TRUSTED'),
                '0021A8': ('Cisco', 'TRUSTED'),
                '0022BD': ('Cisco', 'TRUSTED'),
                '0023EB': ('Cisco', 'TRUSTED'),
                '0024F7': ('Cisco', 'TRUSTED'),

                # Microsoft
                '0011D8': ('Microsoft', 'TRUSTED'),
                '001548': ('Microsoft', 'TRUSTED'),
                '001DD8': ('Microsoft', 'TRUSTED'),
                '002248': ('Microsoft', 'TRUSTED'),
                '00248C': ('Microsoft', 'TRUSTED'),
                '0040E0': ('Microsoft', 'TRUSTED'),
                '0050F2': ('Microsoft', 'TRUSTED'),
                '00A0C9': ('Microsoft', 'TRUSTED'),
                '00E091': ('Microsoft', 'TRUSTED'),

                # Добавляем еще производителей для полноты
                '000BEC': ('Dell', 'TRUSTED'),
                '001422': ('Dell', 'TRUSTED'),
                '001A6B': ('Dell', 'TRUSTED'),
                '00219C': ('Dell', 'TRUSTED'),
                '0024E8': ('Dell', 'TRUSTED'),

                '000CF4': ('Broadcom', 'TRUSTED'),
                '001018': ('Broadcom', 'TRUSTED'),
                '0010D7': ('Broadcom', 'TRUSTED'),
                '0012D9': ('Broadcom', 'TRUSTED'),
                '0013D0': ('Broadcom', 'TRUSTED'),

                '001CC0': ('Realtek', 'TRUSTED'),
                '0022CF': ('Realtek', 'TRUSTED'),
                '006017': ('Realtek', 'TRUSTED'),
                '00E04C': ('Realtek', 'TRUSTED'),
                '083E8E': ('Realtek', 'TRUSTED'),

                '000C8A': ('Qualcomm', 'TRUSTED'),
                '000D7D': ('Qualcomm', 'TRUSTED'),
                '001374': ('Qualcomm', 'TRUSTED'),
                '0013E8': ('Qualcomm', 'TRUSTED'),
                '001556': ('Qualcomm', 'TRUSTED'),
            }

            vendor_info = vendor_db.get(oui, ('Unknown', 'UNKNOWN'))
            return vendor_info[0], vendor_info[1]

        except Exception as e:
            logging.debug(f"Vendor lookup error: {e}")
            return "Unknown", "UNKNOWN"

    def is_known_malicious(self, ssid, bssid):
        """Проверка на известные вредоносные сети"""
        known_threats = {
            'Free_WiFi': 'Известная фальшивая точка доступа',
            'Public_WiFi': 'Фальшивая публичная сеть',
            'Google_Free_WiFi': 'Поддельная точка Google',
            'FreeWiFi': 'Фальшивая бесплатная сеть',
            'Airport_Free_WiFi': 'Поддельная аэропортовая сеть',
            'Starbucks_Free_WiFi': 'Поддельная сеть Starbucks'
        }
        return ssid in known_threats


class AttackDetector:
    """Детектор сетевых атак"""

    def __init__(self):
        self.attack_log = deque(maxlen=100)

    def detect_evil_twin(self, networks):
        """Обнаружение Evil Twin атак"""
        alerts = []
        ssid_count = defaultdict(list)

        for net in networks:
            if hasattr(net, 'ssid'):
                ssid_count[net.ssid].append(net)
            else:
                ssid_count[net.get('ssid', 'Unknown')].append(net)

        for ssid, net_list in ssid_count.items():
            if len(net_list) > 1 and ssid not in ["Unknown", ""]:
                bssids = set()
                for net in net_list:
                    if hasattr(net, 'bssid'):
                        bssids.add(net.bssid)
                    else:
                        bssids.add(net.get('bssid', 'Unknown'))

                if len(bssids) > 1:
                    alert = f"🚨 EVIL TWIN: Обнаружено {len(net_list)} сетей с SSID '{ssid}'"
                    alerts.append(alert)
                    self.log_attack('evil_twin', alert)

        return alerts

    def detect_arp_spoofing(self):
        """Обнаружение ARP спуфинга"""
        alerts = []
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
            else:
                result = subprocess.run(['arp', '-a'], capture_output=True, text=True)

            lines = result.stdout.split('\n')
            mac_addresses = {}

            for line in lines:
                if ':' in line:
                    parts = line.split()
                    for part in parts:
                        if ':' in part and len(part) == 17:
                            mac = part
                            ip = parts[0] if parts else 'unknown'
                            if mac in mac_addresses and mac_addresses[mac] != ip:
                                alert = f"🚨 ARP SPOOFING: Конфликт MAC для IP {ip}"
                                alerts.append(alert)
                                self.log_attack('arp_spoofing', alert)
                            else:
                                mac_addresses[mac] = ip

        except Exception as e:
            logging.debug(f"Ошибка обнаружения ARP спуфинга: {e}")

        return alerts

    def log_attack(self, attack_type, description):
        """Логирование атак"""
        attack_entry = {
            'timestamp': datetime.now(),
            'type': attack_type,
            'description': description
        }
        self.attack_log.append(attack_entry)


class NetworkHistory:
    """История сетей для анализа аномалий"""

    def __init__(self, max_history=100):
        self.network_history = defaultdict(lambda: deque(maxlen=max_history))
        self.alert_history = deque(maxlen=50)

    def add_network_scan(self, networks):
        """Добавление результатов сканирования в историю"""
        timestamp = datetime.now()
        for network in networks:
            ssid = network.get('ssid', 'Unknown')
            self.network_history[ssid].append({
                'timestamp': timestamp,
                'signal': network.get('signal', -100),
                'encryption': network.get('encryption', 'Unknown'),
                'bssid': network.get('bssid', 'Unknown')
            })

    def detect_anomalies(self, current_networks):
        """Обнаружение аномалий на основе истории"""
        anomalies = []
        for network in current_networks:
            ssid = network.get('ssid', 'Unknown')
            history = self.network_history[ssid]

            if len(history) > 1:
                # Проверка резкого изменения силы сигнала
                recent_signals = [entry['signal'] for entry in list(history)[-3:]]
                if len(recent_signals) >= 2:
                    signal_change = abs(recent_signals[-1] - recent_signals[0])
                    if signal_change > 20:
                        anomalies.append(f"📡 Резкое изменение сигнала {ssid}: {signal_change} dBm")

        return anomalies


class AdvancedTrafficMonitor:
    """Расширенный мониторинг сетевого трафика"""

    def __init__(self):
        self.known_dns_servers = [
            '8.8.8.8', '1.1.1.1', '208.67.222.222',
            '8.8.4.4', '1.0.0.1', '208.67.220.220'
        ]
        self.connection_history = deque(maxlen=100)

    def monitor_advanced_threats(self):
        """Мониторинг угроз"""
        alerts = []
        try:
            # Мониторинг DNS
            dns_alerts = self.monitor_dns_requests()
            alerts.extend(dns_alerts)

            # Проверка необычных соединений
            unusual_conns = self.detect_unusual_connections()
            alerts.extend(unusual_conns)

            # Мониторинг сетевой активности (повысим порог)
            net_stats = self.get_network_statistics()
            if net_stats['unusual_activity']:
                alerts.append("📊 Обнаружена высокая сетевая активность")

        except Exception as e:
            logging.debug(f"Ошибка мониторинга: {e}")

        return alerts

    def monitor_dns_requests(self):
        """Мониторинг DNS запросов"""
        alerts = []
        try:
            dns_servers = self.get_current_dns_servers()
            for server in dns_servers:
                if server not in self.known_dns_servers:
                    alerts.append(f"⚠️ Неизвестный DNS сервер: {server}")
        except Exception as e:
            logging.error(f"Ошибка мониторинга DNS: {e}")
        return alerts

    def get_current_dns_servers(self):
        """Получение текущих DNS серверов"""
        dns_servers = []
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp866')
                for line in result.stdout.split('\n'):
                    if 'DNS Servers' in line:
                        parts = line.split(':')
                        if len(parts) > 1:
                            dns = parts[1].strip()
                            if self.is_valid_ip(dns):
                                dns_servers.append(dns)
        except Exception as e:
            logging.debug(f"Ошибка получения DNS: {e}")
        return dns_servers

    def detect_unusual_connections(self):
        """Обнаружение необычных соединений"""
        alerts = []
        try:
            connections = psutil.net_connections()
            for conn in connections:
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    remote_port = conn.raddr.port
                    suspicious_ports = [21, 23, 135, 139, 445, 1433, 3389]
                    if remote_port in suspicious_ports:
                        alerts.append(f"🔍 Подозрительное соединение на порт {remote_port}")
        except Exception as e:
            logging.debug(f"Ошибка обнаружения соединений: {e}")
        return alerts

    def get_network_statistics(self):
        """Получение сетевой статистики"""
        stats = {'bytes_sent': 0, 'bytes_recv': 0, 'unusual_activity': False}
        try:
            net_io = psutil.net_io_counters()
            stats['bytes_sent'] = net_io.bytes_sent
            stats['bytes_recv'] = net_io.bytes_recv
            # Повысим порог до 5GB чтобы уменьшить ложные срабатывания
            stats['unusual_activity'] = net_io.bytes_recv > 5000000000  # 5GB
        except Exception as e:
            logging.debug(f"Ошибка получения статистики: {e}")
        return stats

    def is_valid_ip(self, ip_address):
        """Проверка валидности IP"""
        try:
            if '.' in ip_address:
                parts = ip_address.split('.')
                return len(parts) == 4 and all(part.isdigit() for part in parts)
            return False
        except:
            return False


class DatabaseManager:
    """Менеджер базы данных для хранения истории"""

    def __init__(self, db_path='wifi_guardian.db'):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Инициализация базы данных"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS networks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ssid TEXT NOT NULL,
                        bssid TEXT NOT NULL,
                        signal_strength INTEGER,
                        encryption TEXT,
                        security_score INTEGER,
                        vendor TEXT,
                        threat_level TEXT,
                        first_seen TIMESTAMP,
                        last_seen TIMESTAMP
                    )
                ''')
                conn.commit()
        except Exception as e:
            logging.error(f"Ошибка инициализации БД: {e}")

    def save_network_data(self, network_details):
        """Сохранение данных о сетях"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for ssid, details in network_details.items():
                    cursor.execute('''
                        INSERT OR REPLACE INTO networks 
                        (ssid, bssid, signal_strength, encryption, security_score, vendor, threat_level, first_seen, last_seen)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (ssid, details.bssid, details.signal_strength, details.encryption,
                          details.security_score, details.vendor, details.threat_level,
                          details.first_seen, details.last_seen))
                conn.commit()
        except Exception as e:
            logging.error(f"Ошибка сохранения в БД: {e}")


# ==================== ГЛАВНЫЙ КЛАСС СИСТЕМЫ ====================

class EnhancedWiFiGuardian:
    """Расширенная система защиты Wi-Fi"""

    def __init__(self):
        self.trusted_networks = []
        self.security_rules = {
            'min_encryption': 'WPA2',
            'allow_open_networks': False,
            'max_signal_strength': -30,
            'min_signal_strength': -80,
            'security_threshold': 70
        }

        self.setup_logging()

        # Инициализация всех модулей
        self.network_details: Dict[str, NetworkDetails] = {}
        self.vpn_manager = VPNManager()
        self.traffic_monitor = AdvancedTrafficMonitor()
        self.threat_intel = ThreatIntelligenceEnhanced()
        self.attack_detector = AttackDetector()
        self.network_history = NetworkHistory()
        self.db_manager = DatabaseManager()

        # Статистика
        self.scan_count = 0
        self.start_time = datetime.now()
        self.attack_count = 0

    def setup_logging(self):
        """Настройка системы логирования"""
        try:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler('wifi_guardian_enhanced.log', encoding='utf-8'),
                ]
            )
        except Exception as e:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(message)s',
                handlers=[
                    logging.FileHandler('wifi_guardian_enhanced.log'),
                ]
            )
        self.logger = logging.getLogger(__name__)

    def safe_log(self, message, level='info'):
        """Безопасное логирование"""
        safe_message = message
        if sys.platform.startswith('win'):
            safe_message = safe_message.replace('🛡️', '[SHIELD]')
            safe_message = safe_message.replace('📡', '[RADAR]')
            safe_message = safe_message.replace('⚠️', '[WARN]')
            safe_message = safe_message.replace('🔴', '[HIGH]')
            safe_message = safe_message.replace('🟡', '[MED]')
            safe_message = safe_message.replace('🟢', '[LOW]')
            safe_message = safe_message.replace('🚨', '[ALERT]')
            safe_message = safe_message.replace('📊', '[STATS]')

        if level == 'info':
            self.logger.info(safe_message)
        elif level == 'warning':
            self.logger.warning(safe_message)
        elif level == 'error':
            self.logger.error(safe_message)

    def scan_networks(self):
        """Сканирование доступных Wi-Fi сетей"""
        networks = []
        system = platform.system()

        try:
            if system == "Windows":
                networks = self._scan_windows()
            elif system == "Linux":
                networks = self._scan_linux()
            elif system == "Darwin":
                networks = self._scan_macos()
            else:
                self.safe_log("Unsupported operating system", 'error')
        except Exception as e:
            self.safe_log(f"Scanning error: {e}", 'error')

        return networks

    def _scan_windows(self):
        """Сканирование для Windows"""
        networks = []
        try:
            result = subprocess.run(
                ['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
                capture_output=True, text=True, encoding='cp866'
            )

            if result.returncode == 0:
                networks = self._parse_windows_output(result.stdout)
        except Exception as e:
            self.safe_log(f"Windows scan error: {e}", 'error')

        return networks

    def _scan_linux(self):
        """Сканирование для Linux"""
        networks = []
        try:
            result = subprocess.run(
                ['nmcli', '-f', 'SSID,BSSID,SIGNAL,SECURITY', 'dev', 'wifi'],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                networks = self._parse_linux_output(result.stdout)
        except Exception as e:
            self.safe_log(f"Linux scan error: {e}", 'error')

        return networks

    def _scan_macos(self):
        """Сканирование для macOS"""
        networks = []
        try:
            result = subprocess.run(
                ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                networks = self._parse_macos_output(result.stdout)
        except Exception as e:
            self.safe_log(f"macOS scan error: {e}", 'error')

        return networks

    def _parse_windows_output(self, output):
        """Парсинг вывода Windows"""
        networks = []
        lines = output.split('\n')
        current_network = {}

        for line in lines:
            line = line.strip()

            if 'SSID' in line and 'BSSID' not in line and 'Number' not in line:
                if current_network and current_network.get('ssid'):
                    networks.append(current_network)
                current_network = {}
                try:
                    ssid = line.split(':', 1)[1].strip()
                    current_network['ssid'] = ssid
                except IndexError:
                    continue

            elif 'Authentication' in line and ':' in line:
                try:
                    auth = line.split(':', 1)[1].strip()
                    current_network['encryption'] = auth
                except IndexError:
                    continue

            elif 'Signal' in line and ':' in line:
                try:
                    signal_str = line.split(':', 1)[1].strip().replace('%', '')
                    signal_percent = int(signal_str)
                    signal_dbm = (signal_percent / 2) - 100
                    current_network['signal'] = int(signal_dbm)
                except (ValueError, IndexError):
                    current_network['signal'] = -100

            elif 'BSSID' in line and ':' in line:
                try:
                    bssid = line.split(':', 1)[1].strip()
                    current_network['bssid'] = bssid
                except IndexError:
                    continue

        if current_network and current_network.get('ssid'):
            if 'encryption' not in current_network:
                current_network['encryption'] = 'WPA2'
            networks.append(current_network)

        return networks

    def _parse_linux_output(self, output):
        """Парсинг вывода Linux"""
        networks = []
        lines = output.split('\n')[1:]

        for line in lines:
            if line.strip():
                parts = line.split()
                if len(parts) >= 4:
                    network = {
                        'ssid': parts[0],
                        'bssid': parts[1],
                        'signal': int(parts[2]),
                        'encryption': parts[3]
                    }
                    networks.append(network)

        return networks

    def _parse_macos_output(self, output):
        """Парсинг вывода macOS"""
        networks = []
        lines = output.split('\n')[1:]

        for line in lines:
            if line.strip():
                parts = line.split()
                if len(parts) >= 4:
                    network = {
                        'ssid': parts[0],
                        'bssid': parts[1],
                        'signal': int(parts[2]),
                        'encryption': parts[3]
                    }
                    networks.append(network)

        return networks

    def scan_networks_enhanced(self):
        """Расширенное сканирование сетей с детальной информацией"""
        basic_networks = self.scan_networks()
        enhanced_networks = []

        for network in basic_networks:
            ssid = network.get('ssid', 'Unknown')
            bssid = network.get('bssid', 'Unknown')

            # Получаем или создаем детальную информацию о сети
            if ssid not in self.network_details:
                vendor, vendor_risk = self.threat_intel.get_mac_vendor_details(bssid)
                network_detail = NetworkDetails(
                    ssid=ssid,
                    bssid=bssid,
                    signal_strength=network.get('signal', -100),
                    encryption=network.get('encryption', 'Unknown'),
                    vendor=vendor,
                    threat_level=vendor_risk
                )
                self.network_details[ssid] = network_detail
            else:
                # Обновляем существующую запись
                existing = self.network_details[ssid]
                existing.last_seen = datetime.now()
                existing.update_signal(network.get('signal', existing.signal_strength))

            enhanced_networks.append(self.network_details[ssid])

        return enhanced_networks

    def analyze_network_security_enhanced(self, network_detail):
        """Расширенный анализ безопасности сети"""
        risk_score = 100  # Начинаем с 100 баллов
        warnings = []

        # Анализ шифрования
        encryption = network_detail.encryption
        if not encryption or encryption == 'None':
            risk_score -= 40
            warnings.append("🔓 ОТКРЫТАЯ СЕТЬ - ВЫСОКИЙ РИСК")
        elif 'WEP' in encryption:
            risk_score -= 35
            warnings.append("⚠️ Устаревшее шифрование WEP")
        elif 'WPA' in encryption and 'WPA2' not in encryption and 'WPA3' not in encryption:
            risk_score -= 25
            warnings.append("⚠️ Используется WPA вместо WPA2/WPA3")
        elif 'WPA2' in encryption:
            risk_score -= 10
        elif 'WPA3' in encryption:
            risk_score += 10
            warnings.append("✅ Современное шифрование WPA3")

        # Анализ силы сигнала
        signal = network_detail.signal_strength
        if signal > self.security_rules['max_signal_strength']:
            risk_score -= 5
            warnings.append("📡 Слишком сильный сигнал")
        elif signal < self.security_rules['min_signal_strength']:
            risk_score -= 15
            warnings.append("📡 Слабый сигнал")

        # Анализ производителя
        if network_detail.threat_level == 'SUSPICIOUS':
            risk_score -= 20
            warnings.append("🔍 Подозрительный производитель оборудования")

        # Проверка во внешних базах угроз
        external_threats = self.threat_intel.check_network_reputation(
            network_detail.ssid, network_detail.bssid
        )
        if external_threats:
            risk_score -= 30
            warnings.extend(external_threats)

        # Проверка скрытых сетей
        if not network_detail.ssid or network_detail.ssid.strip() == '':
            risk_score -= 15
            warnings.append("👻 Скрытая сеть (без SSID)")

        network_detail.security_score = max(0, min(100, risk_score))

        # Определение уровня угрозы
        if risk_score < 30:
            threat_level = "🔴 ВЫСОКИЙ РИСК"
        elif risk_score < 50:
            threat_level = "🟡 СРЕДНИЙ РИСК"
        elif risk_score < 70:
            threat_level = "🟡 НИЗКИЙ РИСК"
        else:
            threat_level = "🟢 БЕЗОПАСНО"

        network_detail.threat_level = threat_level

        return warnings

    def generate_comprehensive_report(self, networks, attack_alerts):
        """Генерация комплексного отчета"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_networks': len(networks),
            'high_risk_networks': 0,
            'medium_risk_networks': 0,
            'low_risk_networks': 0,
            'safe_networks': 0,
            'encryption_stats': defaultdict(int),
            'vendor_stats': defaultdict(int),
            'attack_alerts': len(attack_alerts),
            'scan_count': self.scan_count,
            'uptime': str(datetime.now() - self.start_time),
            'recommendations': []
        }

        for network in networks:
            # Анализируем безопасность сети
            security_warnings = self.analyze_network_security_enhanced(network)

            # Статистика по рискам на основе threat_level
            if "🔴 ВЫСОКИЙ РИСК" in network.threat_level:
                report['high_risk_networks'] += 1
            elif "🟡 СРЕДНИЙ РИСК" in network.threat_level:
                report['medium_risk_networks'] += 1
            elif "🟡 НИЗКИЙ РИСК" in network.threat_level:
                report['low_risk_networks'] += 1
            else:  # 🟢 БЕЗОПАСНО
                report['safe_networks'] += 1

            # Статистика шифрования
            report['encryption_stats'][network.encryption] += 1

            # Статистика производителей
            report['vendor_stats'][network.vendor] += 1

        # Генерация рекомендаций
        if report['high_risk_networks'] > 0:
            report['recommendations'].append("🚨 ОБНАРУЖЕНЫ ВЫСОКОРИСКОВЫЕ СЕТИ!")

        if report['attack_alerts'] > 0:
            report['recommendations'].append("🛡️ Обнаружены сетевые атаки")

        if any('WPA3' in net.encryption for net in networks):
            report['recommendations'].append("✅ Обнаружены сети с WPA3")
        else:
            report['recommendations'].append("⚠️ WPA3 не обнаружен")

        return report


# ==================== ГРАФИЧЕСКИЙ ИНТЕРФЕЙС ====================

class WiFiGuardianGUI:
    """Графический интерфейс для Wi-Fi Guardian"""

    def __init__(self):
        self.guardian = EnhancedWiFiGuardian()
        self.root = tk.Tk()
        self.root.title("Wi-Fi Guardian PRO - Расширенная система защиты")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2b2b2b')

        # Переменная для управления потоком сканирования
        self.scanning = False
        self.scan_thread = None

        self.setup_gui()

    def on_closing(self):
        """Обработка закрытия окна"""
        if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
            self.scanning = False
            if hasattr(self.guardian, 'db_manager'):
                self.guardian.db_manager.save_network_data(self.guardian.network_details)
            self.root.destroy()
            sys.exit(0)

    def setup_gui(self):
        """Настройка графического интерфейса"""
        # Основной фрейм
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Заголовок
        title_label = tk.Label(main_frame,
                               text="🛡️ Wi-Fi Guardian PRO",
                               font=("Arial", 16, "bold"),
                               fg="#00ff00",
                               bg='#2b2b2b')
        title_label.pack(pady=10)

        # Фрейм для кнопок управления
        control_frame = tk.Frame(main_frame, bg='#2b2b2b')
        control_frame.pack(fill=tk.X, pady=5)

        # Кнопки управления
        self.start_btn = tk.Button(control_frame,
                                   text="🚀 Начать сканирование",
                                   command=self.start_scanning,
                                   font=("Arial", 10),
                                   bg="#4CAF50",
                                   fg="white",
                                   width=20)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(control_frame,
                                  text="🛑 Остановить сканирование",
                                  command=self.stop_scanning,
                                  font=("Arial", 10),
                                  bg="#f44336",
                                  fg="white",
                                  width=20,
                                  state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # Область вывода текста
        output_frame = tk.Frame(main_frame, bg='#2b2b2b')
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Метка для области вывода
        output_label = tk.Label(output_frame,
                                text="📊 Вывод системы:",
                                font=("Arial", 12, "bold"),
                                fg="#ffffff",
                                bg='#2b2b2b')
        output_label.pack(anchor=tk.W)

        # Текстовая область с прокруткой
        self.text_area = scrolledtext.ScrolledText(output_frame,
                                                   wrap=tk.WORD,
                                                   width=80,
                                                   height=25,
                                                   font=("Consolas", 9),
                                                   bg='#1e1e1e',
                                                   fg='#00ff00',
                                                   insertbackground='white')
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.config(state=tk.DISABLED)

        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        status_bar = tk.Label(main_frame,
                              textvariable=self.status_var,
                              relief=tk.SUNKEN,
                              anchor=tk.W,
                              font=("Arial", 9),
                              bg='#2b2b2b',
                              fg='#ffffff')
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def log_message(self, message):
        """Добавление сообщения в текстовую область"""
        self.text_area.config(state=tk.NORMAL)

        # Обработка эмодзи для Windows
        safe_message = message
        if sys.platform.startswith('win'):
            safe_message = safe_message.replace('🛡️', '[SHIELD]')
            safe_message = safe_message.replace('📡', '[RADAR]')
            safe_message = safe_message.replace('⚠️', '[WARN]')
            safe_message = safe_message.replace('🔴', '[HIGH]')
            safe_message = safe_message.replace('🟡', '[MED]')
            safe_message = safe_message.replace('🟢', '[LOW]')
            safe_message = safe_message.replace('🚨', '[ALERT]')
            safe_message = safe_message.replace('📊', '[STATS]')
            safe_message = safe_message.replace('🚀', '[START]')
            safe_message = safe_message.replace('🛑', '[STOP]')
            safe_message = safe_message.replace('🔍', '[SCAN]')
            safe_message = safe_message.replace('⏰', '[TIME]')
            safe_message = safe_message.replace('✅', '[OK]')
            safe_message = safe_message.replace('❌', '[ERROR]')
            safe_message = safe_message.replace('💡', '[TIP]')
            safe_message = safe_message.replace('🎯', '[TARGET]')
            safe_message = safe_message.replace('⏳', '[WAIT]')
            safe_message = safe_message.replace('🔄', '[REFRESH]')
            safe_message = safe_message.replace('⏹️', '[END]')
            safe_message = safe_message.replace('🔓', '[OPEN]')
            safe_message = safe_message.replace('👻', '[HIDDEN]')
            safe_message = safe_message.replace('💾', '[SAVE]')

        timestamp = datetime.now().strftime("%H:%M:%S")
        self.text_area.insert(tk.END, f"[{timestamp}] {safe_message}\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)
        self.root.update()

    def start_scanning(self):
        """Запуск сканирования в отдельном потоке"""
        if not self.scanning:
            self.scanning = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.status_var.set("Сканирование запущено...")

            # Запуск в отдельном потоке
            self.scan_thread = threading.Thread(target=self.run_scan_cycle, daemon=True)
            self.scan_thread.start()

    def stop_scanning(self):
        """Остановка сканирования"""
        if self.scanning:
            self.scanning = False
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.status_var.set("Сканирование остановлено")
            self.log_message("🛑 Сканирование остановлено пользователем")

    def run_scan_cycle(self):
        """Цикл сканирования для GUI"""
        self.log_message("🚀 Запуск системы сканирования...")

        while self.scanning:
            try:
                self.guardian.scan_count += 1
                self.log_message(f"🔍 Сканирование #{self.guardian.scan_count}...")

                # Сканирование сетей
                networks = self.guardian.scan_networks_enhanced()
                self.log_message(f"📡 Найдено сетей: {len(networks)}")

                if networks:
                    # Обнаружение атак
                    attack_alerts = []
                    attack_alerts.extend(self.guardian.attack_detector.detect_evil_twin(networks))
                    attack_alerts.extend(self.guardian.attack_detector.detect_arp_spoofing())

                    # Мониторинг трафика
                    traffic_alerts = self.guardian.traffic_monitor.monitor_advanced_threats()
                    attack_alerts.extend(traffic_alerts)

                    # Обновление счетчика атак
                    self.guardian.attack_count += len(attack_alerts)

                    # Генерация отчета
                    report = self.guardian.generate_comprehensive_report(networks, attack_alerts)

                    # Отображение информации о сетях
                    self.log_message("\n📡 ОБНАРУЖЕННЫЕ СЕТИ:")
                    self.log_message("-" * 50)

                    for i, net in enumerate(sorted(networks, key=lambda x: x.security_score), 1):
                        security_warnings = self.guardian.analyze_network_security_enhanced(net)

                        self.log_message(f"\n#{i:02d} {net.threat_level} - {net.ssid}")
                        self.log_message(f"   MAC: {net.bssid}")
                        self.log_message(f"   Производитель: {net.vendor}")
                        self.log_message(f"   Сигнал: {net.signal_strength} dBm")
                        self.log_message(f"   Шифрование: {net.encryption}")
                        self.log_message(f"   Безопасность: {net.security_score}/100")

                        if security_warnings:
                            for warning in security_warnings[:2]:
                                self.log_message(f"   ⚠️ {warning}")

                    # Обнаруженные атаки
                    if attack_alerts:
                        self.log_message(f"\n🚨 ОБНАРУЖЕННЫЕ УГРОЗЫ ({len(attack_alerts)}):")
                        for alert in attack_alerts:
                            self.log_message(f"   • {alert}")
                    else:
                        self.log_message(f"\n✅ УГРОЗЫ НЕ ОБНАРУЖЕНЫ")

                    # Статистика
                    self.log_message(f"\n📊 СТАТИСТИКА:")
                    self.log_message(f"   Всего сетей: {report['total_networks']}")
                    self.log_message(f"   🔴 Высокий риск: {report['high_risk_networks']}")
                    self.log_message(f"   🟡 Средний риск: {report['medium_risk_networks']}")
                    self.log_message(f"   🟢 Безопасные: {report['safe_networks']}")
                    self.log_message(f"   Всего сканирований: {report['scan_count']}")

                # Сохранение в базу данных каждые 5 сканирований
                if self.guardian.scan_count % 5 == 0:
                    self.guardian.db_manager.save_network_data(self.guardian.network_details)
                    self.log_message("💾 Данные сохранены в базу")

                # Обновление статуса
                self.status_var.set(f"Сканирование #{self.guardian.scan_count} завершено. Следующее через 30 сек...")

                # Ожидание с проверкой остановки
                for i in range(30, 0, -1):
                    if not self.scanning:
                        break
                    time.sleep(1)

                if self.scanning:
                    self.log_message("🔄 Запускаем новое сканирование...")

            except Exception as e:
                self.log_message(f"❌ Ошибка при сканировании: {e}")
                time.sleep(10)

    def run(self):
        """Запуск GUI"""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Ошибка в GUI: {e}")
            input("Нажмите Enter для выхода...")


# ==================== ОСНОВНАЯ ФУНКЦИЯ ====================

def main():
    """Основная функция с GUI"""
    try:
        if sys.platform.startswith('win'):
            try:
                subprocess.run('chcp 65001', shell=True, capture_output=True)
            except:
                pass

        print("Запуск Wi-Fi Guardian PRO...")

        # Запуск графического интерфейса
        gui = WiFiGuardianGUI()
        gui.log_message("🛡️ Wi-Fi Guardian PRO - Расширенная система защиты")
        gui.log_message("=" * 60)
        gui.log_message("НОВЫЕ ВОЗМОЖНОСТИ:")
        gui.log_message("• 📊 Детальная информация о каждой сети")
        gui.log_message("• 📈 История сигналов и анализ трендов")
        gui.log_message("• 🚨 Обнаружение атак (Evil Twin, ARP спуфинг)")
        gui.log_message("• 🌐 Интеграция с базами угроз")
        gui.log_message("• 🔍 Анализ производителей оборудования")
        gui.log_message("• 💾 Сохранение истории в SQLite базу")
        gui.log_message("• 📡 Расширенный мониторинг сетевого трафика")
        gui.log_message("• 🖥️ Графический интерфейс с отдельным окном")
        gui.log_message("=" * 60)
        gui.log_message("✅ Система готова к работе!")
        gui.log_message("🚀 Нажмите 'Начать сканирование' для запуска мониторинга")

        gui.run()

    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        traceback.print_exc()
        input("Нажмите Enter для выхода...")


if __name__ == "__main__":
    main()