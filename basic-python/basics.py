import math_utils
import requests


print("Requests package installed successfully")


result1 = math_utils.add(10, 5)
result2 = math_utils.subtract(10, 5)

print(result1)
print(result2)



# variables
name = "Nandini"
age = 22

print(name)
print(age)

# list
languages = ["Python", "JavaScript", "Java"]

print(languages)
print(languages[1])

# dictinory

student = {
    "name" : "NANDINI",
    "email" : "shriv2@gmail.com",
    "age": 23,
    "subjects": ["math", "sst", "biology"]

}

print(student["subjects"])
print(student["subjects"][1])  #for particular subject

# programing flow => if; if-else; elif

age = 20

if age >= 18:
    print("You are eligible to vote")


age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are NOT eligible to vote")


marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# if with dictionary
student = {
    "name": "NANDINI",
    "age": 23,
    "is_active": True
}

if student["is_active"]:
    print("Student is active")
else:
    print("Student is inactive")

#LOOPS

courses = ["math", "sst", "biology"]

for subject in courses:
    print(subject)

student = {
    "name": "NANDINI",
    "age": 23,
    "email": "shriv2@gmail.com"
}

for key in student:
    print(key, student[key])

# while 

count = 1

while count <= 5:
    print(count)
    count = count + 1

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)



# functions

def greet_user(name):
    print("Hello", name)

greet_user("Nandini")
greet_user("Alex")

def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
print(check_age(15))



def calculate_total(marks):
    return sum(marks)

marks = [80, 75, 90]
total = calculate_total(marks)
print("Total marks:", total)

# input- output

name = "Nandini"
age = 23

print(f"My name is {name} and my age is {age}")


# input
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")


#   using with functions

def greet_user(name):
    print(f"Welcome {name}")

username = input("Enter username: ")
greet_user(username)

# writing and reading

file = open("data.txt", "w")
file.write("Hello Python File")
file.close()


file = open("data.txt", "r")
content = file.read()
file.close()

print(content)



# __init__

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 

#  method
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_price(self):
        print(f"Product price is {self.price}")

p1 = Product("Laptop", 50000)
p1.show_price()
