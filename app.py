# =============================================
# DocumentRider — OOP, Encapsulation & Magic Methods
# Author: Saleh Torkashvand
# =============================================

# A fully encapsulated class that counts words case-insensitively.
# Behaves like a Python dictionary, supports iteration, deletion, equality,
# and safely hides internal state using name mangling and property methods.

class DocumentRider:
    def __init__(self):
        # Private attribute (encapsulated data)
        self.__words = {}

    # Public method to add words
    def add(self, word):
        """Increment the count of a word (case-insensitive)."""
        word_lower = word.lower()
        self.__words[word_lower] = self.__words.get(word_lower, 0) + 1

    # Dictionary-like retrieval
    def __getitem__(self, word):
        return self.__words.get(word.lower(), 0)

    # Dictionary-like assignment
    def __setitem__(self, word, count):
        self.__words[word.lower()] = count

    # Delete a word
    def __delitem__(self, word):
        if word.lower() in self.__words:
            del self.__words[word.lower()]

    # Length of unique words
    def __len__(self):
        return len(self.__words)

    # Iteration over words
    def __iter__(self):
        return iter(self.__words)

    # Check if a word exists
    def __contains__(self, word):
        return word.lower() in self.__words

    # Custom string representation
    def __str__(self):
        return str(self.__words)

    # Equality check between documents
    def __eq__(self, other):
        if not isinstance(other, DocumentRider):
            return False
        return self.__words == other.__words

    # Total word count
    def total_words(self):
        return sum(self.__words.values())

    # 🧩 Property getter for safe external read access
    @property
    def words(self):
        """Return a read-only copy of all words."""
        return dict(self.__words)

    # 🧩 Optional setter (for controlled replacement)
    @words.setter
    def words(self, new_dict):
        """Safely replace the entire internal dictionary."""
        if isinstance(new_dict, dict):
            # normalize all keys to lowercase
            self.__words = {k.lower(): v for k, v in new_dict.items()}
        else:
            raise TypeError("words must be a dictionary")


# ---------------------------
# ✅ Usage Examples
# ---------------------------

document = DocumentRider()

# Add words (case-insensitive)
document.add("Python")
document.add("python")
document.add("PYTHON")
document.add("Java")
document.add("C++")

print("Document:", document)
# Output: Document: {'python': 3, 'java': 1, 'c++': 1}

# Accessing via __getitem__
print("Python count:", document["Python"])
# Output: 3

# Modifying count via __setitem__
document["Python"] = 50
print("Updated Python count:", document["python"])
# Output: 50

# Deleting a word
del document["c++"]
print("After deleting C++:", document)
# Output: {'python': 50, 'java': 1}

# Membership test
print("'java' in document?", "java" in document)
# Output: True
print("'c++' in document?", "c++" in document)
# Output: False

# Iteration
print("Iterating over words:")
for word in document:
    print(word, "->", document[word])
# Output:
# python -> 50
# java -> 1

# Length & total count
print("Unique words:", len(document))
# Output: 2
print("Total words:", document.total_words())
# Output: 51

# Comparison with another document
doc2 = DocumentRider()
doc2.words = {"python": 50, "java": 1}
print("Documents equal?", document == doc2)
# Output: True

# Reading internal words safely via property
print("All words:", document.words)
# Output: {'python': 50, 'java': 1}

# Replacing safely
document.words = {"Go": 5, "Rust": 3}
print("Replaced dictionary:", document.words)
# Output: {'go': 5, 'rust': 3}
