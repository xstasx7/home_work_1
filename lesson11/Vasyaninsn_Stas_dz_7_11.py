class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(3, -3)
c_2 = ComplexNumber(5, 20)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)