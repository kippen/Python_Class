'''
1)	Create a function that prints the Sum, Difference, Product, and Quotient of two numbers.
'''

def basicMath(fltN1, fltN2):
    sum = fltN1 + fltN2
    difference = fltN1 - fltN2
    product = fltN1 * fltN2
    quotient = fltN1 / fltN2
    print("sum is " + str(sum))
    print("difference is " + str(difference))
    print("product is " + str(product))
    print("quotient is " + str(quotient))

fltN1 = float(input("what is the first number? "))
fltN2 = float(input("what is the second number? "))
basicMath(fltN1, fltN2)
