"""
BMI calculator program 2
Get the user weight in KG.
Get the user height in meter.
Use this formula to calculate the BMI.
BMI = weight_of_the_user/(height of the user * height of the user)

Use this level to check user category

Less than or equal to 18.5 is represents underweight
Between 18.5 -24.9 indicate normal weight
Between 25 -29.9 denotes overweight
Greater than 30 denotes obese

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

if bmi<=18.5 :
    print("The person is underweight")
elif bmi<=24.9 : 
    print("The person is normalweight")
elif bmi<=29.9 :
    print("The person is overweight")
elif bmi >=30 :
    print("The person is obese")

