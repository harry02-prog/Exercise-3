filename = "users.txt"

try:
    
    username = input("Enter Username: ")
    age = int(input("Enter Age: "))   

    
    if username.strip() == "":
        raise ValueError("Username cannot be empty.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    #
    with open(filename, "a") as file:
        file.write(username + " - " + str(age) + "\n")

    print("\nData saved successfully!\n")

except ValueError as e:
    print("Input Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    
    try:
        print("\nSaved Users:")
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No saved users yet.")

    print("System complete.")