SELECT p.PRODUCT_ID, p.PRODUCT_NAME, (o.AMOUNT * p.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT p

JOIN (
     SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT, PRODUCE_DATE
     FROM FOOD_ORDER
     WHERE PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31' # 2022년 5월
     GROUP BY PRODUCT_ID
     ) o ON o.PRODUCT_ID = p.PRODUCT_ID

# 총매출 기준 내림차순 정렬, 식품 ID 기준 오름차순 정렬
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC