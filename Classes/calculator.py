class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def cube(self):
            print(f"The square of {self.n} is {self.n*self.n*self.n}")

    def squareroot(self):
            print(f"The square of {self.n} is {self.n**1/2}")


square = calculator(4)
square.square()
square.cube()
square.squareroot() 