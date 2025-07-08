print("Welcome to BMI Calculator!")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = round(weight / (height ** 2), 2)
print(f"Your BMI value: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
# bmi >= 18.5 and bmi < 25    
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
else:
    print("You are overweight.")
 