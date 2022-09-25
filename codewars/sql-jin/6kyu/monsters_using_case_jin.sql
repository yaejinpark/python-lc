-- https://www.codewars.com/kata/593ef0e98b90525e090000b9/train/sql
select 
  t.*,
  b.legs,
  b.tails,
  case
    when t.heads > t.arms or b.tails > b.legs then 'BEAST'
    else 'WEIRDO'
  end as species
from top_half as t
join bottom_half as b on t.id = b.id
order by species