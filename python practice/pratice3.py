import math
from random import randint as ri

def inp(text):
    return int(input(text))

print("Hello")
print("World")
print("!")
name = "Mike" + #String
age = 30 # Integer
gpa = 3.5 # Decimal
is_tall = True # Boolean -> True/ False
name = "John"
print("Your name is" + name)
print("Your name is", name)

print(int(3.14))
print(float(3))
print(str(True))
print(int("50")) + int("70")

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

#NUMBERS
print(2*3) # Basic Arithmetic: +, -, /, *
print(2**3) # Basic Arithmetic: +, -,/,*
print(10 % 3) # Modulus Op : returns remainder of 10/3
print(1 + 2 * 3) #order of operations
print(10 / 3.0) # int's and doubles

num = 10
num += 100 # += -= /= *=
print(num)

++num
print(num)

#Math class has useful math methods
print(pow(2, 3))
print(math.sqrt(144))

#U S E R I N P U T
name = input("Enter your name: ")
print("Hello", name + "!")
num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)

# L I S T S
lucky_numbers = [4, 8, "fifteen", 16,23, 42.0]
# indexes       0 , 1   2       3     4  5

lucky_numbers[0] = 90
print(lucky)numbers[0])
print(lucky)numbers[1])
print(lucky)numbers[2])
print(lucky)numbers[-1])
print(lucky)numbers[2:])
print(lucky)numbers[2:4])
print(len(lucky_numbers))

# N Dimentional Lists
numberGrid = [[1,2], [3,4]]
numberGrid[0][1] = 99
print(numberGrid[0][0])
print(numberGrid[0][1])

# L I S T   Function
friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1,"Kevin")

#friends.remove("kevin")

print(friends)
print(friends.index("Oscar"))
print(friends.count("Angela"))
friends.sort()
print(friends)
friends.clear()
print(friends)

# Tuples
lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
# indexes        0  1   2          4   5    6


def add_numbers(num1, num2=99):
    return num1 + num2

sum = add_numbers(4,3)
print(sum)

# IF Statements
is_student = False
is_smart = False

if is_student and is_smart:
    print("you are a student")
elif is_student and not(Is_smart):
    print("You are not a student and not smart")
else:
    print("Your are not a student and not smart")

# For loop

for index in range(5):
    print(index)

for index in range(2323424):
    print(index)

lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_nums)

lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_nums)

for letter in "Giraffe":
    print(letter)

for letter in "giraffe":
    print(letter)

#Exception catching
answer = 10 / int(input("Entering Number: "))

answer = 1234 / int(input("Enter Number: "))

try: 
    answer = 10 / int(input("Enter Number: "))
except:
    print("Error")

try:
    answer = 1923 / int(input("Enter Number: "))
except: 
    print("error")

try:
    answer = 10 / int(input("Enter Number: "))
except:
    print("Error")

try:
    answer = 10 /int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any expression") # Big no-no

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
    
    def read_book(self):
        print("Reading", self.title, "by", self.author)

book1 = Book("Howf owo", "JK Rowling")

book1.title = "haff-Blood Prince"

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
        print("Reading", self.title, "by",self.author)

book1 = Book("Harry Potter", "JK Rowling")
#book1.title = "Half-Blood prince"

print(book1.title)
book1.read_book()

#inheritance

class Chef:
    def make_chicken(self):
        print("The chef makes chicken")
    
    def make_salad(self):
        print("The chef makes salad")
    
    def make_special_dish(self):
        print("The chef makes bbq ribs")


class ItalianChef(Chef):
    def make_pasta(self):
        print("The chef makes pasta")

    def make_special_dish(self):
        print("The chef makes chicken parm")


myChef = Chef
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
        print("The Chef makes salad")
    
    def make_special_dish(self):
        print("The chef makes bbq ribs")

class ItalianChef(Chef):
    def __init__(self,name, age, country_of_origin):
        self.country_of_origin = country_of_origin
        super(). __init__(name, age)

    def make_pasta(self):
        print("The make chicken parm")

myChef = Chef("Gordon Ramsay", 50)
myChef.make_chicken()

myItalianChef = ItalianChef("Massimo Bottura", 55, "Italy")
myItalianChef.make_chicken()
print(myItalianChef.age)