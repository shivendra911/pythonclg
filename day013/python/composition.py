# Composition means:

# One class owns another class
# and the child cannot exist without the parent


                                    # Real-Life Example 

                                    # House & Room
                                    # House has rooms
                                    # If house is destroyed 
                                    # Rooms are also destroyed 

# Composition is a relationship where one class contains another class, and the contained object’s lifecycle depends on the container object.


class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()


                                # Car
                                #  └── Engine
                                #      (dies with car)


# Engine cannot exist without Car
# ✔ Strong relationship
# ✔ This is composition



# Use composition when:

# Child object is part of parent

# Child has no independent identity

# Parent controls creation & destruction




#Example
# class Room:
#     def __init__(self, name):
#         self.name = name    

# class House:
#     def __init__(self, address):
#         self.address = address
#         self.rooms = []         

#     def add_room(self, room_name):
#         room = Room(room_name)  
#         self.rooms.append(room)


class hero:
    def __init__(self,help):
        self.help = help


class heroine:
    def __init__(self):
        self.villain = hero("help")

    def happy_ending(self):
        print("Heroine and hero are happy at the end.")