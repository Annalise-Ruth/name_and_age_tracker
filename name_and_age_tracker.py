

user_information = {}
collection_information = []   
retry = True
specialCharacters = ["-", ",", ".", "*", "'"]

#Ask user for name and age input
while retry:
#Have a loop for re-entry of name and age
#Set a definition for the name and age input, for name characters only    
    try:
        full_name = input("Please input your name here, letters only: ")
        for name in full_name:    
            if not name.isalpha() and not name.isspace() and name not in specialCharacters:
                print(name)
                raise ValueError("That's wrong! Letters only please.")
#For age, ages 1 to 120 only
        age = int(input("Please input your age here: "))
        if age < 1 or age > 120:
            raise ValueError("That's wrong! Numbers only and it should be from 1 to 120 years of age.") 
        user_information = {
            "name": full_name,
            "age": age
        }
    #Have an array to collect the infomation given by the user
        collection_information.append(user_information)
    except ValueError as value_error:
        print(value_error)
    except Exception as exception:
        print(exception)

    while True: 
        try:  
            retry_input = input("Do you want to input another entry? (Yes/No): ")
            if retry_input == "No" or retry_input == "no":
                retry = False
                break
            elif retry_input == "Yes" or retry_input == "yes":
                break
            else:
                raise ValueError("Invalid")
        except ValueError as value_error:
            print(value_error)
        except Exception as exception:
            print(exception)

#Compose an array to find the oldest user/highest age
age = []
for user in collection_information:
    age.append(user["age"]) 

max_age = max(age)

#After finding the max age or the highest number, use it to find the name of the user who its equall to
oldest_user = []
for user in collection_information:
    if user["age"] == max_age:
        oldest_user.append(user["name"])

for name in oldest_user:
    print(name)

