def sort_dicts_by_name(data, reverse=False):
    """
    Функция для сортировки списка словарей по ключу 'name'.

    Args:
        data (list): Список словарей, каждый из которых содержит ключ 'name'.
        reverse (bool): Если True, сортировка по убыванию.

    Returns:
        list: Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['name'], reverse=reverse)


# Пример использования
if __name__ == "__main__":
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]

    sorted_data = sort_dicts_by_name(data)
    print("Отсортировано по возрастанию:", sorted_data)

    sorted_data_desc = sort_dicts_by_name(data, reverse=True)
    print("Отсортировано по убыванию:", sorted_data_desc)