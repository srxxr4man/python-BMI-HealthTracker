def calculate_bmi(weight,height):
    bmi =weight/(height**2)
    return round(bmi,2)

def bmi_category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal weight"
    elif bmi<30:
        return "Overweight"
    else:
        return "Obese"

def health_suggestion(category):
    if category=="Underweight":
        return "Increase calorie intake and maintain a balanced diet."
    elif category=="Normal weight":
        return "Maintain your healthy lifestyle with regular exercise."
    elif category=="Overweight":
        return "Exercise regularly and reduce junk food intake."
    else:
        return "Consult a healthcare professional and start a structured fitness plan."

def main():
    print("===== BMI CALCULATOR =====")

    weight = float(input("Enter your weight (in kg):"))
    height = float(input("Enter your height (in meters):"))

    if weight<=0 or height<=0:
        print("Weight and height must be positive numbers.")
        return

    bmi=calculate_bmi(weight,height)
    category=bmi_category(bmi)
    suggestion=health_suggestion(category)

    print("\n===== RESULT =====")
    print("Your BMI:",bmi)
    print("Category:",category)
    print("Suggestion:",suggestion)
    print()

if __name__ == "__main__":
    main()