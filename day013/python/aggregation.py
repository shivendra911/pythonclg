#Aggregation is a HAS-A relationship where one class uses another class, but both objects have independent lifecycles.

#       Student -----> Address
#           HAS-A


                        # Real-Life Example 

                        # College & Student
                        # College has students
                        # If college closes 
                        # Students still exist 


class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address


addr = Address("Delhi", 110001)
s = Student("Shivendra", addr)

print(s.name)
print(s.address.city)
print(s.address.pincode)
