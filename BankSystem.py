import os
import random
import datetime

now = datetime.datetime.now()

greetings_list = ["Hey", "Hello", "Welcome", "Howdy", "Hi", "Shalom", 'Greetings']
greetings = random.choice(greetings_list)

print("""Type [1] to create an account.
Type [2] to sign in to your existing account."""'\n')

fee = 3
i = 0
x = 0
g = 0

user_input = input("> ").lower()
while user_input != '1' and user_input != '2' and user_input != 'quit':
    print('Type Accordingly To The Options. ')
    user_input = input("> ").lower()
    x = x + 1
    if x > 10:
        break
# create--------------------
if user_input == '1':
    chars = "1234567890abcdefghijklmnopqrstuvwxyz"
    for x in range(0, 1):
        file_name = ""
        for x in range(0, 8):
            file_name_char = random.choice(chars)
            file_name = file_name + file_name_char

        code_exists = os.path.isfile(file_name + '.txt')
        while code_exists == True:
            for x in range(0, 1):
                file_name = ""
                for x in range(0, 8):
                    file_name_char = random.choice(chars)
                    file_name = file_name + file_name_char
                print(file_name)

        file = open(file_name + '.txt', 'w')

        personal_client1 = input("Enter your first and last name: ").title()  # user's personal name
        while len(personal_client1) < 3:
            print('Enter a name that is more than 3 characters. ')
            personal_client1 = input("Enter your first and last name: ").title()
        file.write(personal_client1)

        password_client1 = (input("Enter your account's new password: "))  # user's password
        while len(password_client1) < 8:
            print('Your Password is too Weak, Choose Another One. ')
            password_client1 = (input("Enter your account's new password: "))
        file.write(f'\n{password_client1}')

        deposit_amount = int(input("Enter the amount of money you want to add: "))
        while deposit_amount < 1:
            print("\nyou need to add more than 0. ")
            deposit_amount = int(input("Enter the amount of money you want to add: "))

        user_activity = open(file_name + '_activity.txt', 'w')
        user_activity.write(f'{deposit_amount}')
        print(f'''\nYour Account Code is: {file_name} With This Code, you will be able to log in to your account. 
Don't Forget This Code.
--------------------------------------
After Login, Check Out The User Guide.
--------------------------------------
 ''')
        print("Account Created. ")
        file.close()
