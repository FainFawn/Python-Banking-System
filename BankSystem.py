
import random
import datetime


fee = 3
now = datetime.datetime.now()

greetings_list = ["Hey","Hello","Welcome","Howdy","Hi","Shalom",'Greetings']
greetings = random.choice(greetings_list)

print("""Type '!create' to create an account.
Type '!login' to sign in to your existing account."""'\n')

user_input = input("> ").lower()

#create--------------------
if user_input == '!create':
    client_1 = open('client1.txt', 'w')
    # user's personal name
    personal_client1 = (input("Enter your first and last name: ").title())
    client_1.write(personal_client1)

    username_client1 = (input("Enter your new account's username: "))
    client_1.write(f'\r{username_client1}')

    password_client1 = (input("Enter your account's new password: "))
    client_1.write(f'\r{password_client1}')

    client_1 = open('client1_activity.txt', 'w')
    first_deposit = input("Would you like to add money now? (Y/N):  ").lower()
    if first_deposit == 'y':
        deposit_amount = int(input("Enter the amount of money you want to add: "))
        client_1.write(f'{deposit_amount}')
        print("Account Created. ")
    if first_deposit == 'n':
        print("Account Created. ")
    client_1.close()


#login---------------------
login = False
if user_input == '!login':
    client_1 = open('client1.txt', 'r')
    username_client1_r = input("Enter your account's username: ")
    password_client1_r = input("Enter your account's password: ")

    if password_client1_r != client_1.readlines()[2]:

        print("Your info is incorrect. ")
        client_1 = open('client1.txt', 'r')
        print(client_1.readlines()[2])

    else:
        login = True
        client_1 = open('client1.txt', 'r')
        print(client_1.readlines()[2])
#body-----------------------
if login is True:
    client_1 = open('client1.txt', 'r')
    print(f'\n{greetings} {client_1.readlines()[0]}''')
    print(f'''-----------------------
The Time Is: {now.strftime("%H:%M:%S")}
-----------------------''''\n'f"""Current Date: {now.strftime('%d/%m/%y')}
-----------------------"""'')
    print("""
Type '!balance' To See The Amount Of Money You Have Available.
Type '!activity' To see The Payment History Of Your Account.

""")
    while login is True:
        user_input1 = input("> ").lower()
        user_file = open('client1_activity.txt', 'r')
        amount = user_file.readlines()[0]
        if user_input1 == "!balance":
            print(f'''---------------------------------------------
You Currently Have {amount} Shekels In Your Account.                                               
---------------------------------------------
''')
            user_file.close()

  #      client_1 = open('client1.txt', 'r')
  #      activity = client_1.readlines()[3]
  #      if user_input1 == '!activity':
  #          print(activity)

        if user_input1 == '!deposit':
            deposit_amount = input("how much money would you like to deposit?: ")
            user_file = open('client1_activity.txt','r+')

