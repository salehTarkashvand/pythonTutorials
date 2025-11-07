# --------------------------------------------------------------
# Generators in Python — Full Examples and Explanations
# --------------------------------------------------------------
# A generator expression creates a generator iterator that
# produces values on-the-fly (lazy evaluation). It does NOT
# store all values in memory like a list comprehension does.
#
# Note: Output values and memory sizes may vary by Python
# implementation and system. Here we show expected/example outputs.
from sys import getsizeof
from itertools import islice

# Create a generator expression that yields x*2 for x in range(100)
values = (x * 2 for x in range(100))

# The generator itself is an iterator — printing it shows a generator object
print("Generator object:", values)
# Example output: Generator object: <generator object <genexpr> at 0x7f9b3c4d1e40>

# Iterating over generator — it produces items one by one
print("\nIterating over generator (first 10 shown):")
for i, x in enumerate(values):
    print(x, end=" ")
    if i >= 9:  # stop after 10 items for brevity
        break
# Example printed values: 0 2 4 6 8 10 12 14 16 18

# Note: after the above loop, 'values' is NOT exhausted yet — we stopped early.
# Let's consume the rest (demonstration). For clarity we'll create a fresh generator below.

# Create a fresh generator for full iteration demonstration
values = (x * 2 for x in range(100))

print("\nFull iteration (prints first 20 and last 2 for brevity):")
# print first 20 values
for x in islice(values, 20):
    print(x, end=" ")
# Example: 0 2 4 ... 38

# Continue iterating to the end and capture the last two produced values
# (since generator continues from where we left off)
last_two = list(islice(values, 98))  # consume remaining into a list for inspection
# last_two will contain the rest; show last two elements:
if last_two:
    print("\n... last two of generator:", last_two[-2], last_two[-1])
# Example: ... last two of generator: 196 198

# After consuming all elements, generator is exhausted
print("\nAfter full consumption, trying to iterate again yields nothing:")
for x in values:
    print(x)  # no output, because generator is exhausted

# Demonstrate StopIteration with next()
values = (x * 2 for x in range(3))  # small generator: yields 0,2,4
print("\nUsing next():")
print(next(values))  # 0
print(next(values))  # 2
print(next(values))  # 4
# print(next(values))  # would raise StopIteration

# Memory size: generator object is usually small because it doesn't store all items.
values = (x * 2 for x in range(100))
print("\nMemory size of generator object (bytes):", getsizeof(values))
# Example: Memory size of generator object (bytes): 112
# (Note: actual number depends on Python version and platform.)

# For comparison, creating a list with the same elements stores them in memory:
values_list = [x * 2 for x in range(100)]
print("Memory size of list of 100 ints (bytes):", getsizeof(values_list))
# Example: Memory size of list of 100 ints (bytes): 872
# Important: getsizeof(list) returns only the container size, not
# the total size of the referenced integer objects. For deep memory
# profiling use pympler.asizeof or similar tools.

# Reuse note: generators are single-use. To "reuse" create a new generator:
values1 = (x * 2 for x in range(5))
print("\nFirst pass over values1:")
print(list(values1))  # [0, 2, 4, 6, 8]
values1 = (x * 2 for x in range(5))  # recreate
print("Second pass after recreating:")
print(list(values1))  # [0, 2, 4, 6, 8]

# Converting generator to list to store all results:
values = (x * 2 for x in range(10))
stored = list(values)  # now all values are in memory and reusable
print("\nConverted to list (stored):", stored)
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Generator function (same behavior but with explicit yield)
def gen_numbers(n):
    for i in range(n):
        yield i * 2

g = gen_numbers(5)
print("\nGenerator from function (using yield):", list(g))  # [0,2,4,6,8]

# Lazy pipelines: generators compose well for memory-efficient pipelines
def even_numbers(n):
    for i in range(n):
        if (i * 2) % 4 == 0:
            yield i * 2

pipeline = (x for x in even_numbers(20))
print("\nPipeline example (first 5):", list(islice(pipeline, 5)))
# Example output: [0, 4, 8, 12, 16]

# --------------------------------------------------------------
# Key takeaways (printed as comments for clarity):
# 1) Generators evaluate lazily and are memory-efficient for large sequences.
# 2) They are iterators and get exhausted after use (single-pass).
# 3) Use list(...) to materialize results if you need random access or multiple passes.
# 4) getsizeof shows generator object's memory footprint, not full dataset footprint.
# 5) For deep memory measurement, use specialized profilers.
# --------------------------------------------------------------
