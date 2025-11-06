# Demonstration of Python dictionaries (dict) and their common operations

# --- Creating dictionaries ---
point = {"x": 1, "y": 2}  # Using curly braces
print("Original dictionary:", point)  # {'x': 1, 'y': 2}

# You can also use the dict() constructor
point = dict(x=1, y=2)
print("Created using dict():", point)  # {'x': 1, 'y': 2}

# --- Updating values ---
point["x"] = 10
point["y"] = 20
print("\nUpdated values:")
print("x:", point["x"])  # 10
print("y:", point["y"])  # 20

# --- Accessing values safely with get() ---
print("\nUsing get() method:")
print("x value:", point.get("x"))  # 10
print("z value (not found):", point.get("z", 0))  # 0

# --- Deleting keys ---
del point["x"]
print("\nAfter deleting 'x':", point)  # {'y': 20}

# --- Iterating through dictionary ---
print("\nIterating keys:")
for key in point:
    print(key)
# y

print("\nIterating keys and values manually:")
for key in point:
    print(key, point[key])
# y 20

print("\nIterating items() as tuples:")
for item in point.items():
    print(item)
# ('y', 20)

print("\nIterating items() with unpacking:")
for key, value in point.items():
    print(f"Key: {key}, Value: {value}")
# Key: y, Value: 20

# --- Adding new keys dynamically ---
point["z"] = 30
print("\nAfter adding new key 'z':", point)  # {'y': 20, 'z': 30}

# --- Check if a key exists ---
print("\nIs 'y' in point?", "y" in point)      # True
print("Is 'x' not in point?", "x" not in point)  # True

# --- Copying a dictionary ---
copy_point = point.copy()
print("\nCopied dictionary:", copy_point)  # {'y': 20, 'z': 30}

# --- Removing all items ---
copy_point.clear()
print("After clearing:", copy_point)  # {}

# --- Nested dictionaries ---
person = {
    "name": "Saleh",
    "age": 25,
    "skills": {"frontend": "React", "backend": "Node.js"}
}
print("\nNested dictionary example:")
print("Frontend skill:", person["skills"]["frontend"])  # React

# --- Merging two dictionaries ---
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = {**a, **b}  # Merge using unpacking (b overwrites y)
print("\nMerged dictionary:", merged)  # {'x': 1, 'y': 3, 'z': 4}

# --- Using dict comprehension ---
squared = {n: n**2 for n in range(1, 6)}
print("\nDictionary comprehension:", squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# --- Real-world example: counting word frequency ---
sentence = "hello world hello python world"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequency counter:", word_count)
# {'hello': 2, 'world': 2, 'python': 1}
