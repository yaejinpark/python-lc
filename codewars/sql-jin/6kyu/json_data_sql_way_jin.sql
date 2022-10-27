-- https://www.codewars.com/kata/5daf515c3affec002b2fb921/train/sql

SELECT 
  data ->>'first_name' as first_name,
  data ->> 'last_name' as last_name,
  extract(year from age(now(),(data ->> 'date_of_birth')::date)) as age,
--   data #> '{email_addresses,0}'
  case
    when data ->> 'private' = 'true' then 'Hidden'
    when data ->> 'private' = 'false' and data #>> '{email_addresses,0}' is NULL then 'None'
    when data ->> 'email_addresses' is NULL then 'None'
    else data #>> '{email_addresses,0}'
  end as email_address
FROM users
order by first_name,last_name