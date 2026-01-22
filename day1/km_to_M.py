print("Choose conversion:")
print("1. Kilometer to Meter")
print("2. Meter to Kilometer")

choice = int(input("Enter your choice (1 or 2): "))

value = float(input("Enter the value: "))

if choice == 1:
    result = value * 1000
    print(result, "meters")

elif choice == 2:
    result = value / 1000
    print(result, "kilometers")

else:
    print("Invalid choice")
