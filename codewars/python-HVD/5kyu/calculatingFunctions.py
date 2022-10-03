def zero(x='',y=0): 
    return(callable(x,y))
def one(x='',y=1):     
    return(callable(x,y))
def two(x='',y=2):    
    return(callable(x,y))
def three(x='',y=3):
    return(callable(x,y))
def four(x='',y=4):    
    return(callable(x,y))
def five(x='',y=5):
    return(callable(x,y))
def six(x='',y=6):
    return(callable(x,y))
def seven(x='',y=7):
    return(callable(x,y))
def eight(x='',y=8):
    return(callable(x,y))
def nine(x='',y=9):
    return(callable(x,y))

def plus(x,y='+'):    
    return (y,x)
def minus(x,y='-'):
    return (y,x) 
def times(x,y='*'): 
    return (y,x) 
def divided_by(x,y='/'):
    return (y,x)

def callable(x,y):
    if x == '':
        return(y)
    else:
        return(int(eval(f'{y} {x[0]} {x[1]}')))