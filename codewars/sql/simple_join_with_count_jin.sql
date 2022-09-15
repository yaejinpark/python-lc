-- https://www.codewars.com/kata/580918e24a85b05ad000010c/train/sql
select p.id,p.name,count(toys.id) as toy_count
from people as p
join toys on toys.people_id = p.id
group by p.id;