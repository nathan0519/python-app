import os

#display menu for user to choose which function they want
def display_menu2():
    print("""
[1] Type of workout
[2] Trainers information
[3] Calculator
[4] Exit
""")

#display 2 type of calculator for the user to choose
def display_menu2_3():
    print("""
Please choose the type of calculator
[1]BMI Calculator
[2]Calories Calculator
""")

#displaythe user's BMI index
def display_BMI(BMI):
    if BMI <= 18.5:
        print("Your Body Mass Index is",round(BMI,2),"This is considered as underweight")
    elif BMI <= 25:
        print("Your Body Mass Index is",round(BMI,2),"This is considered as normal weight")
    elif BMI <= 29.9:
        print("Your Body Mass Index is",round(BMI,2),"This is considered as overweight")
    else:
        print("Your Body Mass Index is",round(BMI,2),"This is considered as Obese")

#display the user's calories intake
def display_calories(goals,calories):
    if goals == 1:
        goal = "lose"
    elif goals == 2:
        goal = "maintain"
    elif goals == 3:
        goal = "gain"
    print("In order to",goal,"weight, your daily calories intake should be",calories,".")

#tell the user that thier input is invalid
def display_invalid():
    print("Invalid input. Please try again.")

#thank you the user after they choose to exit the programme
def display_exit():
    print("Thank you for choosing us :)")

#display 2 types of gender for the user to chooose
def display_gender():
    print("""
What is your gender?
[1]Male
[2]Female
""")

#display 5 types of activity lvl for the user to choose
def display_activitylvl():
    print("""
What is your activity level?
[1]None
[2]Light
[3]Moderate
[4]Heavy
[5]Extreme
""")

#display 3 different goal for the user to choose
def display_goal():
    print("""
What is yout goal?
[1]Lose Weight
[2]Maintain Weight
[3]Gain Weight
""")

#display 15 types of trainer for the user to choose
def display_trainer():
    print("""
                       What kind of trainer do you want?
[1]Male         [6]Male and experienced             [11]Female and experienced
[2]Female       [7]Male and friendly                [12]Female and friendly
[3}Experienced  [8]Male and strict                  [13]Female and strict
[4]Friendly     [9]Male, experienced and friendly   [14]Female, experienced and friendly
{5]Strict       [10]Male, experienced and strict    [15]Female, experienced and strict
""")

#display the decision for the user to choose
def display_decision1():
    print("""
Do you want to book our trainer?
[Y]es
[N]o
""")

def display_decision2():
    print("""
Is this the trainer you want?
[Y]es
[N]o
""")

#display the user's booking information
def display_booking(name,trainer,hours,date,time):
    print(name,"have succesfully booked trainer",trainer,"for",hours,"hours","on",date,",",time)
    print("Your booking has been recorded. Thank you and please remember to arrive on time.")

#different type of trainer in dictionary
def trainer_dict(trainer_type):
    if trainer_type == 1:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah", "C":"Oscar Leo", "D":"Waynne Lee", "E":"Ryze Ho",
            "F":"George Lo", "G":"Lee Sin", "H":"Rex Lai", "I":"Harry Oliver", "J":"Charlie Sia"
            }
        return trainer_dict
    elif trainer_type == 2:
        trainer_dict = {
            "K":"Vina Sia", "L":"Ally Chia", "M":"Anabel Yi", "N":"Summer Liew", "O":"Ashley Ho",
            "P":"Faith Lim", "Q":"Bella Wong", "R":"Beatrice Sia", "S":"Vayne Sia", "T":"Senna Lu"
            }
        return trainer_dict
    elif trainer_type == 3:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah","D":"Waynne Lee", "E":"Ryze Ho",
            "G":"Lee Sin", "I":"Harry Oliver","N":"Summer Liew", "S":"Vayne Sia"
            }
        return trainer_dict
    elif trainer_type == 4:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah","F":"George Lo",  "J":"Charlie Sia","K":"Vina Sia",
            "L":"Ally Chia", "M":"Anabel Yi","Q":"Bella Wong", "R":"Beatrice Sia", "S":"Vayne Sia",
            "T":"Senna Lu"
            }
        return trainer_dict
    elif trainer_type == 5:
        trainer_dict = {
            "C":"Oscar Leo", "D":"Waynne Lee", "E":"Ryze Ho","G":"Lee Sin", "H":"Rex Lai",
            "I":"Harry Oliver","N":"Summer Liew", "O":"Ashley Ho","P":"Faith Lim"
            }
        return trainer_dict
    elif trainer_type == 6:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah", "D":"Waynne Lee", "E":"Ryze Ho","G":"Lee Sin",
            "I":"Harry Oliver"
            }
        return trainer_dict
    elif trainer_type == 7:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah","F":"George Lo","J":"Charlie Sia"
            }
        return trainer_dict
    elif trainer_type == 8:
        trainer_dict = {
             "C":"Oscar Leo", "D":"Waynne Lee", "E":"Ryze Ho", "G":"Lee Sin", "H":"Rex Lai",
             "I":"Harry Oliver"
             }
        return trainer_dict
    elif trainer_type == 9:
        trainer_dict = {
            "A":"Eden Chia", "B":"Jack Mah"
            }
        return trainer_dict
    elif trainer_type == 10:
        trainer_dict = {
            "D":"Waynne Lee", "E":"Ryze Ho","G":"Lee Sin", "I":"Harry Oliver"
            }
        return trainer_dict
    elif trainer_type == 11:
        trainer_dict = {
            "N":"Summer Liew", "S":"Vayne Sia"
            }
        return trainer_dict
    elif trainer_type == 12:
        trainer_dict = {
            "K":"Vina Sia", "L":"Ally Chia", "M":"Anabel Yi", "Q":"Bella Wong", "R":"Beatrice Sia",
            "S":"Vayne Sia", "T":"Senna Lu",
            }
        return trainer_dict
    elif trainer_type == 13:
        trainer_dict = {
            "N":"Summer Liew", "O":"Ashley Ho", "P":"Faith Lim"
            }
        return trainer_dict
    elif trainer_type == 14:
        trainer_dict = {
            "S":"Vayne Sia"
            }
        return trainer_dict
    elif trainer_type == 15:
        trainer_dict = {
            "N":"Summer Liew"
            }
        return trainer_dict
    
