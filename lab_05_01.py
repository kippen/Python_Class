'''
1)  Create an application that uses a list to hold the following data:

Id	Name	Email
1	Bob Smith	BSmith@Hotmail.com
2	Sue Jones	SueJ@Yahoo.com
3	Joe James	JoeJames@Gmail.com

2)	Add code that lets users appends a new row of data.
3)	Add a loop that lets the user keep adding rows.
4)	Ask the user if they want to save the data to a file when they exit the loop.
5)	Save the data to a file if they say 'yes'
'''

#Create an application that uses a list to hold the following data
lstHeader = ["ID", "Name", "Email"]
lstRow1 = ["1", "Bob Smith", "bsmith@hotmail.com"]
lstRow2 = ["2", "Sue Jones", "suej@yahoo.com"]
lstRow3 = ["3", "Joe James", "joejames@gmail.com"]
lstTable = [lstRow1, lstRow2, lstRow3]
print(lstTable)

#Add code that lets users appends a new row of data.
#Add a loop that lets the user keep adding rows.
while(True):
    strID = input("Input an ID: ")
    strName = input("Input Customer Name (First and Last): ")
    strEmail = input("Input Customer Email: ")
    print("You Entered: ", strID, strName, strEmail)
    lstRowX = [strID, strName, strEmail]
    print(lstRowX)
    lstTable.append(lstRowX)
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



