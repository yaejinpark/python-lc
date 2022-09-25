-- https://www.codewars.com/kata/580d08b5c049aef8f900007c/train/sql

select cu.customer_id, cu.email, count(p.payment_id) as payments_count, sum(p.amount)::float as total_amount
from customer as cu
join payment as p on p.customer_id = cu.customer_id
group by cu.customer_id
order by total_amount desc
limit 10