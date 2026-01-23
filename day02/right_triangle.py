usr = float(input("enter the length of side 1: "))
usr2 = float(input("enter the length of side 2: "))
usr3 = float(input("enter the length of side 3: "))


def is_valid_triangle(a, b, c):
    # Sort the sides
    s = sorted([a, b, c])

    return s[0]**2 + s[1]**2 == s[2]**2
if is_valid_triangle(usr, usr2, usr3):
    print("The lengths can form a right triangle.")
else:
    print("The lengths cannot form a right triangle.")

