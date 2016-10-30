"""lstRow1 = ["1", "Bob Smith", "bsmith@hotmail.com"]
tplRow1 = ("1", "Bob Smith", "bsmith@hotmail.com")
print(lstRow1)
print(tplRow1)

lstRow2 = ["2", "Sue Jones", "suej@yahoo.com"]
lstTable = [lstRow1, lstRow2]
print(lstTable)

lstRow1.append("555-1234")
print(lstTable)

lstRow1.remove("555-1234")
print(lstTable)

lstRow3 = ["3", "Joe James", "joejames@gmail.com"]
lstTable.insert(0, lstRow3)
print(lstTable)

lstTable.sort()
print(lstTable)
"""
'''
#1) A list and a dictionaries are very similar
#   but dictionaries use "keys" instead of indexes
lstRow1 = ["1","Bob Smith", "BSmith@Hotmail.com"]
dicRow1 = {"ID":1,"Name":"Bob Smith", "Email":"BSmith@Hotmail.com"}
print(lstRow1)
print(dicRow1)

print(lstRow1[1])
print(dicRow1["Name"])

#2) dictionaries should can be nested (multi-dimensional),
#   but may also be placed in a list to keep things simple.
print("\n--- multi-dimensional list")
dicRow2 = {"ID":"2","Name":"Sue Jones", "Email":"SueJ@Yahoo.com"}
lstTable = [dicRow1, dicRow2]
print(lstTable)

#3) You can loop through the list to see you dictionary objects
print("\n--- items in the list 'Table'")
for objRow in lstTable:
 print(objRow)

#4) Dictionaries have a number extra functions and properties
#4a) items()

print("\n--- items()")
for myKey, myValue in dicRow1.items():
 print(myKey, " = ", myValue )



#4b) values()
print("\n--- values()")
print(dicRow1.values())

#4b) keys()
print("\n--- keys()")
print(dicRow1.keys())


dicRow1 = {"ID":1,"Name":"Bob Smith", "Email":"BSmith@Hotmail.com"}
print("\n--- items()")
for myKey, myValue in dicRow1.items():
 print(myKey, " = ", myValue )
'''
'''
try:
    fltN1 = 5.0
    fltN2 = 0.0
    fltQuotient = fltN1 / fltN2
except:
    print("You can't divide", fltN1, "by", fltN2, "dummy!")
'''


def DivideValues():
    try:
        q = (fltN1 / fltN2)
    except:
            print("You can't divide", fltN1, "by", fltN2, "dummy!")
    return q
fltN1 = float(input("Enter the first number: "))
fltN2 = float(input("Enter the second number: "))
print(DivideValues())
print("Done")