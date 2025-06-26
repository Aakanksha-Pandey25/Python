
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract class inheriting from ABC
    @abstractmethod
    def calculate_area(self):
        pass # Abstract method with no implementation

    @abstractmethod
    def calculate_perimeter(self):
        pass # Another abstract method

    def get_description(self): # Concrete method
        return "This is a geometric shape."

class Circle(Shape): # Concrete subclass
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# shape = Shape() # This would raise a TypeError (cannot instantiate abstract class)

circle = Circle(5)
print(f"Area of circle: {circle.calculate_area()}")
print(f"Perimeter of circle: {circle.calculate_perimeter()}")
print(circle.get_description())
        
