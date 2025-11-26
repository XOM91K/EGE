import asyncio
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
import joblib
from datetime import datetime, timedelta
from .signature_engine import SignatureEngine
from .ml_analyzer import MLAnalyzer

class AnomalyDetector:
    def __init__(self, config):
        self.config = config
        self.signature_engine = SignatureEngine()
        self.ml_analyzer = MLAnalyzer(config)
        
        # Модели машинного обучения
        self.isolation_forest = IsolationForest(
            contamination=0.1,
            random_state=42
        )
        self.dbscan = DBSCAN(eps=0.5, min_samples=10)
        
        # Исторические данные для анализа временных паттернов
        self.temporal_data = []
        self.baseline_established = False
        
    async def analyze_batch(self, packet_batch):
        """Анализ батча пакетов на аномалии"""
        anomalies = []
        
        # 1. Сигнатурный анализ
        signature_anomalies = await self.signature_engine.analyze(packet_batch)
        anomalies.extend(signature_anomalies)
        
        # 2. Поведенческий анализ
        features = self._extract_ml_features(packet_batch)
        if len(features) > 0:
            behavioral_anomalies = await self.ml_analyzer.detect_anomalies(features)
            anomalies.extend(behavioral_anomalies)
        
        # 3. Временной анализ
        temporal_anomalies = await self._analyze_temporal_patterns(packet_batch)
        anomalies.extend(temporal_anomalies)
        
        return anomalies
    
    def _extract_ml_features(self, packet_batch):
        """Извлечение признаков для ML"""
        features = []
        
        for packet in packet_batch:
            feature_vector = [
                packet['size'],
                packet['src_port'],
                packet['dst_port'],
                packet['ttl'],
                packet['flags'],
                # Дополнительные engineered features
                self._calculate_entropy(packet.get('src_ip', '')),
                self._calculate_entropy(packet.get('dst_ip', ''))
            ]
            features.append(feature_vector)
        
        return np.array(features)
    
    def _calculate_entropy(self, data):
        """Расчет энтропии для обнаружения случайности"""
        if not data:
            return 0
        
        from collections import Counter
        counter = Counter(data)
        total_len = len(data)
        
        entropy = 0
        for count in counter.values():
            p = count / total_len
            entropy -= p * np.log2(p)
        
        return entropy
    
    async def _analyze_temporal_patterns(self, packet_batch):
        """Анализ временных паттернов"""
        anomalies = []
        current_time = datetime.now()
        
        # Анализ частоты пакетов
        if len(packet_batch) > 1000:  # Подозрительно высокий трафик
            anomalies.append({
                'type': 'HIGH_TRAFFIC_VOLUME',
                'severity': 'MEDIUM',
                'description': f'Unusually high packet volume: {len(packet_batch)}',
                'timestamp': current_time
            })
        
        # Анализ паттернов портов
        port_scan_anomaly = self._detect_port_scan(packet_batch)
        if port_scan_anomaly:
            anomalies.append(port_scan_anomaly)
        
        return anomalies
    
    def _detect_port_scan(self, packet_batch):
        """Обнаружение сканирования портов"""
        src_ports = {}
        dst_ports = {}
        
        for packet in packet_batch:
            src_ip = packet.get('src_ip', '')
            dst_port = packet.get('dst_port', 0)
            
            if src_ip and dst_port > 0:
                if src_ip not in src_ports:
                    src_ports[src_ip] = set()
                src_ports[src_ip].add(dst_port)
        
        # Проверка на сканирование портов
        for src_ip, ports in src_ports.items():
            if len(ports) > 50:  # Пороговое значение
                return {
                    'type': 'PORT_SCAN',
                    'severity': 'HIGH',
                    'description': f'Possible port scan from {src_ip} to {len(ports)} different ports',
                    'timestamp': datetime.now()
                }
        
        return None
    
    async def periodic_retrain(self):
        """Периодическое переобучение моделей"""
        while True:
            await asyncio.sleep(self.config['ml']['retrain_interval'])
            await self.ml_analyzer.retrain_models()