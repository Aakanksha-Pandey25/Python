try:
    print("Hi...")
except:
    ("somethig went wrong")
else:
    print("every thing is good")

finally:
    print("Always executable")  # always executable

#second
'''y = True
while y == True:
    x = input("Enter a number:")
    try:
        x= float(x)
        y=False
    except:
        print("Invalid input")
    finally:
        print("Thankyou")'''

#custom exception

class mycustomexception(Exception):
    pass
def check_value(x):
    if x < 0:
        raise mycustomexception ("Negative value not allowed")
try:
        check_value(-5)
except mycustomexception as e:
        print("caught an error:" ,e)

