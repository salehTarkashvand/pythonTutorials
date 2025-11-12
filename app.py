from abc import ABC, abstractmethod

# -------------------- Abstract Base Class --------------------
class UiControl(ABC):
    """Abstract UI Control class defining a common interface."""
    @abstractmethod
    def read(self):
        pass

# -------------------- Concrete Classes --------------------
class TextBox(UiControl):
    def read(self):
        print("📝 Reading data from TextBox")

class DropDownList(UiControl):
    def read(self):
        print("⬇️ Reading data from DropDownList")

class Slider:
    """Example of duck typing: not inheriting from UiControl, but implements read()"""
    def read(self):
        print("🎚️ Reading value from Slider")

# -------------------- Polymorphic Function --------------------
def draw(controls):
    """Accepts any object with a read() method (Polymorphism & Duck Typing)"""
    for control in controls:
        control.read()

# -------------------- Example Usage --------------------
controls = [TextBox(), DropDownList(), Slider()]
draw(controls)
