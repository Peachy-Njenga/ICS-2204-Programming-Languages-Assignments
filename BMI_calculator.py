# PEACHES WAGITHI NJENGA
# SCT211-0004/2022

def Bmi(weight, height):
    bmi = weight/(height**2) 
    print(bmi)

    if bmi < 18:
       print("Underweight")

    elif bmi > 24:
       print("Overweight")

    else: print("Normal weight")

print("Hello, this is a program to calculate Body mass index")
weight = int(input("Enter weight in kilograms"))
height = int(input("Enter height in meters"))

Bmi(weight,height)



    