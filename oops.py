class Car:
    def __init__(self, name, model):
        self.name=name
        self. model = model

obj = Car("mercidies", "new123")
print(obj.name)
print(obj.model)        

#second
class me:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}{self.age}"
obj=me("aakanksha", 15)
print(obj)

#third
class Parent:
    def __init__(aakanksha):
        aakanksha.parent_attr= "parent attribute"

    def show(aakanksha):
        print(aakanksha.parent_attr)

class Child:
    def __init__(Parent):
        super().__init__() #inhert parent attribute
        self.child_attr = "child attribute"

    def display(self):
        self.show() #Access parent attribute
        print(self.child_attr)

obj = Child()
obj.display()           

          