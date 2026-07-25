class A:
    def greet(self):
        return "A"

class B:
    def greet(self):
        return "B"

class C(A, B):
    pass

print(C().greet())         # "A": left-to-right MRO
print(C.__mro__)           # shows the resolution order