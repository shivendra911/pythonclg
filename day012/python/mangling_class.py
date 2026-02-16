class students:


    def __init__(self,name,attendance):
        self.name = name
        self.__attendance = attendance

    def mark_present(self):
        self.__attendance += 1

    def mark_absent(self):
        self.__attendance -= 1

    def is_elgible(self):
        return self.__attendance >= 75
    
    def get_attendance(self):
        return self.__attendance
    

a = students("abhishek",79)
print(a.get_attendance())
print(a.is_elgible())

# a.mark_absent()
# print(a.get_attendance())

# a.mark_absent()
# print(a.get_attendance())

a._students__attendance = 14
print(a.get_attendance())



        