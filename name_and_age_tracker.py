#Ask user for name and age input
#Set a definition for the name and age input
#Have a loop for re-entry of name and age
#Have an array to collect the infomation given by the user
#Compose a ranking system for the ages that had been given by the user

user_information = {}

while True:
    while True:
        try:
            name = input("Please input your name here, letters only: ")
            if not name.isalpha():
                raise ValueError("That's wrong! Letters only please.")
            age = int(input("Please input your age here: "))
            if age < 1 or age > 120:
                raise ValueError("That's wrong! Numbers only and it should be from 1 to 120 years of age.")
            user_information.append({"name": name, "age": age})
            break
        except:
            print("Error")
    