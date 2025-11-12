# =============================================================
# 🧬 Inheritance & OOP Example: Animal, Mammal, Bird Classes
# Author: Saleh Torkashvand
# =============================================================

# 🧠 Description:
# This example demonstrates the concept of INHERITANCE in Python OOP.
# - 'Animal' is a base (parent) class.
# - 'Mammal' and 'Bird' are derived (child) classes that inherit from Animal.
# - Child classes can use or extend parent class attributes and methods.
# - Built-in functions:
#     - isinstance(obj, Class): checks if object is an instance of a class (or its subclass)
#     - issubclass(ClassA, ClassB): checks if ClassA inherits from ClassB
# - All classes in Python implicitly inherit from the base class 'object'.

# =============================================================
# 🐾 Base Class
# =============================================================

class Animal:
    def __init__(self, value):
        """Initialize the animal with a name."""
        self.name = value

    def eat(self):
        """Prints a message indicating that the animal is eating."""
        print(f"{self.name} is eating 🍽️")


# =============================================================
# 🐕 Derived Class 1: Mammal
# =============================================================

class Mammal(Animal):
    def walk(self):
        """Mammals can walk."""
        print(f"{self.name} is walking 🐾")


# =============================================================
# 🕊️ Derived Class 2: Bird
# =============================================================

class Bird(Animal):
    def flying(self):
        """Birds can fly."""
        print(f"{self.name} is flying 🕊️")


# =============================================================
# ✅ Example Usage
# =============================================================

# Create instances
mammal = Mammal("Ashly")
bird = Bird("Henry")

# Base class method (inherited)
mammal.eat()   # Output: Ashly is eating 🍽️
bird.eat()     # Output: Henry is eating 🍽️

# Child class methods
mammal.walk()  # Output: Ashly is walking 🐾
bird.flying()  # Output: Henry is flying 🕊️

# -------------------------------------------------------------
# 🔍 Type Checking
# -------------------------------------------------------------
print("\nType Checking Results:")
print("1️⃣ isinstance(bird, Animal):", isinstance(bird, Animal))   # True
print("2️⃣ isinstance(mammal, Bird):", isinstance(mammal, Bird))   # False
print("3️⃣ issubclass(Bird, Animal):", issubclass(Bird, Animal))   # True
print("4️⃣ issubclass(Bird, object):", issubclass(Bird, object))   # True
print("5️⃣ issubclass(Mammal, Animal):", issubclass(Mammal, Animal)) # True

# -------------------------------------------------------------
# 🧩 Explanation:
# -------------------------------------------------------------
# ✅ isinstance(obj, Class)
#     → Returns True if 'obj' is an instance of 'Class' or its subclasses.
#
# ✅ issubclass(ClassA, ClassB)
#     → Returns True if 'ClassA' inherits from 'ClassB'.
#
# ✅ object
#     → The root of all Python classes. Every class is a subclass of 'object'.

# =============================================================
# 🧾 Expected Output
# =============================================================
# Ashly is eating 🍽️
# Henry is eating 🍽️
# Ashly is walking 🐾
# Henry is flying 🕊️
#
# Type Checking Results:
# 1️⃣ isinstance(bird, Animal): True
# 2️⃣ isinstance(mammal, Bird): False
# 3️⃣ issubclass(Bird, Animal): True
# 4️⃣ issubclass(Bird, object): True
# 5️⃣ issubclass(Mammal, Animal): True
