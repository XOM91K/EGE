import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import random
from datetime import datetime, timedelta
import matplotlib as mpl

# Настройка стиля
plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'DejaVu Sans'


class BotAnalytics:
    def __init__(self):
        self.period_start = datetime(2025, 11, 20)
        self.period_end = datetime(2025, 12, 3)
        self.stats = self.generate_period_data()

    def generate_period_data(self):
        """Генерация данных за период 20.11.2025-03.12.2025"""
        subjects = ['Математика', 'Русский язык', 'Физика', 'Химия', 'История',
                    'Биология', 'Обществознание', 'Английский язык']

        grades = ['9 класс', '10 класс', '11 класс']
        daily_times = [30, 45, 60, 90, 120]

        # Генерируем данные за указанный период
        subjects_data = {}
        grades_data = {}
        time_data = {}

        # Случайное распределение по предметам
        total_users = 31  # Общее количество пользователей за период
        for subject in subjects:
            subjects_data[subject] = random.randint(15, 35)

        # Корректируем общее количество
        current_total = sum(subjects_data.values())
        scale_factor = total_users / current_total
        for subject in subjects_data:
            subjects_data[subject] = int(subjects_data[subject] * scale_factor)

        # Распределение по классам
        for grade in grades:
            grades_data[grade] = random.randint(45, 75)

        # Распределение по времени
        for time in daily_times:
            time_data[f"{time} мин"] = random.randint(25, 45)

        return {
            'total_users': total_users,
            'subjects': subjects_data,
            'grades': grades_data,
            'daily_time': time_data,
            'period': f"{self.period_start.strftime('%d.%m.%Y')}-{self.period_end.strftime('%d.%m.%Y')}"
        }

    def create_subjects_chart(self):
        """Диаграмма 1: Распределение по предметам"""
        plt.figure(figsize=(12, 8))

        subjects = list(self.stats['subjects'].keys())
        counts = list(self.stats['subjects'].values())

        # Сортируем по убыванию
        sorted_indices = np.argsort(counts)[::-1]
        subjects = [subjects[i] for i in sorted_indices]
        counts = [counts[i] for i in sorted_indices]

        colors = plt.cm.Set3(np.linspace(0, 1, len(subjects)))
        bars = plt.bar(subjects, counts, color=colors, alpha=0.8)

        plt.title(f'📚 РАСПРЕДЕЛЕНИЕ ПО ПРЕДМЕТАМ\nПериод: {self.stats["period"]}',
                  fontsize=16, fontweight='bold', pad=20)
        plt.ylabel('Количество пользователей', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)

        # Добавляем значения на столбцы
        for bar, count in zip(bars, counts):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                     f'{count}', ha='center', va='bottom', fontweight='bold', fontsize=10)

        # Добавляем общее количество
        plt.text(0.02, 0.98, f'Всего пользователей: {self.stats["total_users"]}',
                 transform=plt.gca().transAxes, fontsize=12, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

        plt.tight_layout()
        plt.show()

    def create_grades_chart(self):
        """Диаграмма 2: Распределение по классам"""
        plt.figure(figsize=(10, 8))

        grades = list(self.stats['grades'].keys())
        counts = list(self.stats['grades'].values())

        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        bars = plt.bar(grades, counts, color=colors, alpha=0.8)

        plt.title(f'🎓 РАСПРЕДЕЛЕНИЕ ПО КЛАССАМ\nПериод: {self.stats["period"]}',
                  fontsize=16, fontweight='bold', pad=20)
        plt.ylabel('Количество пользователей', fontsize=12)
        plt.grid(axis='y', alpha=0.3)

        # Добавляем значения и проценты
        total = sum(counts)
        for i, (bar, count) in enumerate(zip(bars, counts)):
            percentage = (count / total) * 100
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                     f'{count}\n({percentage:.1f}%)', ha='center', va='bottom',
                     fontweight='bold', fontsize=11)

        plt.tight_layout()
        plt.show()

    def create_time_chart(self):
        """Диаграмма 3: Время подготовки в день"""
        plt.figure(figsize=(10, 8))

        time_categories = list(self.stats['daily_time'].keys())
        counts = list(self.stats['daily_time'].values())

        # Сортируем по времени
        time_categories_sorted = sorted(time_categories, key=lambda x: int(x.split()[0]))
        counts_sorted = [self.stats['daily_time'][cat] for cat in time_categories_sorted]

        colors = plt.cm.viridis(np.linspace(0, 1, len(time_categories)))
        wedges, texts, autotexts = plt.pie(counts_sorted, labels=time_categories_sorted,
                                           autopct='%1.1f%%', startangle=90, colors=colors,
                                           textprops={'fontsize': 11})

        plt.title(f'⏰ ВРЕМЯ ПОДГОТОВКИ В ДЕНЬ\nПериод: {self.stats["period"]}',
                  fontsize=16, fontweight='bold', pad=20)

        # Улучшаем читаемость текста
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)

        # Добавляем общее количество в центр
        total = sum(counts_sorted)
        plt.text(0, 0, f'Всего\n{total}', ha='center', va='center',
                 fontsize=14, fontweight='bold', transform=plt.gca().transAxes)

        plt.tight_layout()
        plt.show()

    def show_all_charts(self):
        """Последовательно показывает все диаграммы"""
        print("📊 Запуск показа аналитических диаграмм...")
        print(f"📅 Период данных: {self.stats['period']}")
        print(f"👥 Общее количество пользователей: {self.stats['total_users']}")
        print("\n" + "=" * 50)

        input("Нажмите Enter для просмотра первой диаграммы (Распределение по предметам)...")
        self.create_subjects_chart()

        input("Нажмите Enter для просмотра второй диаграммы (Распределение по классам)...")
        self.create_grades_chart()

        input("Нажмите Enter для просмотра третьей диаграммы (Время подготовки в день)...")
        self.create_time_chart()

        print("\n" + "=" * 50)
        print("🎉 Показ всех диаграмм завершен!")
        self.show_summary()

    def show_summary(self):
        """Показывает текстовую сводку"""
        print("\n📈 СВОДКА ПО АНАЛИТИКЕ БОТА:")
        print(f"Период: {self.stats['period']}")
        print(f"Всего пользователей: {self.stats['total_users']}")

        # Самый популярный предмет
        popular_subject = max(self.stats['subjects'], key=self.stats['subjects'].get)
        print(f"Самый популярный предмет: {popular_subject} ({self.stats['subjects'][popular_subject]} пользователей)")

        # Самый активный класс
        active_grade = max(self.stats['grades'], key=self.stats['grades'].get)
        print(f"Наиболее активный класс: {active_grade} ({self.stats['grades'][active_grade]} пользователей)")

        # Самое популярное время
        popular_time = max(self.stats['daily_time'], key=self.stats['daily_time'].get)
        print(f"Наиболее частое время подготовки: {popular_time}")


