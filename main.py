import display,process,Input,GUI


GUI.GUI_login()

while True:
    display.display_menu2()
    choice2 = Input.input_choice2()
    if choice2 == 4:
        display.display_exit()
        break
    else:
        while True:
            if choice2 == 1 :
                display.display_part()
                target_body = Input.input_choice1()
                if target_body == 1:
                    display.display_upper()
                    while True:
                        target_muscle = Input.input_choice3()
                        itarget_muscle = int(target_muscle)
                        if 0 < itarget_muscle < 10:
                            display.display_upperEx(itarget_muscle)
                            while True:
                                exercise = Input.input_exercise()
                                decision = display.upper_exercise_info(target_muscle,exercise)
                                if decision == 1:
                                    break
                                else:
                                    continue
                            break
                        else:
                            display.display_invalid()
                elif target_body == 2:
                    display.display_lower()
                    while True:
                        target_muscle = Input.input_choice3()
                        itarget_muscle = int(target_muscle)
                        if 9 < itarget_muscle < 14:
                            display.display_lowerEx(itarget_muscle)
                            while True:
                                exercise = Input.input_exercise()
                                decision = display.lower_exercise_info(target_muscle,exercise)
                                if decision == 1:
                                    break
                                else:
                                    continue
                            break
                        else:
                            display.display_invalid()
                break
            elif choice2 == 2 :
                display.display_trainer()
                trainer_type = Input.input_trainer_type()
                display.trainer_info(trainer_type)
                decision1 = Input.input_decision1()
                if decision1 == 1:
                    decision2 = 0
                    while decision2 == 0:
                        trainer = Input.input_trainer(trainer_type)
                        decision2 = Input.input_decision2()
                        if decision2 ==1:
                            name = Input.input_name()
                            date = Input.input_date()
                            time = Input.input_time()
                            hours = Input.input_book_hours()
                            display.record_booking(trainer,name,date,time,hours)
                            display.display_booking(name,trainer,hours,date,time)
                            break
                        else:
                            continue
                break
            elif choice2 == 3:
                display.display_menu2_3()
                while True:
                    choice2_3 = Input.input_choice1()
                    if choice2_3 == 1:
                        while True:
                            weight = Input.input_weight()
                            height = Input.input_height()
                            if weight > 0 and height > 0:
                                BMI = process.calculate_BMI(weight,height)
                                display.display_BMI(BMI)
                                break
                            else:
                                display.display_invalid()

                        break
                    elif choice2_3 == 2:
                        while True:
                            age = Input.input_age()
                            weight = Input.input_weight()
                            height = Input.input_height()
                            display.display_gender()
                            gender = Input.input_choice1()
                            if age > 0 and weight > 0 and height > 0:
                                if gender == 1:
                                    BMR_male = process.calculate_calories_male(height,weight,age)
                                    display.display_activitylvl()
                                    activity_level = Input.input_activitylvl()
                                    activity = process.calculate_activity(activity_level,BMR_male)
                                    display.display_goal()
                                    goals = Input.input_goal()
                                    calories = process.gain_or_lose(goals,activity)
                                    display.display_calories(goals,calories)
                                    break
                                elif gender == 2:
                                    BMR_female = process.calculate_calories_female(height,weight,age)
                                    display.display_activitylvl()
                                    activity_level = Input.input_activitylvl()
                                    activity = process.calculate_activity(activity_level,BMR_female)
                                    display.display_goal()
                                    goals = Input.input_goal()
                                    calories = process.gain_or_lose(goals,activity)
                                    display.display_calories(goals,calories)
                                    break
                                else:
                                    display.display_invalid() 
                            else:
                                display.display_invalid()

                        break
                    else:
                       display.display_invalid()
                break
            else:
                display.display_invalid()
            
            

                
                