#display 2 differant part of the body for the user to choose        
def display_part():
    print("""
Please choose:
[1] Upper Body
[2] Lower Body
""")

#display 9 different upper part for the user to choose
def display_upper():
    print("""
[1]Traps
[2]Shoulders
[3]Chest
[4]Abs
[5]Upperback
[6]Lowerback
[7]Biceps
[8]Triceps
[9]Forearms
""")

#display 4 different lower part for the user to choose
def display_lower():
    print("""
[10]Quadriceps
[11]Calves
[12]Glutes
[13]Hamstrings
""")
    
#display different type of the exercise for to choose
def display_upperEx(target_muscle):
    if target_muscle == 1:
        print("""
[1]Shrug
[2]Upright Row
[3]Pushup
""")
        
    elif target_muscle == 2:
        print("""
[4]Incline Bench_Press
[5]Lateral Raise
[6]Military Press
""")
        
    elif target_muscle == 3:
        print("""
[7]Cable Fly
[8]Bench Press
[9]Chest Dips
""")
        
    elif target_muscle == 4:
        print("""
[10]Dumbbell Crunch
[11]Plank
[12]Garhammer Raise
""")
        
    elif target_muscle == 5:
        print("""
[13]Lat Pulldown
[14]Kettlebell Swings
""")
        
    elif target_muscle == 6:
        print("""
[15]Supermans
[16]Partial Curls
""")
        
    elif target_muscle == 7:
        print("""
[17]Chin Up
[18]Concentration Curl
""")
        
    elif target_muscle == 8:
        print("""
[19]Diamond Pushup,
[20]Bench Dip
""")
        
    elif target_muscle == 9:
        print("""
[21]Towel Pullup
[22]Crab Walk
""")

#display different type of the exercise for to choose       
def display_lowerEx(target_muscle):
    if target_muscle == 10:
        print("""
[23]Front Squat
[24]Leg Extension
""")
        
    elif target_muscle == 11:
        print("""
[25]Jumping Jack
[26]Tiptoe Walk
""")
        
    elif target_muscle == 12:
        print("""
[27]Goblet Squats
[28]Lateral Stepping
""")
        
    elif target_muscle == 13:
        print("""
[29]Glute Bridge
[30]Bench Hip Thrust
""")

        
cur_path = os.path.dirname(__file__)

