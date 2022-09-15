/* 
Given the following table 'decimals':

decimals table schema
id
number1
number2
Return a table with a single column towardzero where the values are the result of number1 + number2 truncated towards zero.
*/

select trunc(cast(number1 + number2 as float)) as towardzero
from decimals