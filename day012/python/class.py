class employee:


    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id

    def add_bonus(self, bonus_amount):
        self.salary += bonus_amount
        

    def is_high_earner(self):
        return self.salary > 100000

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")    



a = employee("Ankit",122222,12323629)

a.display_info()
a.add_bonus(12)

a.display_info()

# b = employee("Abhishek",123241234,12313)
# b.is_high_earner()