usr = input("Enter a 2-digit number: ").strip()

if usr.isdigit() and len(usr) == 2:
    num = int(usr)
    print("Valid 2-digit integer:", num)
else:
    print("Invalid input")
