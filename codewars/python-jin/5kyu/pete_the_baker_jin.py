# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python
def cakes(recipe, available):
    for k in recipe:
        if k not in available:
            return 0
    return int(min([available[i]/recipe[i] for i in recipe]))
