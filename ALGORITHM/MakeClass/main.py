class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

cal1 = Calculator(3, 5)
print(cal1.add())

cal2 = Calculator(4, 2)
print(cal2.add())