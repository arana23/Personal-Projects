#===============================================================================
# Basic Calorie Count Program
# @author Aparajita Rana
# 
# Total time to code: 23 minutes
# Comments/Notes:
# Reused the menu from todo.py program -> def shortened the time
# Usage of Global variables in python!! 
# Variable named total_cal confused me... better names next time
#===============================================================================
total_cal=0;
cal_eaten=0;
foods=[];

def set_total(tot):
    global total_cal
    total_cal=tot
    print("\nYour information has been recorded, thanks!")

def eat_food(food, cal):
    foods.append(food)
    global cal_eaten
    global total_cal
    cal_eaten+=cal
    #total_cal-=cal
    print("\nYour information has been recorded, thanks!")

def remaining():
    global cal_eaten
    global total_cal
    print("You have "+(str(total_cal-cal_eaten)+" calories left to eat today."))

def total():
    global cal_eaten
    global total_cal
    global foods
    print("\nToday you have eaten:")
    for i, item in enumerate(foods,1):
        print(str(i)+'. ' + item)
    if(total_cal==cal_eaten):
        print("\nYou met your caloric intake goal! Great work")
    if(total_cal>cal_eaten):
        print("\nYou still needed to eat "+str(total_cal-cal_eaten)+" calories today.")
    else:
        print("\nYou ate "+str(cal_eaten-total_cal)+" extra calories today.")
    
menu = {}
menu[1]="Enter total desired daily caloric intake" 
menu[2]="Add eaten food & caloric value"
menu[3]="Get how many calories left"
menu[4]="Print total food eaten and calories for the day"
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
        total_cal=input("Please type in how many calorie you should be eating today.\n")  
        set_total(total_cal)  
                
    elif selection == 2:
        foo=str(raw_input("Please enter the food you ate:\n"))
        cal=int(raw_input("Please enter how many calories it was:\n"))
        eat_food(foo, cal)
    
    elif selection == 3:
        remaining()
    
    elif selection == 4:
        total()
        
    elif selection == 5:
        print("\nHave a great day!")
        condition=False
    else:
        print("That is not a menu option")
    print("\n")
