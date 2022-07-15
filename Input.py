import display,datetime,time

#validate the user input
def input_choice1():
    while True:
        choice1 = input("Please select your option: ")
        try:
            choice1 = int(choice1)
            if 0 < choice1 <= 2:
                return choice1
                break
            else:
                display.display_invalid()
        except:
            display.display_invalid()
            
#validate the user input   
def input_choice2():
    while True:
        choice2 = input("Please select your option: ")
        try:
            choice2 = int(choice2)
            if 0 < choice2 <= 4:
                return choice2
                break
            elif choice2 <=0 or choice2 > 4:
                display.display_invalid()
        except:
            display.display_invalid()

#validate the user input on the target muscle
def input_choice3():
    while True:
        choice3 = input("Please choose your target muscle: ")
        try:
            choice3 = int(choice3)
            if 0 < choice3 <= 13:
                return choice3
                break
            elif choice3 <= 0 or choice3 > 13:
                display.display_invalid()
        except:
            display.display_invalid()

#validate the user input on their weight
def input_weight():
    while True:
        weight = input("What is your weight(in kg):")
        try:
            weight = float(weight)
            if 0 < weight <= 300:
                return weight
                break
            elif weight <= 0 or weight > 300:
                print("Invalid input. Please enter a number between 1-300.")
        except:
            display.display_invalid()

#validate the user input on their height
def input_height():
    while True:
        height = input("Please input yout height(in m):")
        try:
            height = float(height)
            if 0 < height <= 3.5:
                return height
                break
            elif height <= 0 or height > 3.5:
                print("Invalid input. Please enter a number between 0-3.5.")
        except:
            display.display_invalid()

#validate the user input on their age
def input_age():
    while True:
        age = input("What is your age: ")
        try:
            age = int(age)
            if 0 < age <= 120:
                return age
                break
            elif age <= 0 or age > 120:
                print("Invalid input. Please enter a number between 1-120.")
        except:
            display.display_invalid()

#validate the user input on their activity level
def input_activitylvl():
    while True:
        activitylvl = input("Activity level: ")
        try:
            activitylvl = int(activitylvl)
            if 0 < activitylvl <= 5:
                return activitylvl
                break
            elif activitylvl <= 0 or activitylvl > 5:
                print("Invalid input. Please enter a number between 1-5.")
        except:
            display.display_invalid()

#validate the user input on their goal
def input_goal():
    while True:
        goal = input("Goal: ")
        try:
            goal = int(goal)
            if 0 < goal <= 3:
                return goal
                break
            elif goal <= 0 or goal > 3:
                print("Invalid input. Please enter a number between 1-3.")
        except:
            display.display_invalid()

#validate the user input on the type of trainer
def input_trainer_type():
    while True:
        trainer_type = input("Trainer Type:")
        try:
            trainer_type = int(trainer_type)
            if 0 < trainer_type <= 15:
                return trainer_type
                break
            elif trainer_type <= 0 or trainer_type >15:
                print("Invalid input. Please enter a number between 1-15.")
        except:
            display.display_invalid()

#validate the user input on their decision
def input_decision1():
    while True:
        display.display_decision1()
        decision = input("Choice: ").upper()
        try:
            if decision == "Y":
                return 1
                break
            elif decision == "N":
                print("Thank you for visiting!")
                return 0
                break
            else:
                print("Invalid input. Please enter Y or N only!")
        except:
            display.display_invalid()

#validate the user input on their decision
def input_decision2():
    while True:
        display.display_decision2()
        decision = input("Choice: ").upper()
        try:
            if decision == "Y":
                return 1
                break
            elif decision == "N":
                print("Please choose the trainer you want again.")
                return 0
                break
            else:
                print("Invalid input. Please enter Y or N only!")
        except:
            display.display_invalid()

#validate the user input on trainer code
def input_trainer(trainer_type):
    trainer_dict = display.trainer_dict(trainer_type)
    while True:
        trainer = str(input("Please input the trainer code: ").upper())
        try:
            if trainer in trainer_dict:
                trainer_name = trainer_dict.get(trainer)
                print("Trainer:",trainer_name)
                return trainer_name
                break
            else:
                print("Invalid input. Please input the alphabet beside the trainer name.")
        except:
            display.display_invalid()

#validate the booking hours
def input_book_hours():
    while True:
        hours = input("How many hours do you want to book? ") 
        try:
            hours = int(hours)
            if 0 < hours <= 3:
                return hours
                break
            elif hours <= 0 or hours > 3:
                print("Invalid input. Please enter a number between 1-3.")
        except:
            display.display_invalid()

#validate the user input on type of exercise
def input_exercise():
    while True:
        exercise = input("Please choose an excercise: ")
        try:
            exercise = int(exercise)
            if 0 < exercise <= 30:
                return exercise
                break
            elif exercise <= 0 or exercise >30:
                print("Invalid input. Please enter the correct number.")
        except:
            display.display_invalid()

#let the user to input their name
def input_name():
    name = input("Customer Name: ")
    return name

#validate the date
def input_date():
    while True:
        while True:
            date = input("Enter the date that you would like to book (dd/mm/yy): ")
            if len(date) == 8:
                day,month,year = date.split("/")
                try:
                    datetime.datetime(int(year),int(month),int(day))
                    return date
                    break
                except :
                    print("The date you input is not valid! Please try again.")
            else:
                display.display_invalid()

#validate the time
def input_time():
    while True:
        while True:
            timeformat = "%H%M"
            time = input("Enter the time that you would like to book (HHMM): ")
            if len(time) == 4:
                try:
                    validtime = datetime.datetime.strptime(time,timeformat)
                    return(time)
                    break
                except:
                    print("The date you input is not valid! Please try again.")
            else:
                display.display_invalid()
            
            
            
            
            
    
        
