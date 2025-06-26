class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#second
class A:
  def __init__(self, name , id):
    self.name = name
    self.id = id

  def display(self):
      print(self.name , self. id)

    
class B(A):
  def __init__(self, name, id,salary , post):
    #super().__init__(name ,id)
    self.post= post
    self.salary = salary
obj= B("aa", 2 , 2000, "high")
print(obj.name, obj.id, obj.salary, obj.post)

   

 