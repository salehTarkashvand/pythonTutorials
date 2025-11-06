# Demonstration of Python Set operations and methods

# --- Creating sets ---
numbers = [1, 1, 2, 2, 3, 4]
first = set(numbers)  # Removes duplicates from list
second = {1, 2, 5}

print("First set:", first)    # {1, 2, 3, 4}
print("Second set:", second)  # {1, 2, 5}

# --- Basic set operations using operators ---

# Union ( | ): all unique elements from both sets
print("Union (|):", first | second)  # {1, 2, 3, 4, 5}

# Intersection ( & ): elements present in both sets
print("Intersection (&):", first & second)  # {1, 2}

# Difference ( - ): elements in first but not in second
print("Difference (-):", first - second)  # {3, 4}

# Symmetric Difference ( ^ ): elements in one set or the other, but not both
print("Symmetric Difference (^):", first ^ second)  # {3, 4, 5}

# --- Equivalent method calls ---
print("\nEquivalent method calls:")
print("Union:", first.union(second))
print("Intersection:", first.intersection(second))
print("Difference:", first.difference(second))
print("Symmetric Difference:", first.symmetric_difference(second))

# --- Adding and removing elements ---
first.add(6)  # Adds new element
print("\nAfter adding 6:", first)

first.remove(1)  # Removes element (raises error if not found)
print("After removing 1:", first)

first.discard(10)  # Removes safely (no error if not found)
print("After discard(10):", first)

# --- Membership test ---
print("\nIs 3 in first?", 3 in first)  # True
print("Is 7 not in first?", 7 not in first)  # True

# --- Copying a set ---
copied_set = first.copy()
print("\nCopied set:", copied_set)

# --- Clearing all elements ---
copied_set.clear()
print("After clearing copied set:", copied_set)  # set()

# --- Creating set from string (unique letters) ---
letters = set("banana")
print("\nUnique letters in 'banana':", letters)  # {'a', 'b', 'n'}

# --- Frozen sets (immutable sets) ---
frozen = frozenset({1, 2, 3})
print("\nFrozen set:", frozen)
# frozen.add(4)  # ❌ Error: frozenset is immutable
