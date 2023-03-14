class Math:
    # constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print("Math class started (reference created)")

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def divide(self):
        return self.num1 / self.num2

    def multiply(self):
        return self.num1 * self.num2


# instance of the class
math = Math(14, 7)
result = math.divide()
print("result: ", result)


class Statistics(Math):
    def __int__(self, num1, num2):
        super().__init__(num1, num2)

    def variance_calculate(self):
        return self.num1 * self.num2


statistics = Statistics(5, 8)