def calculate_structure_sum(data):
    total_sum = 0

    # Обрабатываем разные типы данных
    if isinstance(data, int):  # Если элемент — число
        total_sum += data
    elif isinstance(data, str):  # Если элемент — строка
        total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):  # Если элемент — список, кортеж или множество
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):  # Если элемент — словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum

# Входные данные
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызов функции
result = calculate_structure_sum(data_structure)

# Вывод результата
print(result)  # 99
