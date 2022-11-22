# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds):
    minutes,sec = divmod(seconds,60)
    hours,minutes = divmod(minutes,60)
    
    return '{:02d}:{:02d}:{:02d}'.format(hours,minutes,sec)