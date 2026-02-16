#Secure Locker System

class SecureLocker:
    def __init__(self, pin):
        self.__pin = pin              
        self.__is_locked = True      


    def __verify_pin(self, pin):
        return self.__pin == pin

   
    def unlock(self, pin):
        if self.__verify_pin(pin):
            self.__is_locked = False
            print("Locker unlocked")
        else:
            print("Incorrect PIN")

    def lock(self):
        self.__is_locked = True
        print("Locker locked")

    def status(self):
        if self.__is_locked:
            print("Locker is Locked")
        else:
            print("Locker is Unlocked")
