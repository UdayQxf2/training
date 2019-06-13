"""
BMI calculator program 3 using functions
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

#function to determine category based on BMI
def func_category(bmi):

    
    if bmi<=18.5 :
        return("The person is underweight")
    elif bmi<=24.9 : 
        return("The person is normalweight")
    elif bmi<=29.9 :
        return("The person is overweight")
    elif bmi >=30 :
        return("The person is obese")




#function to calculate BMI
def func_bmi(weight,height):

    #Calculate the BMI
    bmi = weight/(height*height)
    return bmi

#Function to get input
def getinput():

    #Get the weight as input.
    print("Enter the weight of the person")
    weight = float(input())

    #Get the height as input.
    print("Enter the height of the person")
    height = float(input())

    #This is the calling function to calculate BMI
    bmi = func_bmi(weight,height)
    print(bmi)
    category=func_category(bmi)
    print(category)
#program starts here
if __name__ == "__main__" :

    #This is the calling function to get input
    getinput()
    
