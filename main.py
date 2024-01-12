user_name = "mgdmgjd"
user_password = "1234"
Narek_balance = 0
today_cash_in = 0
today_cash_out = 0
today_transfers = 0


for i in range(0, 10):
    print(i)

user2_name = "Hayk"
Hayk_balance = 0

while True:
    enter_password = input("Enter your password: ")
    if enter_password == user_password:
        print("-"*25)
        print("Welcome")
        print("-" * 25)
        print("B - check balance")
        print("(+) - cash in")
        print("(-) - cash out")
        print("T - transfer")
        print("H - history")
        print("E - exit")
        print("-" * 25)
        while True:
            command = input("Enter command => ")
            if command == "B":

                print(f"Balance Narek: {Narek_balance}$")
                print("-" * 25)
                print((f"Balance Hayk: {Hayk_balance}$"))
                print("-" * 25)

            elif command == "+":
                cash_in = int(input("Enter sum => "))
                if cash_in <= 0:
                    print("invalid sum, try again")
                else:
                    Narek_balance += cash_in
                    today_cash_in += cash_in
                    print("Operation completed!")

            elif command == "-":
                cash_out = int(input("Enter sum => "))
                if cash_out <= 0 or cash_out > Narek_balance:
                    print("invalid sum, try again")
                else:
                    Narek_balance -= cash_out
                    today_cash_out += cash_out
                    print("Operation completed!")

            elif command == "T":
                transfer_to = input("write the name of the person to whom you want to transfer money: ")
                if transfer_to != "Hayk":
                    print("Invalid name, try again")
                transfer = int(input("Enter sum => "))
                if transfer <= 0 or transfer > Narek_balance:
                    print("invalid sum, try again")
                else:
                    Narek_balance -= transfer
                    Hayk_balance += transfer
                    print("Operation completed!")
                    today_transfers += transfer


            elif command == "H":
                print(f"Today cash in: {today_cash_in}$")
                print(f"Today cash out: {today_cash_out}$")
                print(f"Today transfers: {today_transfers}$")

            elif command == "E":
                print("EXIT")
                break

            else:
                print("Invalid command, try again")



    else:
        print("incorrect password, try again: ")