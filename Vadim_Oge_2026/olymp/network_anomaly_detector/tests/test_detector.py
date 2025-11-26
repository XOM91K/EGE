import unittest
import asyncio
from core.anomaly_detector import AnomalyDetector
from core.packet_capture import PacketCapture

class TestAnomalyDetector(unittest.TestCase):
    def setUp(self):
        self.config = {
            'detection': {'threshold': 0.85},
            'ml': {'retrain_interval': 3600}
        }
        self.detector = AnomalyDetector(self.config)
    
    def test_feature_extraction(self):
        """Тест извлечения признаков"""
        test_packets = [
            {
                'size': 1500,
                'src_port': 80,
                'dst_port': 443,
                'ttl': 64,
                'flags': 16
            }
        ]
        
        features = self.detector._extract_ml_features(test_packets)
        self.assertEqual(len(features), 1)
        self.assertEqual(len(features[0]), 7)
    
    async def test_port_scan_detection(self):
        """Тест обнаружения сканирования портов"""
        # Создание тестовых данных сканирования портов
        scan_packets = []
        for port in range(1, 101):
            scan_packets.append({
                'src_ip': '192.168.1.100',
                'dst_port': port,
                'size': 60,
                'protocol': 'TCP'
            })
        
        anomaly = self.detector._detect_port_scan(scan_packets)
        self.assertIsNotNone(anomaly)
        self.assertEqual(anomaly['type'], 'PORT_SCAN')

if __name__ == '__main__':
    unittest.main()