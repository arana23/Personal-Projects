#===============================================================================
# Basic To-Do Program
# Created by Aparajita Rana
# 
# Total time to code: 1 hour 41 mins
# Comments/Notes:
# Very breakable-  no checkers for an out of range number
#                  had forgotten how to use enumerate 
#                  raw_input vs input depends on python version
#===============================================================================

def print_list(lst):
    print("\nHere are the tasks you still have to do:\n")
    for i, item in enumerate(lst,1):
        print(str(i)+'. ' + item)
        
def add_todo():
    val=raw_input("\nEnter different tasks to do, type done when complete:\n")
    while val!='done':
        todo_list.append(str(val))
        val=raw_input()
    print("Thanks! Your tasks are saved\n")

def delete_todo():
    print("\nYour current to-do list is:\n")
    print_list(todo_list)
    loc=raw_input("Enter the number of the element you want to remove:")
    del todo_list[int(loc)-1]
    print("\nThe item has been removed!")

def mark_complete():
    print_list(todo_list)
    loc=raw_input("Enter the number of the element you completed:")
    completed.append(todo_list[int(loc)-1])
    del todo_list[int(loc)-1]
    print("\nThe item has been marked as completed! Great job!")
    
menu = {}
menu[1]="Add to To-Do List" 
menu[2]="Delete from To-Do List"
menu[3]="Mark item as completed"
menu[4]="Print To-Do List"
menu[5]="Exit"
todo_list=[]
completed=[]
condition=True;

while(condition):
    print("Menu")
    for x in menu:
        print(str(x)+". "+menu[x])
    
    selection=input("Please Select:") 
    
    if selection == 1:
        add_todo()    
                
    elif selection == 2:
        delete_todo()
    
    elif selection == 3:
        mark_complete()
    
    elif selection == 4:
        print_list(todo_list)
        
    elif selection == 5:
        print("Today you completed:")
        for x in completed:
            print x
        print("\nHave a great day!")
        condition=False
    else:
        print("That is not a menu option")
    print("\n")
