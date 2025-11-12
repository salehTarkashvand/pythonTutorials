# =============================================================
# 🧠 Advanced Example: Abstract Base Class and Stream Handling
# Author: Saleh Torkashvand
# =============================================================

from abc import ABC, abstractmethod

# -------------------- Custom Exception --------------------
class InvalidOperationError(Exception):
    """Custom error raised when an invalid stream operation occurs."""
    pass


# -------------------- Abstract Base Class --------------------
class Stream(ABC):
    """Abstract base class for different types of data streams."""

    def __init__(self):
        self.opened = False

    def open(self):
        """Open the stream if not already open."""
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True
        print("✅ Stream opened successfully.")

    def close(self):
        """Close the stream if it's currently open."""
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False
        print("✅ Stream closed successfully.")

    @abstractmethod
    def read(self):
        """Abstract method — must be implemented by subclasses."""
        pass


# -------------------- Concrete Implementations --------------------
class FileStream(Stream):
    """Handles reading data from a file."""
    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot read — stream is not open.")
        print("📂 Reading data from file stream...")


class NetworkStream(Stream):
    """Handles reading data from a network connection."""
    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot read — stream is not open.")
        print("🌐 Reading data from network stream...")


class MemoryStream(Stream):
    """Example of an unimplemented subclass — inherits abstract method."""
    def read(self):
        if not self.opened:
            raise InvalidOperationError("Cannot read — stream is not open.")
        print("💾 Reading data from memory stream...")


# =============================================================
# ✅ Example Usage
# =============================================================

try:
    file_stream = FileStream()
    file_stream.open()
    file_stream.read()
    file_stream.close()

    print("\n---\n")

    network_stream = NetworkStream()
    network_stream.open()
    network_stream.read()
    network_stream.close()

    print("\n---\n")

    memory_stream = MemoryStream()
    memory_stream.open()
    memory_stream.read()
    memory_stream.close()

except InvalidOperationError as e:
    print(f"❌ Error: {e}")
except TypeError as e:
    print(f"❌ Abstract class error: {e}")

