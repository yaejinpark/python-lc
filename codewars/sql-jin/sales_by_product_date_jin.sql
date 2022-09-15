-- https://www.codewars.com/kata/5dac87a0abe9f1001f39e36d/train/sql
select
  p.name as product_name,
  extract(year from s.date) as year,
  extract(month from s.date) as month,
  extract(day from s.date) as day,
  sum(p.price * sd.count) as total
from products as p
left join sales_details as sd on sd.product_id = p.id
left join sales as s on sd.sale_id = s.id
group by product_name, rollup(year,month,day)
order by product_name,year,month,day