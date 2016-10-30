
#Create an application that uses a dictionary to hold the data

dicRow1 = {"ID":"1", "Name":"Bob Smith", "Email":"bsmith@hotmail.com"}
dicRow2 = {"ID":"2", "Name":"Sue Jones", "Email":"suej@yahoo.com"}
dicRow3 = {"ID":"3", "Name":"Joe James", "Email":"joejames@gmail.com"}
lstTable = [dicRow1, dicRow2, dicRow3]
print(dicRow1, dicRow2, dicRow3)

#Add code that lets users appends a new row of data.
#Add a loop that lets the user keep adding rows.
while(True):
    strID = input("Input an ID: ")
    strName = input("Input Customer Name (First and Last): ")
    strEmail = input("Input Customer Email: ")
    print("You Entered: ", strID, strName, strEmail)
    dicRowX = {"ID":strID, "Name":strName, "Email":strEmail}
    print(dicRowX)
    lstTable.append(dicRowX)
    print(lstTable)
    strMoreData = input("Add another customer? (y/n): ")
    if(strMoreData.lower() == "y"): continue
    else: break

#Ask the user if they want to save the data to a file when they exit the loop
strUserInput = input("Do you want to save your data (y/n)?: ")
if(strUserInput.lower() == "y"):
    # Save the data to a file if they say 'yes'
    objFile = open("C:\python\\list.txt", "a")
    objFile.write(str(lstTable))  # write data to file
    objFile.close()  # close file
else:
    print("Data not saved")
