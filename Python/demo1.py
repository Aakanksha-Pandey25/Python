
'''x,y=input("enter two variables:").split()
print("no of boys",x)
print("no of girls",y)'''
# function
'''a="i am globall"
def A():
    global a
    a="modified globally"
    print(a)

    A()   
    print(a)'''

'''s="im aakanksha"
print(s)
s1="pandey"
S=s+s1
print(S)'''

'''s="hello"
s1= "H" + s[1:]
s2=s.replace("hello","pandey")
print(s1)
print(s2)'''


'''age=18
if age<=18:
    print("eligible to vote")
else:
    print("not eligible to vote")'''


"""num=0
while(num<5):
    num=num+1
    print("aakanksha")
else:
    print("pandey")"""


'''n=4
for i in range(1,n):
    print(i)'''

"""li=["a","b","c"]
for i in li:
    print(i)
tup=("aaka","nk","sha")  
for i in tup:
    print(i)"""


'''for i in range(1, 5):
  for j in range(i):
    print(i, end=' ')
    print()'''

'''def subnum(x,y):
   return(x-y)

a=5
b=3

res=subnum(a,b)
print("substraction of", a , "and", b ,"is", res)'''


'''def add(a,b):
    return a+b

 res=add(4,6)
print(res)'''

'''sq=lambda x: x**2
print(sq(3))'''

'''class Dog:
    species="canien"
    
    def  __init__(self,name,age):
      self.name=name
      self.age=age

dog1=Dog("Alice", 5)
print(dog1.name)
print(dog1.species)'''


'''class my_info:
   def __init__(self,name,age):
      self.name=name
      self.age=age
info=my_info("Aakanksha",14)
print(info.name)
print(info.age)'''  

"""x="hii Aakanksha"
print(x)
print(type(x))"""

#is operator
"""x=["a","b","c"]
y=["a","b","c"]
z=x
print(x is z)
print(x is y)
print(x==y)"""
#input output
"""x,y,z=input("taking three values:").split()
print("Total number of students:" ,x)
print("Number of boys is: ",y)
print("Number of girls is: ",z)"""
#for loop
'''s=["Aakanksha", "Pandey"]
for i in s:
    print(i)'''
#creating a list
list1=["a","b","c","d","e","f","g","h"]
list1.insert(2,"Hello")
print(list1)
if "a" in list1:
  print("yes, 'a' in this list")
print(list1[-1])
print(list1[2:5])
print(list1[2:])
print(list1[:2])
print(list1[-4:-1])

    