-- https://www.codewars.com/kata/5994dafcbddc2f116d000024/train/sql
select 
  player_name,
  games,
  cast(round(cast(hits as numeric)/cast(at_bats as numeric),3) as varchar) as batting_average
from yankees
where at_bats >= 100
order by batting_average desc

-- example of using :: (short way of casting)
select player_name,
       games,
       round(hits::numeric / at_bats, 3)::text as batting_average
from yankees
where at_bats > 100
order by 3 desc