# https://www.codewars.com/kata/58e230e5e24dde0996000070
# ======== Initial Attempt ===========
# def is_prime(num):
#     flag = False
#     if num == 1 or num == 0:
#         flag = True
#         return flag

#     for i in range(num, num+1000):
#         if (num % i) == 0:
#             flag = True
#             break
#     return flag

# def next_prime(n):
#     # have fun ^.^
#     if n == 0:
#         return 2
    
#     prime = n+1
#     for i in range(1,prime):
#         if is_prime(prime):
#             return prime
#         else:
#             prime += 1
# =======================================

def is_prime(x):
    return all(x % i for i in range(2,x))
    """
    all() returns True or False depending on the elements in the iterable. 
    If all elements are NOT 0 or False, all() returns True. 
    If even one element is 0 or False, all() returns False.
    ** Note: Empty lists/tuples return True for all().
    """
# def next_prime(x):
#     return min([a for a in range(x+1, 2*x) if is_prime(a)])

# next_prime() broken down for easier comprehension
def next_prime(x):
    # Corner case: return 2 if x is 0 or 1
    if x <= 1 :
        return 2
    some_list = []
    for i in range(x+1,x*2):
        if is_prime(i):
            some_list.append(i)
    """
    Any number that is not a prime number should have a 0 for modulo in is_prime(), which makes is_prime() False.
    some_list should only contain prime numbers within the given range, which is 1 greater than given number at the minimum.

    """
    # return the smallest prime number in some_list
    return min(some_list)

# testing
prime_number = 17
# is_prime(prime_number)
print(next_prime(prime_number)) # Should return 19

# some fancy one-liner
def next_prime(n):
    if n <= 1:
        return 2
    return min([num for num in range(n+1,n*2) if all(num%i for i in range(2,n))])