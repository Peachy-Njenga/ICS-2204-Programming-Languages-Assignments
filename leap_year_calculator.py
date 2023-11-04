# PEACHES WAGITHI NJENGA
# SCT211-0004/2022

print("Hello! This is a program that checks whether a year is leap or not")

n=1 # for the while loop

while n==1:
    year= int(input("Input the year you want to check:\n"))

    modulus = year%4

    if modulus == 0:
        print("It is a leap year.")

    else: 
        print("It is is not a leap year.")

    n = int(input("Enter 1 to continue or any other character to terminate the program"))