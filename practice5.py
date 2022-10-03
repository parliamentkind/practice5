#1
"""
class Rectangle():

    def __init__(self, color="green", width=100, height=100):
        self.color = color
        self.width = widthself.height = height

    def square(self):
        return self.width * self.height

    def __init__(self, width, height)
        self.height = height
        self.width = width

    def area1(self):
        area = (self.width + self.height) / 2
        print("area = " + area)

    rect1 = Rectangle()
    print(rect1.color)
    print(rect1.square())

    rect2 = Rectangle("yellow", 23, 34)
    print(rect2.color)
    print(rect2.square())

    rect3 = Rectangle(2, 3)
    rect3.area1()
"""

#2
"""
class name():
    def __init__(self, f_name, l_name, full_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = full_name

    def print(self):
        print("Full name of Student is: " + self.full_name + ' , ', "but you can call me Gus")


Stundent = name("Gustavo", "Fring", "Gustavo Fring")
Stundent.print()
"""

#3
"""
class calculator():

    def __init__ (self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        add1 = num1+num2
        print("num1 + num2: " + add1)

    def diff(self):
        if num1>num2:
            print("num1 is bigger")
        elif num1<num2:
            print("num2 is bigger")
        else:
            print("num1 and num2 is equal")

    def mult(self):
        mult1 = num1*num2
        print("num1 * num2: " + mult1)

    def div(self):
        dev1 = num1/num2
        print("num1/num2: " + dev1)
        
object = calculator(num1, num2)
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
choice = str(input("Choose the case(Addition, Difference, Multiplication, Division)"))

if choise == "Addition":
    object.add()
elif choise == "Difference":
    object.diff()
elif choice == "Multiplication":
    object.mult()
elif choise == "Division":
    object.div()
else:
    print("Enter case correcty")
"""





