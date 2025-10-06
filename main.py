import json
file = open("user.json","r")
data = json.load(file)

profile = input("Do you have account?(yes/no)").strip().lower()

if profile == "yes":
    while True:
        ID = int(input("Enter your ID: "))
        user_found = None
        for user in data:
            if user["ID"] == ID:
                user_found = user
                break
        if user_found is None:
            print("ID not found. Please try again.")
            continue
        password = input("Enter your password: ")
        if password == user_found["password"]:
            print("Welcome back", user_found["user_name"])
            break
        else:
            print("Password incorrect. Please try again.")

elif profile == "no":
    new_a = input("create new account :").strip().lower()
    if new_a == "ok":
        new_name = input("Enter a username:")
        Balance = int(input("Enter your balance :"))
        while True:
            while True:
                new_password = input("Enter your password: ").strip()
                if len(new_password) >= 8:
                    break
                print("Error: Password must be at least 8 number.")
            while True:
                phone = input("Enter your phone number: ").strip()
                if len(phone) == 11:
                    break
                print("Error: Phone number must be 11 digits.")
            while True:
                Email = input("Enter your email: ").strip()
                if "@" in Email and "." in Email and len(Email) >= 6:
                    break
                print("Error: Please enter a valid email address.")
            break

        id_counter = 1
        new_person = {
            "user_name": new_name,
            "password": new_password,
            "ID": id_counter,
            "phone": phone,
            "balance": Balance,}
        data.append(new_person)
        with open("user.json", "w") as file:
            json.dump(data, file)
        for new_person in data:
            id_counter += 1


        print(f"Registered successfully! Your ID is: {id_counter}")


while True:
    print("Menu")
    print("1.deposit")
    print("2.withdraw")
    print("3.transfer")
    print("4. check balance")
    print("5.Exit")
    choice = input("Enter your choice:").strip().lower()
    if choice=="1":
        user_name = input("Enter your username :").strip().lower()
        name_deposit = int(input("Enter your deposit :").strip())
        currency_List = ["usd","sar", "l.e"]
        money = input("Enter your currency you want :").strip().lower()
        while True:
            for user in data:
                if user["user_name"]== user_name:
                    print("Deposit completed successfully")
                    if money == "usd":
                        usd_number = name_deposit * 48
                        print(usd_number)
                    elif money == "sar":
                        sar_number = name_deposit * 12
                        print(sar_number)
                        break
                    else:
                        print(name_deposit)
                    break
            else:
                print("Deposit was not successful")
                break
            with open("user.json", "w") as file:
                json.dump(data, file)
    if choice == "2":
        user_name = input("Enter your username :").strip().lower()
        name_withdraw = int(input("Enter your withdraw :").strip())
        currency = ["usd", "sar", "l.e"]
        money = input("Enter your currency you want :").strip().lower()
        while True:
            for user in data:
                current_balance = user["balance"]
                if user["user_name"] == user_name and name_withdraw <= current_balance :
                    print("withdrawal completed successfully")
                    if money == "usd":
                        usd_number = name_withdraw * 48
                        print(usd_number)
                    elif money == "sar":
                        sar_number = name_withdraw * 12
                        print(sar_number)
                    else:
                        print(name_withdraw)
                    break
                else:
                    print("Withdrawal was not successful")
                break
            with open("user.json", "w") as file:
                json.dump(data, file)
    elif choice == "3":
        amount_transfer = int(input("Enter the amount you want to transfer :").strip())
        ID_D=int(input("ID D will send the money."))
        ID_S=int(input("ID S will receive the money."))

        for user in data:
            while True:
                if user["ID"] == ID_D:
                    if user["balance"] >= amount_transfer:
                        user["balance"] -= amount_transfer
                    suptract = user["balance"] - amount_transfer
                    print(f"{amount_transfer}L.E was transferred successfully")
                    print(f"your balance is  {suptract}")
                    break
                for user in data:
                    if user["ID"] == ID_S:
                        user["balance"] += amount_transfer
                        break
                else:
                    print("error")
                break
        with open("user.json", "w") as file:
            json.dump(data, file)
    elif choice == "4":
        user_name = input("Enter your  username :").strip().lower()
        for user in data:
            if user["user_name"] == user_name:
                print(user)
                break
            else:

                print("error")

    elif choice == "5":
            print(" I am happy to be help. see you soon!")
            break
    else:
        print("Invalid choice")