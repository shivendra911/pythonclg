usr = float(input("Enter the temperature in Celsius: "))
if usr < 15.0:
    print("It's cold.")
elif 15.0 <= usr <= 30.0:
    print("moderate")
else:
    print("Hot")
