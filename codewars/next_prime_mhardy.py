


# def is_prime(num):
#     # define flag variable
#     flag = False
#     if num == 1 or num == 0:
#         flag = True
#         return flag

#     # check for factors
#     for i in range(num+1, num*2):
#         if (num % i) == 0:
#             # if factor is found set flag to true
#             flag=True
#             # break the loop
#             break
#     # check if flag is true
#     return flag

def is_prime(num):
    # return all will return boolean value, false if there are any 0 values,
    # true if there are remainders for all nums (meaning the number is prime)
    return all(num % i for i in range(2, num))
        
def next_prime(x):
    if x <= 1 :
        return 2
    some_list = []
    # check modulus for every number between number and num * 2
    for i in range(x+1,x*2):
        if is_prime(i):
            some_list.append(i)
    print("list of next prime number candidates: ",some_list)
    # return first occurance of number with false return from is_prime
    return min(some_list)

# def next_prime(num):
#     for i in range(num+1, 2*num):
#         return min(is_prime(i))


# def next_prime(num):
#     if num == 0:
#         return 2

#     prime = num+1
#     for i in range(num+1,num*2):
#         if is_prime(prime) == False:
#             return prime
#         else:
#             prime += 1
#             i+=1




number_to_check = 19
print(next_prime(number_to_check))