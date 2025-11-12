from collections import namedtuple

# -------------------- Named Tuple Definition --------------------
# namedtuple creates an immutable class with named fields
# Here, we define a "point" class with fields "x" and "y"
Point = namedtuple("Point", ["x", "y"])

# -------------------- Instances --------------------
p1 = Point(x=1, y=3)
p2 = Point(x=1, y=3)

# -------------------- Comparison --------------------
# namedtuples support value-based comparison
print(p1 == p2)  # True because x and y values are the same

# -------------------- Accessing Fields --------------------
print("p1.x =", p1.x)  # Access by attribute name
print("p1.y =", p1.y)

# -------------------- Immutability --------------------
# p1.x = 10  # ❌ This would raise AttributeError because namedtuple is immutable
