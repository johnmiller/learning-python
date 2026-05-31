"""
Basic Python Cheat Sheet
Run: py basics.py

Use this file as a quick reference for common Python syntax.
"""

import math
import re


# -----------------------------
# 1) Variables and basic types
# -----------------------------
name = "Ada"
age = 30
height = 1.68
is_coding = True

print("\n--- Variables ---")  # -> --- Variables ---
print(name, age, height, is_coding)  # -> Ada 30 1.68 True
print(type(name), type(age), type(height), type(is_coding))  # -> <class 'str'> <class 'int'> <class 'float'> <class 'bool'>


# -----------------------------
# 2) Strings
# -----------------------------
print("\n--- Strings ---")  # -> --- Strings ---
greeting = f"Hello, {name}!"
print(greeting)  # -> Hello, Ada!
print(greeting.lower())  # -> hello, ada!
print(greeting.upper())  # -> HELLO, ADA!
print(greeting.replace("Ada", "Python Learner"))  # -> Hello, Python Learner!
print("Length:", len(greeting))  # -> Length: 11


# -----------------------------
# 3) Numbers and math
# -----------------------------
print("\n--- Numbers ---")  # -> --- Numbers ---
print("5 / 2  =", 5 / 2)   # float division -> 5 / 2  = 2.5
print("5 // 2 =", 5 // 2)  # integer division -> 5 // 2 = 2
print("5 % 2  =", 5 % 2)   # remainder -> 5 % 2  = 1
print("2 ** 3 =", 2 ** 3)  # power -> 2 ** 3 = 8
print("ceil(2.34) =", math.ceil(2.34))  # -> ceil(2.34) = 3
print("sqrt(16) =", math.sqrt(16))  # -> sqrt(16) = 4.0


# -----------------------------
# 4) Lists
# -----------------------------
print("\n--- Lists ---")  # -> --- Lists ---
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)  # -> ['apple', 'banana', 'orange', 'mango']
print("First:", fruits[0])  # -> First: apple
print("Slice [1:3]:", fruits[1:3])  # -> Slice [1:3]: ['banana', 'orange']


# -----------------------------
# 5) Tuples (immutable)
# -----------------------------
print("\n--- Tuples ---")  # -> --- Tuples ---
point = (10, 20)
print(point)  # -> (10, 20)


# -----------------------------
# 6) Sets (unique, unordered)
# -----------------------------
print("\n--- Sets ---")  # -> --- Sets ---
numbers = {1, 2, 2, 3, 4}
print("Unique values:", numbers)  # -> Unique values: {1, 2, 3, 4} (order may vary)
numbers.add(5)
numbers.remove(1)
print("After add/remove:", numbers)  # -> After add/remove: {2, 3, 4, 5} (order may vary)

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)  # -> Union: {1, 2, 3, 4, 5} (order may vary)
print("Intersection:", a & b)  # -> Intersection: {3}


# -----------------------------
# 7) Dictionaries
# -----------------------------
print("\n--- Dictionaries ---")  # -> --- Dictionaries ---
user = {"name": "Ada", "role": "Engineer", "active": True}
print(user)  # -> {'name': 'Ada', 'role': 'Engineer', 'active': True}
print("Name:", user["name"])  # -> Name: Ada
print("Role:", user.get("role"))  # -> Role: Engineer


# -----------------------------
# 8) Conditionals
# -----------------------------
print("\n--- Conditionals ---")  # -> --- Conditionals ---
score = 82
if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
else:
	grade = "C or below"
print("Grade:", grade)  # -> Grade: B


# -----------------------------
# 9) Loops
# -----------------------------
print("\n--- Loops ---")  # -> --- Loops ---
for fruit in fruits:
	print("for loop:", fruit)  # -> for loop: apple ... then banana/orange/mango

count = 0
while count < 3:
	print("while loop count:", count)  # -> 0, then 1, then 2
	count += 1


# -----------------------------
# 10) Functions
# -----------------------------
print("\n--- Functions ---")  # -> --- Functions ---


def add(a, b):
	return a + b


def greet(person="friend"):
	return f"Hi, {person}!"


print(add(2, 3))  # -> 5
print(greet())  # -> Hi, friend!
print(greet("Sam"))  # -> Hi, Sam!


# -----------------------------
# 11) List comprehensions
# -----------------------------
print("\n--- Comprehensions ---")  # -> --- Comprehensions ---
squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]
print("Squares:", squares)  # -> Squares: [0, 1, 4, 9, 16, 25]
print("Evens:", evens)  # -> Evens: [0, 2, 4, 6, 8]


# -----------------------------
# 12) Exceptions
# -----------------------------
print("\n--- Exceptions ---")  # -> --- Exceptions ---
try:
	result = 10 / 0
	print(result)  # -> (not reached in this example)
except ZeroDivisionError:
	print("Cannot divide by zero.")  # -> Cannot divide by zero.


# -----------------------------
# 13) Classes
# -----------------------------
print("\n--- Classes ---")  # -> --- Classes ---


class Dog:
	def __init__(self, name):
		self.name = name

	def bark(self):
		return f"{self.name} says woof!"


dog = Dog("Milo")
print(dog.bark())  # -> Milo says woof!


# -----------------------------
# 14) Useful built-ins
# -----------------------------
print("\n--- Built-ins ---")  # -> --- Built-ins ---
nums = [3, 1, 4, 1, 5]
print("min:", min(nums))  # -> min: 1
print("max:", max(nums))  # -> max: 5
print("sum:", sum(nums))  # -> sum: 14
print("sorted:", sorted(nums))  # -> sorted: [1, 1, 3, 4, 5]


# -----------------------------
# 15) Regular expressions (re)
# -----------------------------
print("\n--- Regular Expressions ---")  # -> --- Regular Expressions ---
text = "Contact: ada@example.com, backup: support@test.org"

# search: first match
email_match = re.search(r"[\w.-]+@[\w.-]+", text)
if email_match:
	print("First email:", email_match.group())  # -> First email: ada@example.com

# findall: all matches
all_emails = re.findall(r"[\w.-]+@[\w.-]+", text)
print("All emails:", all_emails)  # -> All emails: ['ada@example.com', 'support@test.org']

# sub: replace matches
masked = re.sub(r"[\w.-]+@[\w.-]+", "[hidden-email]", text)
print("Masked:", masked)  # -> Masked: Contact: [hidden-email], backup: [hidden-email]

# quick common patterns
print("\nCommon patterns:")  # -> Common patterns:
print(r"\d+  -> one or more digits")  # -> \d+  -> one or more digits
print(r"\s+  -> one or more whitespace chars")  # -> \s+  -> one or more whitespace chars
print(r"\bword\b -> whole word match")  # -> \bword\b -> whole word match

sample = "Order 123 ships in 5 days"
print("Digits in sample:", re.findall(r"\d+", sample))  # -> Digits in sample: ['123', '5']
print("Whole word 'ships'?:", bool(re.search(r"\bships\b", sample)))  # -> Whole word 'ships'?: True
