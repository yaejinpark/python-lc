"""
Implement a function that accepts 3 integer values a, b, c. 

The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

The triangle inequality theorem states that:

a < b + c,

b < a + c,

c < a + b

"""

def is_triangle(a,b,c):
	return (a < b+c)*(b < a+c)*(c < a+b)

print(is_triangle(1,1,2)) # False
print(is_triangle(3,6,9)) # False
print(is_triangle(1,1,1)) # True
print(is_triangle(3,4,5)) # True