# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
def productFib(prod,f0=0,f1=1):
    if f0*f1 == prod:
        return [f0,f1,True]
    elif prod < f0*f1:
        return [f0,f1,False]
    return productFib(prod,f1,f1+f0)

# I like this solution
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]