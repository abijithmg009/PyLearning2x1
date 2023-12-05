#Polymorphism
#Abstraction
#Exception

#Polymorphism - It's a concept in OOPS. it allow the object of  different classes should be treated as object
#of common super class
# object -> can behave differently based on the situation
#person -> Amit, Pramod can talk(), Anit can talk in Hindi and Pramod can talk in English

class Shape:
    def area(self):
        print("area of shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
         self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())

shape3 = Shape()
print(shape3.area())

# if rectagle area is not available, then it will call the parent area