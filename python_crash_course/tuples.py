# tuples are lists of items that connot be changed (an immutable list)

dimensions = (10, 20)

print(dimensions[0])
print(dimensions[1])

# a list on the other hand is mutable
dimension = [10, 20]
dimension[0] = 250
print(dimensions)

# for loops in tuples 
for tuples in dimensions:
    print(tuples)


# Writing over a Tuple 

print("\nOriginal Dimensions")
 
for value in dimensions:
    print(value)

print("\nModified Dimensions")
dimensions = (20, 200)
for value in dimensions:
    print(value)


#  TRY IT YOURSELF 

menu = ("pizza", "burger", "spagetti", "lentil soup", "pancakes")

print("\nHere is our menu: \n")
for foods in menu:
    print(foods)

menu = ("pizza", "crepe", "scrambled eggs", "lentil soup", "pancakes")

print("\n Our new menu:\n")
for foods in menu:
    print(foods)