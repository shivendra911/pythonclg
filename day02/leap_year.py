usr = int(input("Enter a number: "))
# Check if the year is a leap year
if (usr % 4 == 0 and usr % 100 != 0) or (usr % 400 == 0):
    print(f"{usr} is a leap year.")
else:
    print(f"{usr} is not a leap year.") 