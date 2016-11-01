#-------------------------------------------------#
# Title: Module 05 Assignemnt
# Dev:   kkeeney
# Date:  October 31, 2016
# ChangeLog: (Who, When, What)
#   none yet
#-------------------------------------------------#

#----- Data -----#
# declare variables and constants
#Create a text file called Todo.txt using the following data:
#Clean House,low
#Pay Bills,high

dicTodo = {}#create dictionary for todo items
'''
newfile = open("todo.txt", "w")
newfile.write("Clean House,low\n")
newfile.write("Pay Bills,high\n")
newfile.close
#Commenting this out because it is unneeded after inital creation of the file.
'''

#------ Processing -----#
# perform tasks

#Verify that data was written and correct
#newfile = open("todo.txt", "r")
#print(newfile.read())
#2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary.
#Tip: You can use a for loop to read a single line of text from the file and then place the data into a new dictionary object.
newfile = open("todo.txt", "r")
for line in newfile:
    strTask = line
    #print(strTask)#checking to make sure line is turned into a string
    #print(strTask.split(","))#checking to make sure split actually spilts up the data
    lstTodo = strTask.split(",")
    #print(lstTodo)#checking to make sure data is in list
    #print(type(dicTodo))#making sure it is really a list
    #print(lstTodo[0]) #verify position of task in list
    #print(lstTodo[1]) #verify position of priority in list
    dicTodo[lstTodo[0]] = lstTodo[1]#3.	After you get a row of data stored in a Python dictionary, add the new “row” into a Python List object (now the data will be managed as a table or two-dimensional array).
    #print(type(dicTodo)) verify it's really a dictionary
    for task, priority in dicTodo.items():#4.	Display the contents of the List to the user.
        print("Task:", task, "| " "Priority:", priority)
newfile.close

#----- Presentation (Input/Output) -----#
# get user input
# send program output

#5.	Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
    #print ("Choose 1 to Add task")
    #print ("Choose 2 to Remove task")
    #print ("Choose 3 to Save all tasks to the Todo.txt file and exit!")
while(True):
    print ("Choose 1 to Add task")
    print ("Choose 2 to Remove task")
    print ("Choose 3 to Save all tasks to the Todo.txt file and exit!")
    strAnswer = str(input("What would you like to do?: "))
    if strAnswer == "1":
        newTask = str(input("Please enter the new task: "))
        newPriority = str(input("Please enter the priority of the new task (e.g. high, medium or low): "))
        dicTodo[newTask] = newPriority
        #print(dicTodo)checking to make sure the item was actually entered.
    elif strAnswer == "2":
        strDelete = input("Which task should be deleted?: ")
        if strDelete in dicTodo: #I wanted to account for case here, but .lower does not work for dictionaries and I ran out of time to investigate further.
            del dicTodo[strDelete]
        #print(dicTodo) checking to make sure item is deleted
    elif strAnswer == "3":
        newfile = open("todo.txt", "w")
        for task, priority in dicTodo.items():
            newfile.write(task + "," + priority + "\n")
        newfile.close #6.	Save the data from the table into the Todo.txt file when the program exits.
        print("Your file has been saved")
        break

