# =============================================
# Advanced DocumentRider Class with Magic Methods
# Author: Saleh Torkashvand
# =============================================

# A powerful word counter class that behaves like a dictionary
# Supports addition, removal, iteration, length, comparison, and more

class DocumentRider:
    def __init__(self):
        # Dictionary to store word counts (case-insensitive)
        self.words = {}

    # Add a word to the counter
    def add(self, word):
        """Increment the count of a word (case-insensitive)."""
        word_lower = word.lower()
        self.words[word_lower] = self.words.get(word_lower, 0) + 1

    # Dictionary-like retrieval
    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)

    # Dictionary-like assignment
    def __setitem__(self, word, count):
        self.words[word.lower()] = count

    # Delete a word
    def __delitem__(self, word):
        if word.lower() in self.words:
            del self.words[word.lower()]

    # Length of unique words
    def __len__(self):
        return len(self.words)

    # Iteration over words
    def __iter__(self):
        return iter(self.words)

    # Check if word exists
    def __contains__(self, word):
        return word.lower() in self.words

    # String representation
    def __str__(self):
        return str(self.words)

    # Comparison between two documents (based on total counts)
    def __eq__(self, other):
        if not isinstance(other, DocumentRider):
            return False
        return self.words == other.words

    # Sum total words
    def total_words(self):
        return sum(self.words.values())


# ---------------------------
# ✅ Usage Examples
# ---------------------------

document = DocumentRider()

# Add words
document.add("Python")
document.add("python")
document.add("PYTHON")
document.add("Java")
document.add("Java")
document.add("C++")

# Print dictionary-like object
print("Document:", document)
# Output: Document: {'python': 3, 'java': 2, 'c++': 1}

# Access using __getitem__
print("Python count:", document["Python"])  
# Output: Python count: 3

# Modify using __setitem__
document["Python"] = 50
print("Updated Python count:", document["python"])  
# Output: Updated Python count: 50

# Delete a word
del document["c++"]
print("After deleting C++:", document)
# Output: After deleting C++: {'python': 50, 'java': 2}

# Check if word exists
print("'java' in document?", "java" in document)  
# Output: 'java' in document? True
print("'c++' in document?", "c++" in document)  
# Output: 'c++' in document? False

# Iterate over words
print("\nIterating words:")
for word in document:
    print(word, "->", document[word])
# Output:
# python -> 50
# java -> 2

# Length and total words
print("\nNumber of unique words:", len(document))  
# Output: Number of unique words: 2
print("Total words count:", document.total_words())  
# Output: Total words count: 52

# Comparison with another document
doc2 = DocumentRider()
doc2["python"] = 50
doc2["java"] = 2
print("\nDocuments equal?", document == doc2)  
# Output: Documents equal? True

# Example of a new document
doc3 = DocumentRider()
doc3["python"] = 10
print("Documents equal?", document == doc3)  
# Output: Documents equal? False
