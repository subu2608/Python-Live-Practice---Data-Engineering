
class Work:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name, "Your Age:", self.age, "\nYour authorisation have been verified." )
    def printage(self):
        print(self.name, "Your age is:", self.age)

w=Work(input("Name:"), input("Age:"))
w.printname()
w.printage()


'''
class Maths:
    def square(self, n):
        return n*n
    def cube(self, n):
        return n*n*n
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return 0
m=Maths()
print(m.square(5))
'''