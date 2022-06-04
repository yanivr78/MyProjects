# 🚨 Don't change the code below 👇
height = float(input("enter your height in feets: "))

# Convert height from feets to inches:
height *= 12
weight = float(input("enter your weight in lbs: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight * 703 / height ** 2)

print(bmi)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25: # We dont need to check bmi >= 18.5 because that we done so above.
  print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
