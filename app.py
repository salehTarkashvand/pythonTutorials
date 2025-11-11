# =============================================
# Python Classes and Objects — Full Example
# Author: Saleh Torkashvand
# =============================================

# A simple class definition in Python

class Point:
    # A class method (function inside a class)
    # All instance methods must take 'self' as the first parameter
    # 'self' refers to the current object (instance) created from this class
    def draw(self):
        print("Drawing a point...")  # Output when draw() is called

# ------------------------------------------------------------
# ✅ Creating an instance (object) of the Point class
# ------------------------------------------------------------
point = Point()  # Creating an object named 'point'

# ------------------------------------------------------------
# ✅ Checking the type of the object
# ------------------------------------------------------------
print(isinstance(point, Point))  # True → because 'point' is an instance of class Point

# ------------------------------------------------------------
# ✅ Calling a method using the object
# ------------------------------------------------------------
point.draw()  # Output: Drawing a point...

# ------------------------------------------------------------
# ✅ Adding attributes to an object dynamically
# ------------------------------------------------------------
point.x = 10
point.y = 20
print("Point coordinates:", point.x, point.y)  # Output: Point coordinates: 10 20

# ------------------------------------------------------------
# ✅ Creating another object of the same class
# ------------------------------------------------------------
another_point = Point()
another_point.x = 5
another_point.y = 7
another_point.draw()  # Output: Drawing a point...

print(isinstance(another_point, Point))  # True

# ------------------------------------------------------------
# ✅ Example: Define a constructor (__init__)
# ------------------------------------------------------------
class Circle:
    # The __init__ method automatically runs when you create a new object
    def __init__(self, radius):
        self.radius = radius  # Assign value to the object’s property
        print(f"Circle created with radius = {self.radius}")

    def area(self):
        return 3.14 * (self.radius ** 2)

# Create two circles
circle1 = Circle(5)  # Output: Circle created with radius = 5
circle2 = Circle(10) # Output: Circle created with radius = 10

# Calculate and print their areas
print("Circle 1 area:", circle1.area())  # Output: 78.5
print("Circle 2 area:", circle2.area())  # Output: 314.0

# ------------------------------------------------------------
# ✅ isinstance() and type() differences
# ------------------------------------------------------------
print(isinstance(circle1, Circle))  # True → circle1 is an instance of Circle
print(type(circle1))                # <class '__main__.Circle'>

# ------------------------------------------------------------
# ✅ Example: Checking instance type against multiple classes
# ------------------------------------------------------------
print(isinstance(circle1, (Circle, Point)))  # True → circle1 is a Circle, so it's True
print(isinstance(point, (Circle, Point)))    # True → point is a Point

# ------------------------------------------------------------
# ✅ Example: isinstance() vs issubclass()
# ------------------------------------------------------------
class Shape:
    pass

class Rectangle(Shape):
    pass

rect = Rectangle()
print(isinstance(rect, Rectangle))  # True
print(isinstance(rect, Shape))      # True → because Rectangle inherits Shape
print(issubclass(Rectangle, Shape)) # True → Rectangle is a subclass of Shape
print(issubclass(Point, Shape))     # False → no inheritance relation
