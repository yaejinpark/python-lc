SELECT cus.customer_id, cus.email, 
COUNT(pay.payment_id) as payments_count, 
SUM(pay.amount) :: FLOAT as total_amount 
FROM payment pay
JOIN customer cus ON cus.customer_id=pay.customer_id
GROUP BY cus.customer_id
ORDER BY total_amount DESC
LIMIT 10