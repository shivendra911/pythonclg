

# class Student:
    

#     def __init__(self, name ,marks,roll_no):
#         self.name = name
#         self.marks = marks
#         self.roll_no = roll_no

#     def add_marks(self, marks):
#         self.marks += marks

#     def display(self):
#         print(f"Name: {self.name}, Marks: {self.marks}, Roll No: {self.roll_no}")

#     def is_passed(self):
#         return self.marks >= 40
    
# s1 = Student("Shivendra",35,55)
# s1.display()
# print(s1.is_passed())

# s1.add_marks(10)
# s1.display()
# print(s1.is_passed())





class Student:

    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    def add_marks(self, marks):
        self.marks += marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Roll No: {self.roll_no}")

    def is_passed(self):
        return self.marks >= 40


def menu(student):
    while True:
        print("\n--- Student Menu ---")
        print("1. Display Student Details")
        print("2. Add Marks")
        print("3. Check Pass/Fail")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student.display()

        elif choice == "2":
            marks = int(input("Enter marks to add: "))
            student.add_marks(marks)
            print("Marks updated.")

        elif choice == "3":
            print("PASSED" if student.is_passed() else "FAILED")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


def main():
    # object creation happens here
    s1 = Student("Shivendra", 35, 55)
    menu(s1)


# 👇 THIS makes the menu appear automatically
if __name__ == "__main__":
    main()
