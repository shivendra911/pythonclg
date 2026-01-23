usr = int(input("Enter a number: "))
usr2 = int(input("Enter another number: "))
usr3 = int(input("Enter a third number: "))
if usr >= usr2 and usr >=usr3:
    print(f"{usr} is the largest number.")
elif usr2 >= usr and usr2 >= usr3:
    print(f"{usr2} is the largest number.")
else:
    print(f"{usr3} is the largest number.")
    