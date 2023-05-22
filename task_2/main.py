import csv
import pandas as pd


def open_and_read_csv_whithout_pd(file_name: str) -> list:
    """
    Функция читает .csv файл
    :param file_name: .csv файл
    :return: список с числами из .csv файла
    """
    some_list = list()
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for item in reader:
            some_list.append(', '.join(item))
        some_list.remove(some_list[0])
    result_list = [int(elem) for elem in some_list]
    return result_list


def open_and_read_csv_pd(file_name: str) -> list:
    """
    Функция читает .csv фай
    :param file_name: .csv файл
    :return: список с числами из .csv файла
    """
    data = pd.read_csv(file_name)
    result_list = data['value'].tolist()
    return result_list


def max_length_1(some_list: list) -> int:
    """
    Функция для подсчета длины максимальной последовательности, положительных чисел в списке.
    :param some_list: список с int
    :return: int максимальная длинна последовательности
    """
    result_list = list()
    count_list = list()
    length_count = 0
    for elem in some_list:
        if elem >= 1:
            result_list.append(elem)
            length_count += 1
            count_list.append(length_count)
        elif elem <= 0:
            result_list.clear()
            length_count = 0
    length = max(count_list)
    return length


def max_length_2(some_list: list) -> int:
    """
    Функция для подсчета длины максимальной последовательности, положительных чисел в списке.
    :param some_list: список с int
    :return: int максимальная длинна последовательности
    """
    length_count = 0
    max_length_count = 0
    for elem in some_list:
        if elem >= 1:
            length_count += 1
        else:
            if length_count > 0:
                max_length_count = max(max_length_count, length_count)
                length_count = 0
    return max(max_length_count, length_count)


def save_result_to_csv(result: int) -> None:
    """
    Функция для сохранения результата
    :param result: int
    :return: создает файл в директории "numbers_out.csv"
    """
    with open("numbers_out.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(['max_length'])
        file_writer.writerow([f'{result}'])


numbers = open_and_read_csv_pd('numbers.csv')
result = max_length_2(numbers)
save_result_to_csv(result)
