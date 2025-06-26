
class shape:
    def area(self):
        return "notdefined"

class Rectangle(shape):
    def __init__(self , length ,width):
        self.length= length
        self.width= width

    def area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self , radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
shapes = [Rectangle(2 ,3) , circle(4)]
for shape in shapes:
    print(f"Area: {shape.area()}")
# overriding

class Animal:
    def sound(self):
        return "some generic sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow" 

animals = [Animal() , Dog(), Cat()]
for Animal in animals:
    print(Animal.sound())
