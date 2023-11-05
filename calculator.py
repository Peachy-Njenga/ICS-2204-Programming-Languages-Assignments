#PEACHES WAGITHI NJENGA
#SCT211-0004/2022

def calc (a,b): #function for input of numbers and arithmetics
    var= input(" Choose an operation below. \n a-addition \n s-subtraction \n m-multiplication \n d-division:  \n")
    if var == "a":
       print(a+b)
    elif var == "s":
        print(a-b)
    elif var == "m":
        print(a*b)
    elif var == "d":
        print(a/b)
    else:
        print("Invalid option")
        

name = input("Enter your name")

print("Hello " +name +"! This is a program to add, subtract, multiply or divide two numbers. " ) 

#prompt for input
num1 = int(input("enter your first number"))
num2 = int(input("Enter your second number"))

calc(num1,num2)





