SELECT top.id, top.heads, top.arms, b.legs, b.tails, 
CASE 
  WHEN top.heads > top.arms OR b.tails > b.legs THEN 'BEAST' 
  ELSE 'WEIRDO' END
AS species
FROM top_half AS top
JOIN bottom_half AS b ON b.id = top.id
ORDER BY species