#display trainer info
def trainer_info(trainer_type):
    new_path = os.path.join(cur_path+"\\trainers_info\\")
    if trainer_type == 1:
        with open(new_path+"trainer_male.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
        
    elif trainer_type == 2:
        with open(new_path+"trainer_female.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 3:
        with open(new_path+"trainer_exp.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 4:
        with open(new_path+"trainer_friendly.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 5:
        with open(new_path+"trainer_strict.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 6:
        with open(new_path+"trainer_male_exp.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 7:
        with open(new_path+"trainer_male_friendly.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 8:
        with open(new_path+"trainer_male_strict.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 9:
        with open(new_path+"trainer_male_exp_friendly.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 10:
        with open(new_path+"trainer_male_exp_strict.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 11:
        with open(new_path+"trainer_female_exp.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 12:
        with open(new_path+"trainer_female_friendly.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 13:
        with open(new_path+"trainer_female_strict.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 14:
        with open(new_path+"trainer_female_exp_friendly.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info
            
    elif trainer_type == 15:
        with open(new_path+"trainer_female_exp_strict.txt","r") as f:
            trainer_info = f.read()
            print(trainer_info)
            return trainer_info

#display exercise information for the upper body
def upper_exercise_info(target_muscle,exercise):
    new_path = os.path.join(cur_path+"\\exercise\\")
    if target_muscle == 1:
        final_path = os.path.join(new_path+"\\traps\\")
        if exercise == 1:
            with open(final_path+"shrug.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 2:
            with open(final_path+"upright_row.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 3:
            with open(final_path+"pushup.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()
            
    elif target_muscle == 2:
        final_path = os.path.join(new_path+"\\shoulders\\")
        if exercise == 4:
            with open(final_path+"incline_bench_press.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 5:
            with open(final_path+"lateral_raise.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 6:
            with open(final_path+"military_press.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()
            
    elif target_muscle == 3:
        final_path = os.path.join(new_path+"\\chest\\")
        if exercise == 7:
            with open(final_path+"cable_fly.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 8:
            with open(final_path+"bench_press.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 9:
            with open(final_path+"chest_dips.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 4:
        final_path = os.path.join(new_path+"\\abs\\")
        if exercise == 10:
            with open(final_path+"dumbbell_crunch.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 11:
            with open(final_path+"plank.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 12:
            with open(final_path+"garhammer_raise.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 5:
        final_path = os.path.join(new_path+"\\upperback\\")
        if exercise == 13:
            with open(final_path+"lat_pulldown.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 14:
            with open(final_path+"kettlebell_swings.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 6:
        final_path = os.path.join(new_path+"\\lowerback\\")
        if exercise == 15:
            with open(final_path+"supermans.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 16:
            with open(final_path+"partial_curls.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 7:
        final_path = os.path.join(new_path+"\\biceps\\")
        if exercise == 17:
            with open(final_path+"chin_up.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 18:
            with open(final_path+"concentration_curl.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 8:
        final_path = os.path.join(new_path+"\\triceps\\")
        if exercise == 19:
            with open(final_path+"diamond_pushup.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 20:
            with open(final_path+"bench_dip.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 9:
        final_path = os.path.join(new_path+"\\forearms\\")
        if exercise == 21:
            with open(final_path+"towel_pullup.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 22:
            with open(final_path+"crab_walk.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

#display exercise information for the lower body    
def lower_exercise_info(target_muscle,exercise):
    new_path = os.path.join(cur_path+"\\exercise\\")
    if target_muscle == 10:
        final_path = os.path.join(new_path+"\\quadriceps\\")
        if exercise == 23:
            with open(final_path+"front_squat.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 24:
            with open(final_path+"leg_extension.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 11:
        final_path = os.path.join(new_path+"\\calves\\")
        if exercise == 25:
            with open(final_path+"jumping_jack.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 26:
            with open(final_path+"tiptoe_walk.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 12:
        final_path = os.path.join(new_path+"\\glutes\\")
        if exercise == 27:
            with open(final_path+"goblet_squats.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 28:
            with open(final_path+"lateral_stepping.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

    elif target_muscle == 13:
        final_path = os.path.join(new_path+"\\hamstrings\\")
        if exercise == 29:
            with open(final_path+"glute_bridge.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        elif exercise == 30:
            with open(final_path+"bench_hip_thrust.txt","r") as f:
                exercise_info = f.read()
                print(exercise_info)
                return 1
        else:
            display_invalid()

#record user's booking information into a text file
def record_booking(trainer,name,date,time,hours):
    final_path = os.path.join(cur_path+"\\booking\\booking_record.txt")
    with open(final_path, "a") as f:
        strLine1 = "Trainer Name:"+str(trainer)+"\n"
        strLine2 = "Customer Name:"+str(name)+"\n"
        strLine3 = "Date:"+str(date)+"\n"
        strLine4 = "Time:"+str(time)+"\n"
        strLine5 = "Hours booked:"+str(hours)+"\n\n"
        f.write(strLine1)
        f.write(strLine2)
        f.write(strLine3)
        f.write(strLine4)
        f.write(strLine5)
        f.close()

