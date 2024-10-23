#Ask user for name and age input
#Set a definition for the name and age input
#Have a loop for re-entry of name and age
#Have an array to collect the infomation given by the user
#Compose an array to find the oldest user/highest age

user_information = {}
collection_information = []   
retry = True

while retry:
    try:
        name = input("Please input your here, letters only: ")
        if not name.isalpha():
            raise ValueError("That's wrong! Letters only please.")
        age = int(input("Please input your age here: "))
        if age < 1 or age > 120:
            raise ValueError("That's wrong! Numbers only and it should be from 1 to 120 years of age.")
        user_information = {
            "name": name,
            "age": age
        }
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


age = []
for user in collection_information:
    age.append(user["age"]) 

max_age = max(age)

oldest_user = []
for user in collection_information:
    if user["age"] == max_age:
        oldest_user.append(user["name"])

for name in oldest_user:
    print(name)

