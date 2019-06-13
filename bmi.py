"""
BMI calculator program.
Get the user weight in KG.
Get the user height in meter.
Use this formula to calculate the BMI.
BMI = weight_of_the_user/(height of the user * height of the user)
"""

#Get the weight as input.
print("Enter the weight of the person");
weight = float(input())

#Get the height as input.
print("Enter the height of the person");
height = float(input())

#Calculate the BMI
bmi = weight/(height*height)

print("The BMI of the person is :",bmi)

