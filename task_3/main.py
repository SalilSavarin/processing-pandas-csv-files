import pandas as pd
import pandasql as ps


def total_profit_month(departments: str, operations: str):
    """
    Функция, которая посчитает прибыль за месяц для каждого подразделения
    :param departments: csv файл с департаментами
    :param operations: csv файл с операциями
    :return: pandas.core.frame.DataFrame
    """
    data = pd.read_csv(departments)
    df_departments = pd.DataFrame(data)
    data = pd.read_csv(operations)
    df_operations = pd.DataFrame(data)
    sql_select = '''
    SELECT year, month, d.name, SUM(income) AS income
    FROM df_operations AS o
    JOIN df_departments d ON o.department_id = d.id 
    GROUP BY year, month, d.name
    ORDER BY year, month, income DESC'''
    df_total_profit_month = ps.sqldf(sql_select, locals())
    return df_total_profit_month


def save_to_csv(df):
    """
    Функция для сохранения данных
    :param df: pandas.core.frame.DataFrame
    :return: None
    """
    df.to_csv('income_out.csv', index=False)


total_profit = total_profit_month('departments.csv', 'operations.csv')
save_to_csv(total_profit)
