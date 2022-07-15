#calculate BMI
def calculate_BMI(weight,height):
    BMI = (weight /(height*height))
    return BMI

#calculate calories for male
def calculate_calories_male(height,weight,age):
    calc_height = ((6.2 * height * 100)/2.54)
    calc_weight = 12.7 * weight
    calc_age= 6.76 * age
    BMR_male = 66 + calc_height + calc_weight - calc_age
    return BMR_male

#calculate calories for female
def calculate_calories_female(height,weight,age):
    calc_height = ((4.35 * height * 100)/2.54)
    calc_weight = 4.7 * weight
    calc_age = 4.7 * age
    BMR_female = 665.1 + calc_height + calc_weight - calc_age
    return BMR_female

#calculate the value of activity 
def calculate_activity(activity_level,BMR):
    activity = 0
    if activity_level == 1:
        activity = 1.2 * BMR
    elif activity_level == 2:
        activity = 1.375 * BMR
    elif activity_level == 3:
        activity = 1.55 * BMR
    elif activity_level == 4:
        activity = 1.725 * BMR
    elif activity_level == 5:
        activity = 1.9 * BMR

    return activity

#calculate calories
def gain_or_lose(goals,activity):
    calories = 0
    if goals == 1:
        calories = activity - 500
        return calories
    elif goals == 2:
        calories = activity
        return calories
    elif goals == 3:
        while True:
            gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
            try:
                if gain == 1: 
                    calories = activity + 500
                    return calories
                    break
                elif gain == 2:
                    calories = activity + 1000
                    return calories
                    break
            except:
                print("Invalid input.Please try again")
    
