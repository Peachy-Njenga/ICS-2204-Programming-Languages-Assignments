# PEACHES WAGITHI NJENGA
# SCT211-0004/2022

#fuction that returns the current date
import datetime

def calculate_age(birth_date):
    # Get the current date
    current_date = datetime.date.today()

    # Calculate the age
    age = current_date - birth_date

    # Extract years, months, and days from the age
    years = age.days // 365
    remaining_days = age.days % 365
    months = (remaining_days // 30) + (years*12)
    
    days = (remaining_days % 30) + (months*30)

    return years, months, days

def main():
    try:
        # Input date of birth from the user
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

        # Convert the input string to a datetime object
        date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d').date()

        # Calculate the age
        years, months, days = calculate_age(date_of_birth)

        # Display the age
        print(f"Age: {years} years, {months} months, {days} days")

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


main()
