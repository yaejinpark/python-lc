-- https://www.codewars.com/kata/5d50e3914861a500121e1958/train/sql
select coalesce(chr(cast((sum(ascii(letter) - 96)-1)%26 as int) + 97),'z') as letter
from letters