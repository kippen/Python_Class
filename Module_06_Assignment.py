#-------------------------------------------------#
# Title: Module 06 Assignemnt
# Dev:   kkeeney
# Date:  November 07, 2016
# ChangeLog: (Who, When, What)
#   none yet
#-------------------------------------------------#

#-- data --#
dicTodo = {}

#------ Processing -----#
# perform tasks
#5)	Make a Class to hold the functions.
class HomeInventory(object):

    #1)	Make a function for the code that loads each row of data you have from the ToDo.txt text file into a Python Dictionary
    # and then adds the rows of data to a Python List.
    def loadData():
        newfile = open("todo.txt", "r")
        for line in newfile:
            strTask = line
            lstTodo = strTask.split(",")
            dicTodo[lstTodo[0]] = lstTodo[1]
        newfile.close
        return

    #2)	Make a function for the code that displays the contents of the Python List object to the user.
    def displayData():
        for task, priority in dicTodo.items():#4.	Display the contents of the List to the user.
            print("Task:" + task + " | " + "Priority:" + priority)
        return

    #3)	Make a function for the code that allows the user to Add or Remove tasks from the list,
    # plus save the tasks in the List tasks-priorities using numbered choices.
    def addDeleteSave():
        while (True):
            print("Choose 1 to Add task")
            print("Choose 2 to Remove task")
            print("Choose 3 to Save all tasks to the Todo.txt file and exit!")
            strAnswer = str(input("What would you like to do?: "))
            if strAnswer == "1":
                newTask = str(input("Please enter the new task: "))
                newPriority = str(input("Please enter the priority of the new task (e.g. high, medium or low): "))
                dicTodo[newTask] = newPriority
                for task, priority in dicTodo.items():  # 4.	Display the contents of the List to the user.
                    print("Task:", task, "| " "Priority:", priority)
                    # print(dicTodo)checking to make sure the item was actually entered.
            elif strAnswer == "2":
                print("These are the available tasks:")
                for task, priority in dicTodo.items():  # 4.	Display the contents of the List to the user.
                    print("Task: " + task + "| " "Priority: " + priority)
                strDelete = input("Which task should be deleted?: ")
                if strDelete in dicTodo:  # I wanted to account for case here, but .lower does not work for dictionaries and I ran out of time to investigate further.
                    del dicTodo[strDelete]
                    # print(dicTodo) checking to make sure item is deleted
            elif strAnswer == "3":
                print(HomeInventory.saveClose())
                break
    #4)	Make a function for the code that saves the data from the table into the Todo.txt file when the program exits.
    def saveClose():
        newfile = open("todo.txt", "w")
        for task, priority in dicTodo.items():
            newfile.write(task + "," + priority)
        newfile.close  # 6.	Save the data from the table into the Todo.txt file when the program exits.
        print("Your file has been saved")

#-- presentation --#

print(HomeInventory.loadData())
print(HomeInventory.displayData())
print(HomeInventory.addDeleteSave())
