SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, SUM(b.PRICE * bs.SALES) AS TOTAL_SALES
FROM AUTHOR a

JOIN BOOK b ON a.AUTHOR_ID = b.AUTHOR_ID
JOIN BOOK_SALES bs ON b.BOOK_ID = bs.BOOK_ID

WHERE bs.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'

GROUP BY AUTHOR_NAME, CATEGORY

ORDER BY AUTHOR_ID ASC, CATEGORY DESC

# SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY
# FROM AUTHOR a

# JOIN BOOK b ON a.AUTHOR_ID = b.AUTHOR_ID

# ORDER BY AUTHOR_NAME, CATEGORY