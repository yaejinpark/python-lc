# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python

def power_of_two(x):
  # your code here
    x_bin = bin(x)[2:] # converts integer to binary
    return x_bin.count('1') == 1