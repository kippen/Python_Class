'''
LAB 6-3: Working with classes
1)	Create a class with (4) Methods, have them return a Sum, Difference, Product, and Quotient of two numbers.
2)	Name the class MathProcessor
3)	Name the methods AddValues, SubtractValues, MultiplyValues, DivideValues.
4)	Display the results to the user by calling each method.
'''

class MathProcessor(object):

    @staticmethod
    def addMath(fltN1, fltN2):
        return fltN1 + fltN2

    @staticmethod
    def subMath(fltN1, fltN2):
        return fltN1 - fltN2

    @staticmethod
    def multMath (fltN1, fltN2):
        return fltN1 * fltN2

    @staticmethod
    def divMath (fltN1, fltN2):
        return fltN1 / fltN2

#request inputs from user
fltN1 = float(input("what is the first number? "))
fltN2 = float(input("what is the second number? "))
#addition method
fltAnswer = MathProcessor.addMath(fltN1, fltN2)
print("Sum =", fltAnswer)
#subtraction method
fltAnswer = MathProcessor.subMath(fltN1, fltN2)
print("Difference =", fltAnswer)
#multiplication method
fltAnswer = MathProcessor.multMath(fltN1, fltN2)
print("Product =", fltAnswer)
#division method
fltAnswer = MathProcessor.divMath(fltN1, fltN2)
print("Quotient =", fltAnswer)
