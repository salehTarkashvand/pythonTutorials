# =============================================================
# 📘 Advanced Example: DocumentRider with Getter, Setter & Deleter
# Author: Saleh Torkashvand
# =============================================================

# 🧠 Description:
# This class demonstrates how to use Python's @property, @setter, and @deleter
# to manage a private dictionary safely.
# It includes validation, error handling, and common dictionary-like operations.

class DocumentRider:
    def __init__(self):
        """Initialize with an empty private dictionary."""
        self.__words = {}

    # -------------------- Getter --------------------
    @property
    def words(self):
        """✅ Getter: Returns the internal dictionary of words."""
        return self.__words

    # -------------------- Setter --------------------
    @words.setter
    def words(self, value):
        """✅ Setter: Validates and updates the internal dictionary safely."""
        if not isinstance(value, dict):
            raise TypeError("❌ value must be a dictionary")

        if not all(isinstance(k, str) for k in value.keys()):
            raise ValueError("❌ all keys must be strings")

        if not all(isinstance(v, (int, float)) for v in value.values()):
            raise ValueError("❌ all values must be numeric (int or float)")

        self.__words = value

    # -------------------- Deleter --------------------
    @words.deleter
    def words(self):
        """✅ Deleter: Clears all words in the document."""
        print("⚠️ Deleting all words from the document...")
        self.__words.clear()

    # -------------------- Magic methods --------------------
    def __str__(self):
        """Pretty print when printing the object."""
        return f"DocumentRider(words={self.__words})"

    def __len__(self):
        """Return number of unique words."""
        return len(self.__words)

    def total_count(self):
        """Return total count of all words."""
        return sum(self.__words.values())

    def __delitem__(self, key):
        """Support `del document['word']` syntax."""
        key_lower = key.lower()
        if key_lower in self.__words:
            print(f"🗑️ Deleted word: '{key_lower}'")
            del self.__words[key_lower]
        else:
            print(f"⚠️ Word '{key_lower}' not found in document.")

    def __contains__(self, key):
        """Support 'in' keyword."""
        return key.lower() in self.__words


# =============================================================
# ✅ Example Usage
# =============================================================

document = DocumentRider()

# 1️⃣ Set valid dictionary
document.words = {"python": 5, "AI": 3, "machine": 7}
print("✅ document.words =", document.words)
# Output: {'python': 5, 'AI': 3, 'machine': 7}

# 2️⃣ Print object
print("🖨️ Document:", document)
# Output: DocumentRider(words={'python': 5, 'AI': 3, 'machine': 7})

# 3️⃣ Length & total
print("📏 Unique words:", len(document))       # 3
print("🔢 Total word count:", document.total_count())  # 15

# 4️⃣ Delete a single key using delitem
del document["AI"]  
# Output: 🗑️ Deleted word: 'ai'

print("✅ After deleting 'AI':", document.words)
# Output: {'python': 5, 'machine': 7}

# 5️⃣ Try deleting non-existing key
del document["java"]
# Output: ⚠️ Word 'java' not found in document.

# 6️⃣ Check if word exists
print("'python' in document?", "python" in document)  # True
print("'AI' in document?", "AI" in document)          # False

# 7️⃣ Delete all words using @deleter
del document.words
# Output: ⚠️ Deleting all words from the document...

print("✅ After deleting all words:", document.words)
# Output: {}

# 8️⃣ Try setting invalid data types
try:
    document.words = 123
except Exception as e:
    print("❌ Error:", e)

try:
    document.words = {"python": "ten"}  # invalid value type
except Exception as e:
    print("❌ Error:", e)

try:
    document.words = {10: 100}  # invalid key type
except Exception as e:
    print("❌ Error:", e)
