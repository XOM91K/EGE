import subprocess
import re
import platform
import json
from datetime import datetime
import requests


class SafeConnect:
    def __init__(self):
        self.networks = []
        self.results = []

    def scan_networks(self):
        """Сканирование доступных Wi-Fi сетей"""
        print("🔍 Сканирование Wi-Fi сетей...")

        system = platform.system()

        try:
            if system == "Windows":
                self._scan_windows()
            elif system == "Linux":
                self._scan_linux()
            elif system == "Darwin":  # macOS
                self._scan_macos()
            else:
                print("❌ Неподдерживаемая операционная система")
                return False
            return True
        except Exception as e:
            print(f"❌ Ошибка при сканировании: {e}")
            return False

    def _scan_windows(self):
        """Сканирование для Windows"""
        try:
            result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
                                    capture_output=True, text=True, encoding='cp866')

            lines = result.stdout.split('\n')
            current_network = {}

            for line in lines:
                line = line.strip()

                if 'SSID' in line and 'BSSID' not in line:
                    if current_network:
                        self.networks.append(current_network)
                    current_network = {'name': line.split(':')[1].strip(), 'security': 'Unknown'}

                elif 'Authentication' in line:
                    current_network['security'] = line.split(':')[1].strip()

                elif 'Signal' in line:
                    signal_str = line.split(':')[1].strip().replace('%', '')
                    current_network['signal'] = int(signal_str) if signal_str.isdigit() else 0

            if current_network:
                self.networks.append(current_network)

        except Exception as e:
            print(f"Ошибка Windows сканирования: {e}")

    def _scan_linux(self):
        """Сканирование для Linux"""
        try:
            result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SECURITY,SIGNAL', 'dev', 'wifi'],
                                    capture_output=True, text=True)

            for line in result.stdout.split('\n'):
                if line.strip():
                    parts = line.split(':')
                    if len(parts) >= 3:
                        network = {
                            'name': parts[0],
                            'security': parts[1] if parts[1] else 'Open',
                            'signal': int(parts[2]) if parts[2].isdigit() else 0
                        }
                        self.networks.append(network)

        except Exception as e:
            print(f"Ошибка Linux сканирования: {e}")

    def _scan_macos(self):
        """Сканирование для macOS"""
        try:
            result = subprocess.run(
                ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'],
                capture_output=True, text=True)

            lines = result.stdout.split('\n')[1:]  # Пропускаем заголовок

            for line in lines:
                if line.strip():
                    parts = re.split(r'\s+', line.strip())
                    if len(parts) >= 4:
                        network = {
                            'name': parts[0],
                            'security': parts[3] if len(parts) > 3 else 'Unknown',
                            'signal': int(parts[2].replace('-', '')) if parts[2].replace('-', '').isdigit() else 0
                        }
                        self.networks.append(network)

        except Exception as e:
            print(f"Ошибка macOS сканирования: {e}")

    def analyze_network(self, network):
        """Анализ безопасности сети"""
        analysis = {
            'name': network['name'],
            'security_type': network['security'],
            'risk_level': 'Низкий',
            'threats': [],
            'recommendations': []
        }

        # Анализ типа безопасности
        security = network['security'].lower()

        if 'wpa3' in security:
            analysis['risk_level'] = 'Очень низкий'
            analysis['recommendations'].append("✅ WPA3 - современный стандарт безопасности")

        elif 'wpa2' in security:
            analysis['risk_level'] = 'Низкий'
            analysis['recommendations'].append("✅ WPA2 - надежный стандарт безопасности")

        elif 'wpa' in security:
            analysis['risk_level'] = 'Средний'
            analysis['threats'].append("⚠️ WPA устарел и может быть уязвим")
            analysis['recommendations'].append("🔄 Обновите роутер до WPA2/WPA3")

        elif 'wep' in security:
            analysis['risk_level'] = 'Очень высокий'
            analysis['threats'].append("🚨 WEP легко взломать за несколько минут")
            analysis['recommendations'].append("🔄 НЕМЕДЛЕННО обновите безопасность роутера")

        elif 'open' in security or not security or security == 'unknown':
            analysis['risk_level'] = 'Критический'
            analysis['threats'].append("🚨 Открытая сеть - все данные передаются в открытом виде")
            analysis['recommendations'].append("🔒 Избегайте передачи конфиденциальных данных")
            analysis['recommendations'].append("🛡️ Используйте VPN для защиты")

        # Анализ имени сети
        name = network['name'].lower()

        # Подозрительные имена
        suspicious_keywords = ['free', 'public', 'guest', 'openwifi', 'test']
        if any(keyword in name for keyword in suspicious_keywords):
            analysis['threats'].append("⚠️ Имя сети может указывать на публичную/небезопасную сеть")
            analysis['risk_level'] = self._increase_risk(analysis['risk_level'])

        # Сети без имени
        if not name or name == 'unknown':
            analysis['threats'].append("⚠️ Скрытая или анонимная сеть - может быть подозрительной")
            analysis['risk_level'] = self._increase_risk(analysis['risk_level'])

        # Рекомендации по уровню риска
        if analysis['risk_level'] in ['Средний', 'Высокий', 'Очень высокий', 'Критический']:
            analysis['recommendations'].append("🛡️ Обязательно используйте VPN")
            analysis['recommendations'].append("🔐 Избегайте банковских операций и ввода паролей")

        return analysis

    def _increase_risk(self, current_risk):
        """Повышение уровня риска"""
        risk_levels = ['Очень низкий', 'Низкий', 'Средний', 'Высокий', 'Очень высокий', 'Критический']
        current_index = risk_levels.index(current_risk)
        return risk_levels[min(current_index + 1, len(risk_levels) - 1)]

    def display_results(self):
        """Отображение результатов анализа"""
        print("\n" + "=" * 80)
        print("🔒 SAFECONNECT: РЕЗУЛЬТАТЫ АНАЛИЗА БЕЗОПАСНОСТИ СЕТЕЙ")
        print("=" * 80)

        for i, result in enumerate(self.results, 1):
            print(f"\n📡 СЕТЬ #{i}: {result['name']}")
            print(f"   🔐 Тип безопасности: {result['security_type']}")

            # Цветовая индикация уровня риска
            risk_color = {
                'Очень низкий': '🟢',
                'Низкий': '🟢',
                'Средний': '🟡',
                'Высокий': '🟠',
                'Очень высокий': '🔴',
                'Критический': '💀'
            }

            print(f"   {risk_color.get(result['risk_level'], '⚪')} Уровень риска: {result['risk_level']}")

            if result['threats']:
                print("   ⚠️  УГРОЗЫ:")
                for threat in result['threats']:
                    print(f"      • {threat}")

            if result['recommendations']:
                print("   💡 РЕКОМЕНДАЦИИ:")
                for recommendation in result['recommendations']:
                    print(f"      • {recommendation}")

            print("-" * 80)

    def generate_report(self):
        """Генерация отчета"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"safeconnect_report_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("SAFECONNECT - ОТЧЕТ АНАЛИЗА БЕЗОПАСНОСТИ СЕТЕЙ\n")
            f.write(f"Сгенерировано: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")

            for result in self.results:
                f.write(f"СЕТЬ: {result['name']}\n")
                f.write(f"Безопасность: {result['security_type']}\n")
                f.write(f"Уровень риска: {result['risk_level']}\n")

                if result['threats']:
                    f.write("Угрозы:\n")
                    for threat in result['threats']:
                        f.write(f"  - {threat}\n")

                if result['recommendations']:
                    f.write("Рекомендации:\n")
                    for rec in result['recommendations']:
                        f.write(f"  - {rec}\n")

                f.write("\n" + "-" * 40 + "\n")

        print(f"\n📊 Отчет сохранен в файл: {filename}")

    def show_safety_tips(self):
        """Показать советы по безопасности"""
        print("\n" + "=" * 80)
        print("🛡️  ОБЩИЕ РЕКОМЕНДАЦИИ ПО БЕЗОПАСНОСТИ В ПУБЛИЧНЫХ СЕТЯХ")
        print("=" * 80)

        tips = [
            "🔒 Всегда используйте VPN в публичных сетях",
            "🌐 Избегайте посещения банковских сайтов и ввода паролей",
            "📱 Используйте мобильный интернет для важных операций",
            "🔍 Проверяйте правильность имени сети (избегайте 'Free WiFi' и подобных)",
            "🔄 Регулярно обновляйте антивирус и ОС",
            "🚫 Отключайте автоматическое подключение к Wi-Fi",
            "📶 Отключайте Wi-Fi когда не используете",
            "🔐 Используйте двухфакторную аутентификацию везде где возможно"
        ]

        for tip in tips:
            print(f"   • {tip}")

    def run(self):
        """Основной метод запуска программы"""
        print("🚀 ЗАПУСК SAFECONNECT...")
        print("Анализ и защита публичных Wi-Fi сетей")
        print("=" * 50)

        # Сканирование сетей
        if not self.scan_networks():
            return

        if not self.networks:
            print("❌ Не найдено доступных Wi-Fi сетей")
            return

        print(f"📶 Найдено сетей: {len(self.networks)}")

        # Анализ каждой сети
        for network in self.networks:
            analysis = self.analyze_network(network)
            self.results.append(analysis)

        # Отображение результатов
        self.display_results()

        # Генерация отчета
        self.generate_report()

        # Советы по безопасности
        self.show_safety_tips()

        print("\n" + "=" * 80)
        print("✅ АНАЛИЗ ЗАВЕРШЕН! Будьте осторожны в публичных сетях!")
        print("=" * 80)


# Дополнительный модуль для проверки известных уязвимостей
class SecurityChecker:
    @staticmethod
    def check_common_vulnerabilities():
        """Проверка на известные уязвимости"""
        common_threats = [
            "KRACK (Key Reinstallation Attacks) - уязвимость в WPA2",
            "WPS PIN vulnerabilities - возможность подбора PIN",
            "Evil Twin attacks - поддельные точки доступа",
            "Packet sniffing - перехват трафика",
            "DNS spoofing - подмена DNS записей"
        ]

        print("\n🔍 ИЗВЕСТНЫЕ УЯЗВИМОСТИ WI-FI:")
        for threat in common_threats:
            print(f"   ⚠️  {threat}")


if __name__ == "__main__":
    # Проверка прав администратора
    if platform.system() != "Windows":
        import os

        if os.geteuid() != 0:
            print("⚠️  Для полного сканирования запустите программу с правами администратора")

    # Запуск основной программы
    scanner = SafeConnect()
    scanner.run()

    # Дополнительная информация об уязвимостях
    SecurityChecker.check_common_vulnerabilities()