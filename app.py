# ============================================================
# 🐍 Advanced Example: Inheritance and super() in Python
# Author: Saleh Torkashvand
# ============================================================

# ✅ Base class: Animal
class Animal:
    def __init__(self, name):
        # Common attribute for all animals
        self.name = name
        print(f"🐾 Animal initialized with name: {self.name}")

    def eat(self):
        print(f"{self.name} is eating 🍽️")


# ✅ Derived class 1: Mammal (inherits from Animal)
class Mammal(Animal):
    def __init__(self, name, sound):
        # Use super() to call the parent class constructor
        super().__init__(name)
        self.sound = sound
        print(f"🦴 Mammal initialized with sound: {self.sound}")

    def walk(self):
        print(f"{self.name} is walking 🐾")

    def make_sound(self):
        print(f"{self.name} says '{self.sound}' 🐶")


# ✅ Derived class 2: Bird (inherits from Animal)
class Bird(Animal):
    def __init__(self, name, age):
        # Call parent constructor to set the 'name'
        super().__init__(name)
        self.age = age
        print(f"🕊️ Bird initialized with age: {self.age}")

    def fly(self):
        print(f"{self.name} is flying 🪶")

    def info(self):
        print(f"{self.name} is {self.age} years old 🧓")


# ============================================================
# ✅ Create objects
# ============================================================

mammal = Mammal("Ashly", "Woof")
bird = Bird("Henry", 3)

print("\n--------------------")
# ✅ Check inheritance relationships
print("isinstance(bird, Animal)?", isinstance(bird, Animal))  # True
print("isinstance(mammal, Bird)?", isinstance(mammal, Bird))  # False
print("issubclass(Bird, Animal)?", issubclass(Bird, Animal))  # True
print("issubclass(Mammal, Animal)?", issubclass(Mammal, Animal))  # True
print("issubclass(Bird, object)?", issubclass(Bird, object))  # True

print("\n--------------------")
# ✅ Use methods from parent and child classes
mammal.eat()       # From Animal
mammal.walk()      # From Mammal
mammal.make_sound()

bird.eat()         # From Animal
bird.fly()         # From Bird
bird.info()

print("\n--------------------")
# ✅ Show MRO (Method Resolution Order)
print("Bird MRO:", [cls.__name__ for cls in Bird.__mro__])
print("Mammal MRO:", [cls.__name__ for cls in Mammal.__mro__])
