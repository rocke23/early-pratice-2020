from random import randit as ri
import math
from random import randint as ri
from traceback import print_tb


def inp(text):
    return int(input(text))


def inp(text):
    return int(input(text))


def inp(text):
    return int(input(text))


def inp(text):
    return int(input(text))


print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # Integer
gpa = 3.5  # Decimal
is_tall = True  # Boolean -> True/False
name = "John"
print("your name is " + name)
print("Your name is", name)

print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # Integer
gpa = 3.5  # Decimal
is_tall = True  # Boolean -> True/False
name = "John"
print("your name is " + name)
print("Your name is", name)

print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # Integer
gpa = 3.5  # Decimal
is_tall = True  # Boolean -> True/False
name = "John"
print("Your name is " + name)
print("Your name is", name)

print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # Integer
gpa = 3.5  # Decimal
is_tall = True  # Boolean -> True/False
name = "John"
print("Your name is " + name)
print("Your name is", name)

print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # integer
gpa = 3.5  # Decimal
is_tall = True  # Boolean -> True/False
name = "John"
print("Your name is " + name)
print("Your name is", name)

print("Hello")
print("World")
print("!")
name = "Mike"  # Strings
age = 30  # Integer
is_tall = True  # Boolean -> True/False
name = "John"
print("Your name is " + name)
print("Your name is", name)

print(int(3.14))
print(float(3))
print(str(True))
print(int("50") + int("70"))

print(int(3.14))
print(float(3))
print(str(True))
print(int("50") + int("70"))
print(int(3.14))
print(float(3))
print(str(True))
print(int("50") + int("70"))

# Strings

greeting = "Hello"
# indexes: 01234
print(len(greeting))
print(greeting[0])
print(greeting[-1])
print(greeting.find("110"))
print(greeting.find("2"))
print(greeting[2:])
print(greeting[2:3])

# Strings
greeting = "Hello"
# indexes: 01234
print(len(greeting))
print(greeting[0])
print(greeting[-1])
print(greeting.find("110"))
print(greeting.find("2"))
print(greeting[2:])
print(greeting[2:3])
# Numbers
print(2*3)  # Basic Arithmetic: +,-,/, *
print(2**3)  # Basic Arithmetic: +,-,/,*
print(1 + 2 * 3)  # order of operations
print(10 / 3.0)  # int's and doubles

num = 10
num += 100  # +=, -=, /= *=
print(num)

++num
print(num)
# math class has useful math methods
print(pow(2, 3))
print(math.sqrt(144))
# USER INPUT
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)
# Math class has useful math methods
print(pow(2, 3))
print(math.sqrt(144))
# USER INPUT
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)

# Math class has useful math methods
print(pow(2, 3))
print(math.sqrt(144))
# USER INPUT
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)

# LISTs
lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
# indexes       0  1    2         3   4  5

lucky_numbers[0] = 90
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[2])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))

# N Dimentional Lists
numberGrid = [[1, 2], [3, 4]]
numberGrid[0][1] = 99
print(numberGrid[0][0])
print(numberGrid[0][1])
numberGrid = [[1, 2], [3, 4]]
numberGrid[0][1] = 99
print(numberGrid[0][0])
print(numberGrid[0][1])

# LIST fUNCTION
friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1, "Kevin")
friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1, "Kevin")

print(friends)
print(friends.index("Oscar"))
print(friends.count("Angela"))
friends.sort()
print(friends)
friends.clear()
print(friends)
# friends.remove("Kevin")
print(friends)
print(friends.index("Oscar"))
print(friends.count("Angela"))
friends.sort()
print(friends)
friends.clear()
print(friends)
# friends.remove("Kevin")
print(friends)
print(friends.index("Oscar"))
print(friends.count("Angela"))
friends.sort()
print(friends)
friends.clear()
print(friends)
# TUPLES
lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
# indexes        0 1   2       3   4  5
#lucky_numbers[0] = 90
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))
# Function


