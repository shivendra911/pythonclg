usr = int(input("Enter a number: "))

if usr % 15 == 0:
    print("Divisible by both 3 and 5")
elif usr % 3 == 0:
    print("Divisible by 3")
elif usr % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by either 3 or 5")