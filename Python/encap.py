class public:
    def __init__(self):
        self.name="Aakanksha" # public attribute

    def display_name(self):
        print(self.name)

obj= public()
obj.display_name()
print(obj.name)

#second
class protected:
    def __init__(self):
        self._age=25  #protected attribute

class subclass(protected):
    def display_age(self):
        print(self._age)

obj =subclass()
obj.display_age()

#third private
class private:
    def __init__(self):
        self.__salary = 50000 # private attribute

    def salary(self):
        return self.__salary # access  through public method
    
obj = private()
print(obj.salary())
#print(obj.__salary)