--Найти города, в которых в 2016 году было издано больше всего книг.
SELECT city_of_publishing, COUNT(*) AS books_published, receipt_date - 5 AS published_date
    FROM df
    WHERE receipt_date - 5 = 2016
    GROUP BY city_of_publishing
    ORDER BY books_published DESC;

SELECT COUNT(title) as count_book
    FROM df
    WHERE title LIKE 'Война и мир';



SELECT r.name, COUNT(library_card_number) AS lend, "{0}" - DATE(r.date_of_birth) AS age
    FROM df_lending l
    JOIN df_reader r ON l.library_card_number = r.card_number
    WHERE DATE(l.date_lend) >= "{0}"
    GROUP BY library_card_number
    ORDER BY lend DESC, "{0}" - DATE(r.date_of_birth);
