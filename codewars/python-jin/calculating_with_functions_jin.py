# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
def input_parser(operation='operator',num=''):
    return operation(num) if callable(operation) else num
def zero(operation='operator',num=0): #your code here
    return operation(num) if callable(operation) else num
def one(operation='operator',num=1): #your code here
    return operation(num) if callable(operation) else num
def two(operation='operator',num=2): #your code here
    return operation(num) if callable(operation) else num
def three(operation='operator',num=3): #your code here
    return operation(num) if callable(operation) else num
def four(operation='operator',num=4): #your code here
    return operation(num) if callable(operation) else num
def five(operation='operator',num=5): #your code here
    return operation(num) if callable(operation) else num
def six(operation='operator',num=6): #your code here
    return operation(num) if callable(operation) else num
def seven(operation='operator',num=7): #your code here
    return operation(num) if callable(operation) else num
def eight(operation='operator',num=8): #your code here
    return operation(num) if callable(operation) else num
def nine(operation='operator',num=9): #your code here
    return operation(num) if callable(operation) else num

def plus(num): #your code here
    def adder(num2):
        return num+num2
    return adder if callable(num) == False else None
def minus(num): #your code here
    def subtr(num2):
        return num2-num
    return subtr if callable(num) == False else None
def times(num): #your code here
    def mult(num2):
        return num*num2
    return mult if callable(num) == False else None
def divided_by(num): #your code here
    def div(num2):
        return num2//num if num2 != 0 else 0
    return div if callable(num) == False else None