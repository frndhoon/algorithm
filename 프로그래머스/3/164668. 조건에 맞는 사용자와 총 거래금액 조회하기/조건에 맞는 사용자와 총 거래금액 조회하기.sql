SELECT u.USER_ID, u.NICKNAME, SUM(b.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER u

JOIN (SELECT WRITER_ID, PRICE, STATUS
      FROM USED_GOODS_BOARD
      WHERE STATUS = 'DONE'
      ) b ON b.WRITER_ID = u.USER_ID

GROUP BY b.WRITER_ID HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES