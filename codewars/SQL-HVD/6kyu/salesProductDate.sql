SELECT p.name AS product_name, 
DATE_PART('year', s.date) AS year, 
DATE_PART('month', s.date) AS month,
DATE_PART('day', s.date) AS day,
SUM(sd.count*p.price) AS total
FROM sales s
JOIN sales_details sd ON s.id = sd.sale_id
JOIN products p ON p.id = sd.product_id
GROUP BY product_name, ROLLUP (year, month, day)
ORDER BY product_name, year, month, day nulls last;