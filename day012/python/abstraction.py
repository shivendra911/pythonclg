from abc import ABC, abstractmethod

class thor_hammer(ABC):
    @abstractmethod
    def worthy(self):
        pass

    def fly(self):
        print(f"rotates and flies")

    def thunder(self):
        print(f"creates thunder")

class thor(thor_hammer):
    def worthy(self):
        print(f"Thor is worthy to lift the hammer")

t1 = thor()
t1.worthy()
t1.fly()
t1.thunder()