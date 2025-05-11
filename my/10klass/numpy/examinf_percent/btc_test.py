def test_graph():
    # Проверка данных API
    assert "prices" in data, "В ответе API нет ключа 'prices'"
    assert len(prices) > 0, "Данные о ценах пустые"

    # Получаем текущие оси
    ax = plt.gca()

    # Проверка параметров графика
    assert ax.get_title() == "Курс биткоина за последние 7 дней (USD)", "Неверный заголовок"
    assert ax.get_xlabel() == "Дата", "Неверная подпись оси X"
    assert ax.get_ylabel() == "Цена (USD)", "Неверная подпись оси Y"
    assert ax.gridOn, "Сетка не включена"

    # Проверка формата дат (первые 3 значения)
    line = ax.get_lines()[0]
    x_data = line.get_xdata()
    assert all(isinstance(x, str) and len(x) == 5 and '.' in x for x in x_data[:3]), "Неверный формат дат"

    return "Все тесты пройдены!"


# Запуск теста
try:
    test_result = test_graph()
    print(test_result)
    plt.show()  # Показываем график только если тесты прошли
except AssertionError as e:
    print(f"Тест не пройден: {e}")
except Exception as e:
    print(f"Ошибка: {e}")