# login---------------------
login = False
if user_input == '2':
    code_input = input("Enter Your Account's Code: ")

    exist = os.path.isfile(code_input + '.txt')
    while not exist:
        print("\nAccount Doesn't Exist, Try Again.  ")
        code_input = input("Enter Your Account's Code: ")
        exist = os.path.isfile(code_input + '.txt')

    if os.path.exists(code_input + '.txt'):
        file = open(code_input + '.txt', 'r')
        password_client1_r = input("\nEnter your account's password: ")

        if password_client1_r != file.readlines()[1]:
            print("Your info is incorrect. ")
            file.close()

        else:
            login = True
        # body-----------------------
        if login is True:
            os.path.isfile(code_input + '_activity.txt')
            file = open(code_input + '.txt', 'r')

            print(f'\n{greetings} {file.readlines()[0]}''')
            print(f'''----------------------
Current Time: {now.strftime("%H:%M %p")}
----------------------''''\n'f"""Current Date: {now.strftime('%d/%m/%y')}
----------------------"""'')
            print("""
Type [1] To See The Amount Of Money You Have Available. 
Type [2] To See The Account Activity.  
Type [3] To Deposit. 
Type [4] To Withdrew. 
Type [5] To Transfer Money.
Type [6] To See The User Guide. 
Type [7] To See The Advanced Options. 

            """)
            file.close()
            while login is True:
                user_input1 = input("> ").lower()

                file = open(code_input + '_activity.txt', 'r')
                amount = file.readlines()[0]

                if user_input1 == "1":
                    while int(amount) < 1:
                        print('you have no money left. ')
                        break
                    else:
                        print('''----------------------------------------------
You Currently Have {:,} Shekels In Your Account.
----------------------------------------------

                        '''.format(int(amount)))
                file.close()

                if user_input1 == '2':

                    file = open(code_input + '_activity.txt', 'r+')
                    lines = file.readlines()

                    print("⬆ - Newest. | ⬇ - Oldest. \n")
                    for line in reversed(lines):
                        if line != lines[0]:
                            print(line)
                if user_input1 == '!2':
                    with open(code_input + '_activity.txt', "r+") as f:
                        lines = f.readlines()
                        f.seek(0)
                        for line in lines:
                            if line == lines[0]:
                                f.write(line)
                                print('Activity Deleted. ')
                        f.truncate()

                if user_input1 == '3':
                    deposit_money = int(input('Enter The Amount Of Money You Want To Deposit: '))  # Deposit Money
                    while deposit_money > 30000:
                        print("You Can't Deposit More Than 30,000 At Once. ")
                        deposit_money = int(input('Enter The Amount Of Money You Want To Deposit: '))

                    deposit_money_total = deposit_money + int(amount)
                    file = open(code_input + '_activity.txt', 'r+')
                    file.write(f'{str(deposit_money_total)}'"\n")
                    file.close()
                    print('Deposit Completed. ')
                    with open(code_input + '_activity.txt', 'a+') as f:
                        f.write(f"+{deposit_money} | Deposit. \n")
                        f.close()

                if user_input1 == '4':
                    if int(amount) >= 1:

                        withdraw_money = int(
                            input('Enter The Amount Of Money You Want To Withdrew: '))  # Withdraw Money
                        if withdraw_money > int(amount):
                            print("You Can't Withdraw More Than You Have. \n")
                            withdraw_money = int(input('Enter The Amount Of Money You Want To Withdrew: '))

                        while withdraw_money > 30000:
                            print("You Can't Withdraw More Than 30,000₪ At Once. \n")
                            withdraw_money = int(input('Enter The Amount Of Money You Want To Withdrew: '))

                        withdraw_money_total = int(amount) - withdraw_money
                        with open(code_input + '_activity.txt', 'r+') as withdraw:
                            lines = withdraw.readlines()
                            withdraw.seek(0)
                            for line in lines:
                                if line == lines[0]:
                                    withdraw.write(f"{str(withdraw_money_total)}\n")
                                else:
                                    withdraw.write(line)
                            withdraw.truncate()
                            withdraw.close()
                            print('Withdrawal Completed ')

                        with open(code_input + '_activity.txt', 'a+') as withdraw:
                            withdraw.write(f"-{withdraw_money} | Withdraw. \n")
                            withdraw.close()
                    else:
                        print('You Have No Money Left. ')

                if user_input1 == '5':  # transfer money
                    while int(amount) > 1:
                        file = open(code_input + '_activity.txt', 'r+')

                        another_account = input("Who Would You Like To Transfer? Enter Their Account's Code: ")
                        another_account_exists = os.path.isfile(another_account + '.txt')
                        if another_account == code_input or another_account_exists == False:
                            print("Incorrect Information, Try Again \n")
                        else:
                            print(f'\nThe Fee Is {fee} Shekels. ')
                            transfer_amount = int(input('Enter The Amount Of Money You Would Like to Transfer: '))

                            while transfer_amount > int(amount) or transfer_amount > 30000:
                                transfer_amount = int(input('Enter The Amount Of Money You Would Like to Transfer: '))
                                print("Unsuccessful Transfer.  ")

                            amount_with_fee = transfer_amount + fee
                            amount_total = int(amount) - transfer_amount - fee

                            # User's Account ---------------
                            with open(code_input + '_activity.txt', "r+") as f:
                                lines = f.readlines()
                                f.seek(0)
                                for line in lines:
                                    if line != lines[0]:
                                        f.write(line)
                                    else:
                                        f.write(f'{str(amount_total)}'"\n")
                                f.truncate()

                            with open(code_input + '_activity.txt', 'a+') as f:

                                f.write(f"-{amount_with_fee} | Transferred-(Taken). \n")

                            # Another Account----------------
                            with open(another_account + '_activity.txt', "r+") as f:
                                money_line = f.readlines()[0]
                                another_amount = int(money_line) + transfer_amount
                                lines = f.readlines()
                                f.seek(0)
                                f.write(f"{str(another_amount)}\n")
                                for line in lines:
                                    if another_amount not in line:
                                        f.write(line)

                            with open(another_account + '_activity.txt', 'a+') as f:
                                f.write(f"+{transfer_amount} | Transferred-(Given). \n")

                            print("Transfer Complete.")

                            break

                    else:
                        print('You Have No Money Left. ')
                if user_input1 == '6':
                    print("""
►| You Can't Transfer/Deposit/Withdraw More Than 30,000₪ At once.

►| You Can't Transfer All Of Your Money To Someone Else.

►| You Need To Have At Least 1 Shekel Left In Your Account.

►| You Should Delete Your Account History When You Have No Need Of Your Old Activity.

""")

                files = [code_input + '_activity.txt', code_input + '.txt']
                if user_input1 == '7':
                    print('''-----------------
Advanced Options: 
-----------------
Type [8] To Change Your Account's Password. 
Type [9] To Delete Your Account.
Type [10] To Log Out. 
Type [!2] To Delete Account Activity. 

''')
                if user_input1 == '9':  # Deleting The Account
                    file = open(code_input + '.txt')
                    password_client1_r = input("Enter your account's password: ")
                    if password_client1_r != file.readlines()[1]:
                        print('Incorrect Password, Quiting User...')
                        break
                    else:
                        file.close()
                        for x in files:
                            os.remove(x)
                        print("Account Deleted. ")
                        break

                if user_input1 == '8':  # Changing password
                    print('Password must be more than 8 characters long.')
                    current_password = input("Enter Your Current Password: ")
                    while current_password != password_client1_r:
                        print('Incorrect, Try Again. ')
                        current_password = input("Enter Your Current Password: ")
                        i = i + 1
                    if i > 10:
                        break
                    new_password = input('Enter Your New Password: ')

                    while len(new_password) < 8:
                        print('Choose a Password that is more than 8 characters long. ')
                        new_password = input('Enter Your New Password: ')

                    while new_password == current_password:
                        print("The New Password Matches The Old One, Try Again.")
                        new_password = input('Enter Your New Password: ')

                    with open(code_input + '.txt', "r+") as f:
                        lines = f.readlines()

                        f.seek(0)
                        for line in lines:
                            if line != lines[1]:
                                f.write(line)
                        f.truncate()
                        f.write(new_password)
                        print('password has been changed. ')
                        f.close()
                        break

                if user_input == 'quit' or user_input1 == '10':  # Log Out
                    print('See You Later! ')
                    break
