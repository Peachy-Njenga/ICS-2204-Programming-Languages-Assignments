# PEACHES WAGITHI NJENGA
# SCT211-0004/2022

#function to calculate the total bill

def tipCalculator(tip_percentage):
    tip = (tip_percentage*bill_amount)/100
    total_bill = tip+bill_amount
    bill_per_person = total_bill/people
    print("The total bill per person is:")
    print(round(bill_per_person, 2))

n=1
while n==1:
   bill_amount = input("enter the total bill amount:")
   bill_amount = float(bill_amount)
   tip_percentage = float(input("what tip percentage of the total bill would you like to give? Choose a percentage from below:\n1. 10\n2. 12\n3. 15\n  "))
   people = float(input("How many people are splittin the bill"))

   if tip_percentage == 10:
    tipCalculator(10)

   elif tip_percentage == 12:
    tipCalculator(12)

   elif tip_percentage == 15:
    tipCalculator(15)

   else: print("Invalid input")

   n = int(input("Enter 1 to continue or any other character to terminate the program"))
       