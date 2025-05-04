# Импорт библиотек
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime


# Шаг 1: Получение данных из API
def get_launch_data():
    url = "https://ll.thespacedevs.com/2.2.0/launch/upcoming/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return None


# Шаг 2: Обработка данных
def process_data(data):
    if not data or 'results' not in data:
        print("Некорректные данные от API")
        return pd.DataFrame()  # Возвращаем пустой DataFrame

    try:
        # Создаем DataFrame
        launches = pd.DataFrame(data['results'])

        # Извлекаем нужные данные
        processed_data = pd.DataFrame({
            'name': launches['name'],
            'date': pd.to_datetime(launches['net']),
            'status': launches['status'].apply(lambda x: x['name'] if pd.notnull(x) else 'Unknown'),
            'country': launches['pad'].apply(lambda x: x['location']['country_code'] if pd.notnull(x) else 'Unknown'),
            'cosmodrome': launches['pad'].apply(lambda x: x['name'] if pd.notnull(x) else 'Unknown'),
            'lat': launches['pad'].apply(lambda x: x['latitude'] if pd.notnull(x) else None),
            'lon': launches['pad'].apply(lambda x: x['longitude'] if pd.notnull(x) else None),
            'mission_type': launches['mission'].apply(lambda x: x['type'] if x and 'type' in x else 'Unknown')
        })

        return processed_data

    except Exception as e:
        print(f"Ошибка при обработке данных: {e}")
        return pd.DataFrame()


# Шаг 3: Визуализация
def plot_launch_stats(launch_df):
    if launch_df is None or launch_df.empty:
        print("Нет данных для визуализации")
        return

    plt.figure(figsize=(15, 10))

    # График 1: Количество запусков по странам
    plt.subplot(2, 2, 1)
    country_counts = launch_df['country'].value_counts()
    country_counts.plot(kind='bar', color='skyblue')
    plt.title('Количество запусков по странам')
    plt.xlabel('Код страны')
    plt.ylabel('Количество')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')

    # График 2: Запуски по месяцам
    plt.subplot(2, 2, 2)
    launch_df['month'] = launch_df['date'].dt.month_name()
    monthly_counts = launch_df['month'].value_counts().sort_index()
    monthly_counts.plot(kind='line', marker='o', color='green')
    plt.title('Запуски по месяцам')
    plt.xlabel('Месяц')
    plt.ylabel('Количество')
    plt.grid()

    # График 3: Распределение типов миссий
    plt.subplot(2, 2, 3)
    mission_counts = launch_df['mission_type'].value_counts()
    mission_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Распределение типов миссий')
    plt.ylabel('')

    plt.tight_layout()
    plt.show()

    # Интерактивная карта запусков (только если есть координаты)
    if not launch_df[['lat', 'lon']].isnull().all().all():
        try:
            fig = px.scatter_geo(launch_df,
                                 lat='lat',
                                 lon='lon',
                                 hover_name='name',
                                 hover_data=['country', 'cosmodrome', 'mission_type'],
                                 color='country',
                                 scope='world',
                                 title='Карта космодромов с предстоящими запусками')
            fig.show()
        except Exception as e:
            print(f"Ошибка при построении карты: {e}")
    else:
        print("Нет координат для построения карты")


# Основная функция
def main():
    print("Получаем данные о космических запусках...")

    # Получаем данные
    launch_data = get_launch_data()

    if launch_data:
        # Обрабатываем данные
        processed_df = process_data(launch_data)

        if not processed_df.empty:
            print("\nПервые 5 записей:")
            print(processed_df.head())

            # Визуализируем данные
            print("\nСтроим графики...")
            plot_launch_stats(processed_df)
        else:
            print("Не удалось обработать данные - получен пустой DataFrame")
    else:
        print("Не удалось получить данные от API")


if __name__ == "__main__":
    main()