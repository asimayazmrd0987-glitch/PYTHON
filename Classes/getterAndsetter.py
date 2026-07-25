class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("radius must be positive")
        self._radius = value

    @property
    def area(self):               # computed, read-only property
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)     # calls the getter, looks like attribute access
c.radius = 10        # calls the setter, validates
print(c.area)         # computed on the fly, no stored area value
c.area = 100          # AttributeError — no setter defined, read-only