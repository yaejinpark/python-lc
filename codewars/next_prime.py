
# Write a function that accepts an integer and returns the first prime number of greater value


def is_prime(num):
    # return all will return boolean value, false if there are any 0 values,
    # true if there are remainders for all nums (meaning the number is prime)
    return all(num % i for i in range(2, num))
        
def next_prime(x):
    if x <= 1 :
        return 2
    some_list = []
    # check modulus for every number between number and num * 2
    for i in range(x+1,x*2):  # <= THIS RANGE NEEDS TO BE OPTIMIZED TO REDUCE RUNTIME
        if is_prime(i):
            some_list.append(i)
    print("list of next prime number candidates: ",some_list)
    # return first occurance of number with false return from is_prime
    return min(some_list)


number_to_check = 25
print(next_prime(number_to_check))