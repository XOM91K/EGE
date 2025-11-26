import smtplib
import requests
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class AlertSystem:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    async def send_alert(self, anomaly):
        """Отправка оповещения об аномалии"""
        alert_message = self._format_alert(anomaly)
        
        # Логирование
        self.logger.warning(f"ANOMALY DETECTED: {alert_message}")
        
        # Отправка по email
        if self.config['alerts']['email_enabled']:
            await self._send_email_alert(alert_message)
        
        # Webhook уведомление
        if self.config['alerts']['webhook_url']:
            await self._send_webhook_alert(anomaly)
    
    def _format_alert(self, anomaly):
        """Форматирование сообщения об аномалии"""
        return f"""
        🚨 NETWORK ANOMALY DETECTED 🚨
        Type: {anomaly.get('type', 'Unknown')}
        Severity: {anomaly.get('severity', 'Unknown')}
        Description: {anomaly.get('description', 'No description')}
        Timestamp: {anomaly.get('timestamp', datetime.now())}
        """
    
    async def _send_email_alert(self, message):
        """Отправка email оповещения"""
        try:
            # Конфигурация SMTP
            smtp_config = self.config.get('smtp', {})
            
            msg = MIMEMultipart()
            msg['From'] = smtp_config.get('from_email')
            msg['To'] = smtp_config.get('to_email')
            msg['Subject'] = "Network Anomaly Alert"
            
            msg.attach(MIMEText(message, 'plain'))
            
            with smtplib.SMTP(
                smtp_config.get('smtp_server'), 
                smtp_config.get('smtp_port')
            ) as server:
                server.starttls()
                server.login(
                    smtp_config.get('username'),
                    smtp_config.get('password')
                )
                server.send_message(msg)
                
        except Exception as e:
            self.logger.error(f"Failed to send email alert: {e}")
    
    async def _send_webhook_alert(self, anomaly):
        """Отправка оповещения через webhook"""
        try:
            response = requests.post(
                self.config['alerts']['webhook_url'],
                json=anomaly,
                timeout=5
            )
            response.raise_for_status()
        except Exception as e:
            self.logger.error(f"Failed to send webhook alert: {e}")