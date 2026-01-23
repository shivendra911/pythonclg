usr = float(input("enter the length of side 1: "))
usr2 = float(input("enter the length of side 2: "))
usr3 = float(input("enter the length of side 3: "))

if usr + usr2 > usr3 and usr + usr3 > usr2 and usr2 + usr3 > usr:
    print("The lengths can form a valid triangle.")
else:
    print("The lengths cannot form a valid triangle.")

# Alternative approach using a function

def is_valid_triangle(a, b, c):
    # Sort the sides
    s = sorted([a, b, c])
    # Check if sum of two smaller sides > largest side
    return s[0] + s[1] > s[2]


if is_valid_triangle(usr, usr2, usr3):
    print("The lengths can form a valid triangle.")
else:
    print("The lengths cannot form a valid triangle.")