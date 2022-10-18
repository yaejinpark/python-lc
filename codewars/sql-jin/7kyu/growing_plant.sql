-- https://www.codewars.com/kata/58941fec8afa3618c9000184/train/sql

select id, 
  case
    when desired_height <= up_speed then 1
    else ceil((desired_height - up_speed)::decimal/(up_speed - down_speed))::int + 1
  end as num_days
from growing_plant