usr = float(input("enter the length of side 1: "))
usr2 = float(input("enter the length of side 2: "))
usr3 = float(input("enter the length of side 3: "))

if usr == usr2 and usr2 == usr3 and usr3 == usr:
    print("Equilateral")
elif usr != usr2 and usr2 != usr3 and usr3 == usr:
    print("Scalene")
else :
    print("isoceles")


# Alternative approach using a function

if usr + usr2 <= usr3 or usr + usr3 <= usr2 or usr2 + usr3 <= usr:
    print("Not a valid triangle")
else:
    sides = {usr, usr2, usr3}

    if len(sides) == 1:
        print("Equilateral")
    elif len(sides) == 3:
        print("Scalene")
    else:
        print("Isosceles")
