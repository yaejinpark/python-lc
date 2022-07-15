"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

"""

# Problem was simple, but the solution was too brilliant.

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

"""
You can add boolean values in Python (True -> 1, False -> 0). 
For example, if b == 27 then you get for (b > 30) + (b > 25) + (b > 18.5) -> False + True + True -> 0 + 1 + 1 -> 2 [
'Underweight', 'Normal', 'Overweight', 'Obese'][2] -> 'Overweight'
"""