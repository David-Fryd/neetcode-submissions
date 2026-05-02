import math

class AreaCalc:
    def calculate(self, length, width=None):
        if width == None:
            return round(length ** 2 * math.pi, 2)
        return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
