--Найти города, в которых в 2016 году было издано больше всего книг.
select city_of_publishing, count(*) as books_published, receipt_date - 5 as published_date
    from df
    where receipt_date - 5 = 2016
    group by city_of_publishing
    order by books_published desc;

--Вывести количество экземпляров книг «Война и мир» Л.Н.Толстого, которые находятся в библиотеке.
select count(title) as count_book
    FROM df
    WHERE title LIKE 'Война и мир';

-- Найти читателей, которые за последний месяц брали больше всего книг в библиотеке.
-- При выводе выполнить сортировку читателей по возрасту (от молодых к старшим)
SELECT r.name, count(library_card_number) AS lend, CURRENT_DATE() - date(r.date_of_birth) AS age
    FROM df_lending l
    JOIN df_reader r ON l.library_card_number = r.card_number
    WHERE date(l.date_lend) >= NOW() - INTERVAL 1 MONTH
    GROUP BY library_card_number
    ORDER BY lend DESC, age;
