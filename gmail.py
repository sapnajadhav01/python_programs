# WAP For Gmail Registration and Login Page
user = {}
while True:
    print("\n========== Gmail Menu ==========")
    print("1. Registration")
    print("2. Login")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        id = int(input("Enter Your ID: "))
        fname = input("Enter Your First Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        number = int(input("Enter Mobile Number: "))
        gender = input("Enter Gender: ")
        dob = input("Enter Date Of Birth: ")
        address = input("Enter Your Address: ")
        state = input("Enter Your State: ")
        country = input("Enter Your Country: ")

        user.update({
            id: {
                "fname": fname,
                "email": email,
                "password": password,
                "number": number,
                "gender": gender,
                "dob": dob,
                "address": address,
                "state": state,
                "country": country
            }
        })

        print("Registration Successful")

    elif choice == 2:

        email = input("Enter Email: ")
        password = input("Enter Password: ")

        found = False

        for key, value in user.items():

            if value["email"] == email and value["password"] == password:
                print("Login Successful")
                print("Welcome", value["fname"])
                found = True
                break

        if found == False:
            print("Invalid Email or Password")

    elif choice == 3:

        if len(user) == 0:
            print("No User Registered")

        else:
            print("\n===== Registered Users =====")

            for key, value in user.items():
                print("\nID :", key)
                print("Name :", value["fname"])
                print("Email :", value["email"])
                print("Password :", value["password"])
                print("Mobile Number :", value["number"])
                print("Gender :", value["gender"])
                print("Date Of Birth :", value["dob"])
                print("Address :", value["address"])
                print("State :", value["state"])
                print("Country :", value["country"])

    elif choice == 4:
        print("Thank You...")
        break

    else:
        print("Invalid Choice")