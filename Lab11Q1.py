class Calculator:  
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def adder(self):  
        return self.number1 + self.number2

    def subtractor(self):  
        return self.number1 - self.number2

    def multiplier(self):  
        return self.number1 * self.number2

    def divider(self): 
        return self.number1 / self.number2

    def clear(self):  
        self.number1 = 0
        self.number2 = 0

#  ask for input and store inside x and y
x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
cal = Calculator(x, y)

print("Add: ", cal.adder())
print("Subtract: ", cal.subtractor())
print("Multiply: ", cal.multiplier())
print("Divide: ", cal.divider())

print("Numbers before clear: " + str(cal.number1) + " and " + str(cal.number2))
cal.clear()
print("Numbers after clear: " + str(cal.number1) + " and " + str(cal.number2))