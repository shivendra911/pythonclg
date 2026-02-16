# Inheritance happens in levels.
#Each class has only one parent, and inheritance goes level by level.
#A → B → C → D
                                            # ✔ Single parent at each level
                                            # ✔ Straight line
                                            # ✔ No branching

                                            # Levels alone ≠ Multilevel
                                            # One parent per class = Multilevel
                                            # More than one parent anywhere = Hybrid


# Grandparent → Parent → Child

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.walk()
d.bark()

