class calculator:
    def __init__(self, a: float, b: float, o: str):
        self.a = a
        self.b = b
        self.o = o.lower()

    def calc(self):
        if self.o == 'add':
            return self.a + self.b
        elif self.o == 'subtract':
            return self.a - self.b
        elif self.o == 'multiply':
            return self.a * self.b
        elif self.o == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero error"
        else:
            return "Invalid operation"

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
o = input("Enter operation (add, subtract, multiply, divide): ")

calc = calculator(a, b, o)
result = calc.calc()
print(result)

