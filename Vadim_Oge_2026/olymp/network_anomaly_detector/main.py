#!/usr/bin/env python3
import asyncio
import logging
import signal
import sys
from datetime import datetime
from core.packet_capture import PacketCapture
from core.anomaly_detector import AnomalyDetector
from utils.visualizer import RealTimeVisualizer
from utils.alert_system import AlertSystem

class NetworkAnomalyDetector:
    def __init__(self, config_path="config/config.yaml"):
        self.config = self.load_config(config_path)
        self.setup_logging()
        
        self.packet_capture = PacketCapture(self.config)
        self.anomaly_detector = AnomalyDetector(self.config)
        self.visualizer = RealTimeVisualizer()
        self.alert_system = AlertSystem(self.config)
        
        self.is_running = False
        
    def load_config(self, config_path):
        import yaml
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('anomaly_detector.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    async def start(self):
        self.is_running = True
        self.logger.info("Starting Network Anomaly Detection System")
        
        # Запуск компонентов
        await asyncio.gather(
            self.packet_capture.start_capture(),
            self.process_packets(),
            self.visualizer.start_dashboard(),
            self.anomaly_detector.periodic_retrain()
        )
    
    async def process_packets(self):
        """Обработка захваченных пакетов"""
        async for packet_batch in self.packet_capture.get_packets():
            # Анализ на аномалии
            anomalies = await self.anomaly_detector.analyze_batch(packet_batch)
            
            # Оповещения и визуализация
            for anomaly in anomalies:
                await self.alert_system.send_alert(anomaly)
                self.visualizer.update_data(anomaly)
    
    def stop(self):
        self.is_running = False
        self.packet_capture.stop()
        self.visualizer.stop()
        self.logger.info("System stopped")

def signal_handler(signum, frame):
    print("\nShutting down...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    
    detector = NetworkAnomalyDetector()
    asyncio.run(detector.start())