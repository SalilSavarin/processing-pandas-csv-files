import pandas as pd
import pandasql as ps
from dateutil.relativedelta import relativedelta
import datetime


def read_rus_csv(file_name):
    """
    Функция открывает csv файл
    :param file_name: csv файл
    :return: pandas.core.frame.DataFrame
    """
    file_csv = pd.read_csv(file_name, sep=';', encoding='cp1251')
    file_df = pd.DataFrame(file_csv)
    return file_df

# Данный фрагмент кода приводит файлы с данными к рабочему виду
#
# После открытия DataFrame 'Задача3_Книги.csv' были удалены строки с некорректными данными,
# добавлена строки для проверки работы sql-запроса из функции search_city() и search_and_count(),
# переименованы столбцы на английский
books_df = read_rus_csv('Задача3_Книги.csv').drop_duplicates().drop(index=[6, 9, 25, 46, 57, 90])
books_df.columns = ['id_book', 'title', 'author', 'publisher', 'city_of_publishing', 'numbers_of_pages', 'id_copy', 'receipt_date']
new_row = pd.Series(data={'id_book': '100000', 'title': 'Spider', 'author': 'Stan', 'publisher': 'Marvel', 'city_of_publishing': 'Thompsonton', 'numbers_of_pages': '20', 'id_copy': '219412', 'receipt_date': '01.02.2021'}, name='x')
row_with_war_and_peace = pd.Series(data={'id_book': '101111', 'title': 'Война и мир', 'author': 'Л.Н.Толстого', 'publisher': 'Эксмо', 'city_of_publishing': 'Moscow', 'numbers_of_pages': '980', 'id_copy': '2124215', 'receipt_date': '09.09.1873'}, name='x')
books_df = books_df._append(new_row)
books_df = books_df._append(row_with_war_and_peace)
books_df['receipt_date'] = pd.to_datetime(books_df['receipt_date'])

# После открытия DataFrame 'Задача3_Выдачи книг.csv' были удалены строки с некорректными данными,
# переименованы столбцы на английский
book_lending_df = read_rus_csv('Задача3_Выдачи книг.csv')
book_lending_df.columns = ['id_copy', 'date_lend', 'date_return', 'library_card_number']
book_lending_df = book_lending_df.drop(index=[497])
book_lending_df['date_lend'] = pd.to_datetime(book_lending_df['date_lend'])
book_lending_df['date_return'] = pd.to_datetime(book_lending_df['date_return'])

# После открытия DataFrame 'Задача3_Читатели.csv' были переименованы столбцы на английский
reader_df = read_rus_csv('Задача3_Читатели.csv').drop_duplicates()
reader_df.columns = ['card_number', 'last_name', 'name', 'surname', 'date_of_birth', 'gender', 'address', 'phone']
reader_df['date_of_birth'] = pd.to_datetime(reader_df['date_of_birth'])


# Найти города, в которых в 2016 году было издано больше всего книг.
def search_city(file):
    """
    Функция для поиска города, в которых в 2016 году было издано больше всего книг
    :param file: pandas.core.frame.DataFrame Книги
    :return: pandas.core.frame.DataFrame Город и количество книг
    """
    df = file
    sql_select = '''
    SELECT city_of_publishing, COUNT(*) AS books_published, receipt_date - 5 AS published_date
    FROM df
    WHERE receipt_date - 5 = 2016
    GROUP BY city_of_publishing
    ORDER BY books_published DESC
    '''
    select_result_df = ps.sqldf(sql_select, locals())
    return select_result_df


# Вывести количество экземпляров книг «Война и мир» Л.Н.Толстого, которые находятся в библиотеке.
def search_and_count(file):
    """
    Функция, которая найдет количество экземпляров книг «Война и мир» Л.Н.Толстого
    :param file: pandas.core.frame.DataFrame Книги
    :return: pandas.core.frame.DataFrame Количество книг
    """
    df = file
    sql_select = '''
    SELECT COUNT(title) as count_book
    FROM df
    WHERE title LIKE 'Война и мир'
    '''
    select_result_df = ps.sqldf(sql_select, locals())
    return select_result_df


# Найти читателей, которые за последний месяц брали больше всего книг в библиотеке.
# При выводе выполнить сортировку читателей по возрасту (от молодых к старшим)
def search_reader(df_reader, df_lending):
    """
    Функция, которая найдет читателей, бравшего больше всего книг за последний месяц и
    отсортирует по возрасту
    :param df_reader: pandas.core.frame.DataFrame Читатели
    :param df_lending: pandas.core.frame.DataFrame Выдача книг
    :return: pandas.core.frame.DataFrame Читателей
    """
    date = datetime.date.today()
    date_interval = datetime.date.today() - relativedelta(months=1)
    df_reader = df_reader
    df_lending = df_lending
    sql_select = '''
    SELECT r.name, COUNT(library_card_number) AS lend, "{0}" - DATE(r.date_of_birth) AS age
    FROM df_lending l
    JOIN df_reader r ON l.library_card_number = r.card_number
    WHERE DATE(l.date_lend) >= "{1}"
    GROUP BY library_card_number
    ORDER BY lend DESC, age
    '''.format(date, date_interval)
    select_result_df = ps.sqldf(sql_select, locals())
    return select_result_df


print(search_reader(reader_df, book_lending_df))
print(search_city(books_df))
print(search_and_count(books_df))