def add_numbers(num1, num2=99):
    return num1 + num2


sum = add_numbers(4, 3)
print(sum)
# If Statements
is_student = False
is_smart = False

# if Statements
is_student = False
is_smart = False

if is_student and is_smart:
    print("you are a student")
elif is_student and not(is_smart):
    print("You are not a smart student")
else:
    print("Your are not a student and not smart")
# >, <, >= <=, !=, ==
if is_student and is_smart:
    print("you are a student")
elif is_student and not (is_smart):
    print("your are not a smart student")
else:
    print("your are noot a student and not smart")

# >, <, >=, <=, !=, ==

if 1 > 3:
    print("number comparison was false")
if "dog" == "cat":
    print("string comparison was false")

test_grades = {
    "Andy": "B+",
    "Stand": "C",
    "Ryan": "A",
    3: 95.2
}
print(test_grades["Andy"])
print(test_grades.get("Ryan", "No student Found"))
print(test_grades.get("Ry" "No student Found"))
print(test_grades[3])
# while loop
index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 32:
    print(index)
    index += 1

index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 5:
    print(index)
    index += 1
index = 1
while index <= 5:
    print(index)
    index += 1

# for loop
for index in range(5):
    print(index)
for index in range(232232):
    print(index)
lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_nums)

# for loop
for index in range(5):
    print(index)
for index in range(2234234):
    print(index)
lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_nums)

lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_nums)
for letter in "Giraffe":
    print(letter)
for letter in "gifafe":
    print(letter)

# Exception catching
answer = 10 / int(input('Enter Number: '))
answer = 1234 / int(input("Enter Number: "))
try:
    answer = 10 / int(input("Enter Number: "))
except:
    print("Error")
try:
    answer = 1923 / int(input("Enter Number: "))
except:
    print("Error")
try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print("Caught any exception")  # Big no-no


class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    def read_book(self):
        print("Reading", self.title, "by", self.author)


book1 = Book("Howf owo", "Jk Rowling")
book1.title = "half-Blood Price"
print(book1.title)
book1.read_book()
#Getter & Setters


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def title(self):
        print("getting title")
        return self._title

    @title.setter
    def title(self, value):
        print("setting title")
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    def read_book(self):
        print("Reading", self.title, "by", self.author)


book1 = Book("Harry Potter", "JK Rowling")
#book1.title = "Half-Blood prince"
print(book1.title)
book1.read_book()
# inheritance