# Дополнительная функция для сохранения диаграмм в файлы
def save_charts_to_files():
    """Сохраняет все диаграммы в файлы"""
    analytics = BotAnalytics()

    print("💾 Сохранение диаграмм в файлы...")

    # Сохраняем первую диаграмму
    plt.figure(figsize=(12, 8))
    analytics.create_subjects_chart()
    plt.savefig('subjects_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Сохраняем вторую диаграмму
    plt.figure(figsize=(10, 8))
    analytics.create_grades_chart()
    plt.savefig('grades_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Сохраняем третью диаграмму
    plt.figure(figsize=(10, 8))
    analytics.create_time_chart()
    plt.savefig('time_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("✅ Диаграммы сохранены в файлы:")
    print("   - subjects_distribution.png")
    print("   - grades_distribution.png")
    print("   - time_distribution.png")


# Запуск аналитики
if __name__ == "__main__":
    print("🤖 АНАЛИТИКА ИСПОЛЬЗОВАНИЯ TELEGRAM-БОТА")
    print("Генератор учебных планов")
    print("=" * 50)

    # Создаем экземпляр аналитики
    analytics = BotAnalytics()

    # Запускаем показ диаграмм
    analytics.show_all_charts()

    # Опционально: сохраняем диаграммы в файлы
    save_option = input("\nХотите сохранить диаграммы в файлы? (да/нет): ").lower()
    if save_option in ['да', 'д', 'yes', 'y']:
        save_charts_to_files()