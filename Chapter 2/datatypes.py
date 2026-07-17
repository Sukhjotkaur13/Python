# ==========================================================
#                  PYTHON DATA TYPES
# ==========================================================

# ----------------------------------------------------------
# What are Data Types?
# ----------------------------------------------------------

# Data Type specifies the type of data that a variable can store.

# In Python, every value belongs to a specific data type.

# Python is a Dynamically Typed Language.
# This means we do not need to declare the data type of a variable.
# Python automatically identifies the data type according to the assigned value.

# Example

a = 10
b = 10.5
c = "Python"
d = True

print(a)
print(b)
print(c)
print(d)

# ----------------------------------------------------------
# Common Built-in Data Types
# ----------------------------------------------------------

# 1. int
# 2. float
# 3. str
# 4. bool
# 5. complex

# There are many other data types in Python such as
# list, tuple, set and dictionary which we will study later.

# ==========================================================
# INTEGER DATA TYPE (int)
# ==========================================================

# Integer stores whole numbers.
# It can be positive, negative or zero.

age = 20
marks = 95
temperature = -5

print(age)
print(marks)
print(temperature)

# ==========================================================
# FLOAT DATA TYPE (float)
# ==========================================================

# Float stores decimal numbers.

percentage = 89.75
price = 250.50

print(percentage)
print(price)

# ==========================================================
# STRING DATA TYPE (str)
# ==========================================================

# String is a collection of characters enclosed within
# single quotes (' ')
# double quotes (" ")
# or triple quotes (''' ''' or """ """)

name = "Rahul"
city = 'Delhi'

message = """Welcome
to
Python"""

print(name)
print(city)
print(message)

# ==========================================================
# BOOLEAN DATA TYPE (bool)
# ==========================================================

# Boolean stores only two values.

# True
# False

is_pass = True
is_admin = False

print(is_pass)
print(is_admin)

# ==========================================================
# COMPLEX DATA TYPE (complex)
# ==========================================================

# Complex numbers contain a real part and an imaginary part.

number = 5 + 3j

print(number)

# ==========================================================
# type() Function
# ==========================================================

# type() is an inbuilt function.

# It is used to check the data type of a variable.

a = 100
b = 10.5
c = "Python"
d = True
e = 5 + 6j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Output
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'complex'>

# ==========================================================
# Checking the Type of Literal Values
# A literal is a fixed value that is written directly in the program.
# ==========================================================

print(type(100))
print(type(25.5))
print(type("Hello"))
print(type(False))

# ==========================================================
# id() Function
# ==========================================================

# id() is an inbuilt function.

# It returns the memory identity (unique identification)
# of an object.

# Note:
# Beginners usually call it "memory address".
# Technically, id() returns the object's identity.
# In CPython, this often corresponds to the memory address.

a = 10

print(id(a))

b = "Python"

print(id(b))

# ==========================================================
# Same Object Example
# ==========================================================

x = 100
y = 100

print(id(x))
print(id(y))

# In many Python implementations,
# both variables may have the same id
# because Python can reuse immutable objects.

# ==========================================================
# Different Object Example
# ==========================================================

name1 = "Python"
name2 = "Java"

print(id(name1))
print(id(name2))

# ==========================================================
# Memory Size
# ==========================================================

# Python provides the sys module
# to calculate the memory occupied by an object.

import sys

a = 10

print(sys.getsizeof(a))

# getsizeof() returns the size in Bytes.

# Example

print(sys.getsizeof(100))
print(sys.getsizeof(25.5))
print(sys.getsizeof("Python"))
print(sys.getsizeof(True))

# Note:
# The returned size depends on the Python version
# and the operating system.

# ==========================================================
# Checking Everything Together
# ==========================================================

number = 50

print("Value :", number)
print("Data Type :", type(number))
print("Object ID :", id(number))
print("Memory Size :", sys.getsizeof(number), "Bytes")

# ==========================================================
# Dynamic Typing
# ==========================================================

# A variable can store different data types at different times.

data = 10

print(data)
print(type(data))

data = "Python"

print(data)
print(type(data))

data = 50.25

print(data)
print(type(data))

# Python automatically changes the data type.

# ==========================================================
# Important Points
# ==========================================================

# 1. Every value has a data type.
# 2. Python automatically assigns data types.
# 3. type() checks the data type.
# 4. id() returns the object identity.
# 5. sys.getsizeof() returns memory occupied by the object.
# 6. Python is dynamically typed.

# ==========================================================
# Practice Programs
# ==========================================================

# Q1
# Create one variable of each data type.

# Q2
# Print their values.

# Q3
# Print their data types.

# Q4
# Print their object IDs.

# Q5
# Print their memory sizes.

# ==========================================================
# Sample Program
# ==========================================================

import sys

name = "Sukhjot"
age = 22
percentage = 89.5
is_student = True

print(name)
print(type(name))
print(id(name))
print(sys.getsizeof(name))

print(age)
print(type(age))
print(id(age))
print(sys.getsizeof(age))

print(percentage)
print(type(percentage))
print(id(percentage))
print(sys.getsizeof(percentage))

print(is_student)
print(type(is_student))
print(id(is_student))
print(sys.getsizeof(is_student))

# ==========================================================
# End of Data Types
# ==========================================================