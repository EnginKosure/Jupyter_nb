# Create methods for the Calculator class that can do the following:
class Calculator:

    def add(self, num1, num2):
        return num1+num2

    def subtract(self, num1, num2):
        return num1-num2

    def multiply(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        return num1/num2


calculator = Calculator()

print(calculator.add(10, 5))  # ➞ 15

print(calculator.subtract(10, 5))  # ➞ 5

calculator.multiply(10, 5)  # ➞ 50

calculator.divide(10, 5)  # ➞ 2
