print("Data Converter")
print("1. KB to MB")
print("2. MB to KB")
print("3. MB to GB")
print("4. GB to MB")

choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print(value / 1000, "MB")

elif choice == 2:
    print(value * 1000, "KB")

elif choice == 3:
    print(value / 1000, "GB")

elif choice == 4:
    print(value * 1000, "MB")

else:
    print("Invalid choice")
