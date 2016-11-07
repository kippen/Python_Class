'''
LAB 6-2: Working with returned lists
1)	Create a function that returns a list of the Sum, Difference, Product, and Quotient of two numbers.
2)	Display the results to the user.
3)	Divide you program into data, processing, and presentation sections.
'''

#-- Data --#
fltN1 = 0.0
fltN2 = 0.0
lstAnswer = []

#-- Processing --#
def basicMath(fltN1, fltN2):
    s = fltN1 + fltN2
    d = fltN1 - fltN2
    p = fltN1 * fltN2
    q = fltN1 / fltN2
    #lstAnswer = [s, d, p, q, fltN1, fltN2] - this didn't work
    return [s, d, p, q, fltN1, fltN2]#adding brackets makes it a list instead of a tuple

#-- Presentation --#
fltN1 = float(input("what is the first number? "))
fltN2 = float(input("what is the second number? "))
lstAnswer = basicMath(fltN1, fltN2)
print("sum = ", lstAnswer[0],"\n" "difference =", lstAnswer[1],"\n"
    "product = ", lstAnswer[2],"\n" "quotient = ", lstAnswer[3],"\n"
    "The numbers you input were", lstAnswer[4], "&", lstAnswer[5])

#positional v named arguments
print(basicMath(fltN1 = 5.6, fltN2 = 4.4))