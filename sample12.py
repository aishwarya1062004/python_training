from datetime import datetime

def calculateAge(dob):
    birth_date = datetime.strptime(dob, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print(f"Your age is: {age}")

dob = input("Enter dob (dd-mm-yyyy): ")
calculateAge(dob)
