# https://www.codewars.com/kata/5270d0d18625160ada0000e4
def score(dice):
    print(dice)
    triples = [1000,200,300,400,500,600]
    singles = [100,0,0,0,50,0]
    points = 0
    
    for i in range(1,7):
        count_num = dice.count(i)
        points += count_num // 3 * triples[i-1]
        points += count_num % 3 * singles[i-1]
            
    return points