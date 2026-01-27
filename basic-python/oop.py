# Inheritence

class User:
    def __init__(self, name):
        self.name = name
    def login(self):
        print(f"{self.name} logged in")

class Admin(User):
    pass           

admin1 = Admin("Nandini")
admin1.login()


# Encapsulation
# public var
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Alex")
print(s.name)

# protected var
class Student:
    def __init__(self, name):
        self._name = name

# private var
class Student:
    def __init__(self, name):
        self.__name = name


# Polymorphism
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# ABSTRACTION
class Payment:
    def pay(self):
        pass
class CardPayment(Payment):
    def pay(self):
        print("Paid using card")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")
payments = [CardPayment(), UPIPayment()]

for payment in payments:
    payment.pay()


    # instance var and class var
class Student:
    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Nandini")
s2 = Student("Alex")

print(s1.name)
print(s2.name)


class Student:
    school_name = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name
s1 = Student("Nandini")
s2 = Student("Alex")

print(s1.school_name)
print(s2.school_name)