class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("the chef makes salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def make_pasta(self):
        print("The chef makes pasta")

    def make_special_dish(self):
        print("The chef makes chicken parm")


myChef = Chef()
myChef.make_chicken()
myItalianChef = ItalianChef()
myItalianChef.make_chicken()

myChef = Chef()
myChef.make_special_dish()
myItalianChef = ItalianChef()
myItalianChef.make_special_dish()


class Chef:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def __init__(self, name, age, country_of_origin):
        self.country_of_origin = country_of_origin
        super(). _init_(name, age)

    def make_pasta(self):
        print("The chef makes pasta")

    def make_special_dish(self):
        print("The chef make chicken parm")


myChef = Chef("Gordon Ramsay", 50)
myChef.make_chicken()

myItalianChef = ItalianChef("Massimo Bottura", 55, "Italy")
myItalianChef.make_chicken()
print(myItalianChef.age)


class Chef:
    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def make_Pasta(self):
        print("The chef makes pasta")

    def make_speical_dish(self):
        print("The chef makes chicken parm")


myChef = Chef()
myChef.make_chicken()
myItalianChef = ItalianChef()
myItalianChef.make_chicken()

myChef = Chef()
myChef.make_special_dish()
myItalianChef = ItalianChef()
myItalianChef.make_special_dish()


class Chef:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def make_chicken(self):
        print("The chef makes chicken")

    def make_salad(self):
        print("The chef makes salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def _init_(self, name, age, country_of_origin):
        self.country_of_origin = country_of_origin
        super(). _init_(name, age)

    def make_pasta(self):
        print("The chef makes pasta")

    def make_special_dish(self):
        print("The chef make chicken parm")


myChef = Chef("Gordon Ramsay", 50)
myChef.make_chicken()
myItalianChef = ItalianChef("Massimo Buttura", 55, "Italy")
myItalianChef.make_chicken()
print(myItalianChef.age)


def inp(text):
    return int(input(text))


def inp(text):
    return int(input(text))


def inp(text):
    return int(input(text))


print("Hello")
print("World")
print("!")
name = "Mike"  # string
age = 30  # Integer
gpa = 3.5  # decimal
is_tall = True  # Boolean ->True/False
name = "john"
print("Your name is" + name)
print("Your name is", name)
name = "Jhon"
print("Your name is " + name)
print("your name is", name)

print(int(3.14))
print(float(3))
print(str(True))
print(int("50") + int("70"))
# Strings
print(int(3.14))
print(float(3))
print(str(True))
print(int("50") + int("70"))

print(int(24.5))
print(float(3))
print(str(True))
print(int("50") + int("79"))
print(int(24.24))
print(float(3))
print(str(True))
print(int("52") + int("722"))

# String

greeting = "Hello"
# indexex: 01234
print(len(greeting))
print(greeting[0])
print(greeting[-1])
print(greeting.find("110"))
print(greeting.find("2"))
print(greeting[2:])
print(greeting[2:3])

greeting = "Hello"
# indexes: 01234
print(len(greeting))
print(greeting[0])
print(greeting[-1])
print(greeting.find("110"))
print(greeting.find("2"))
print(greeting[2:])
print(greeting[2:3])

# Number
print(2*3)  # Basic Arithmetic: +, -, /, *
print(2**3)  # Basic Arithmeic: +, -, /, *
print(10 % 3)  # Modules OP: returns remainder of 10 / 3
print(1 + 2 * 3)  # order of operations
print(10 / 3.0)  # int's and doubles

# Numbers
print(2 * 3)  # Basics Arithemtic: +, -, /, *
print(2 ** 3)  # Basic Arithemtic: +, -, /, *
print(10 % 3)  # Modules OP : returns remainder of 10/3
print(1 + 2 * 3)  # order of operations
print(10 / 3.0)  # int's and doubles

num = 10
num += 100  # +=, -=, /= , *=
print(num)

++num
print(num)
++num
print(num)

# Math class has useful math methods
print(pow(2, 3))
print(math.sqrt(144))
print(pow(3, 4))
print(math.sqrt(144))
print(pow(3.2, 24))
print(math.sqrt(144))

# User Input
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))



import math
from random import randit as ri

def inp(text):
    return int(input(text))

print("Hello")
print("World")
print("!")
name = "Mike" #String
age = 30 # Integer
gpa = 3.5 # Decimal
is_tall = True # B

name = "John"
print(int(3.15))
print(float(3))
print(str(True))
print(int("50") + int("70"))

# Strings

greeting = "Hello"
# indexes  01234
print(len(greeting))
print(greeting[0])
print(greeting[-1])
print(greeting.find("110"))
print(greeting.find("2"))
print(greeting[2:])
print(greeting[2:3])

# Numbers
print(2 * 3) # Basic Arithmetic: +, -, /, *
print(1 + 2 * 3) # Basic Arithmetic: +,-,/,*
print(10 % 3) # Modulus Op: returns remainder of 10/3
print(1 + 2 * 3) # order of operations
print(10 / 3.0) # int's and doubles

num = 10
num += 100 # +=, -=, /=, *=
print(num)

++num
print(num)

#Math class has useful math methods
print(pow(2,3))
print(math.sqrt(144))

#USER INPUT
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter second Num: "))
print(num1 + num2)