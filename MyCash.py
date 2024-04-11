from datetime import datetime
import os

# Get the current date and time
date = datetime.now()

cash_file_path = 'D:\\V.S.code\\V.S.code\\python\\my python\\MyCash\\cash.txt'
charges_file_path = 'D:\\V.S.code\\V.S.code\\python\\my python\\MyCash\\charges.txt'

# Open the cash file for reading and writing
cash_file = open(cash_file_path, 'r+')

# Read the existing content
cash_content = cash_file.readlines()

# Extract the balance from the first line
cash = float(cash_content[0].strip()) if cash_content else 0.0

# Open the charges file for appending
charges_file = open(charges_file_path, 'a')

# Display options and process user input
print("current date:", date.strftime("%Y-%m-%d %H:%M"))
print('\n\nWELCOME TO MyCash APPLICATION\nPLEASE CHOOSE AN OPTION:')
while True:
    print('(1) SHOW YOUR CURRENT BALANCE')
    print('(2) ADD CASH')
    print('(3) ADD EXPENSES')
    print('(4) SHOW ACTIVITY')
    print('(33) HELP')
    print('(5) EXIT')
    print('(11) Creator credits')
    
    
    
    choose = int(input('enter the number of your option: '))
    print("\n\n")
    
    if choose == 1:
        print("Your current balance is:", cash)
    elif choose == 2:
        amount_to_add = float(input('Enter the amount to add: '))
        cash += amount_to_add
        print(f'Added {amount_to_add}. Updated balance: {cash}')
        # Log the money added in the charges file
        with open(charges_file_path, 'a') as charges_file:
            charges_file.write(f'{date.strftime("%Y-%m-%d %H:%M")}: Money added: +{amount_to_add}, \n')
    elif choose == 3:
        reason = input('Enter the reason for the charge: ')
        charge_amount = float(input('Enter the charge amount: '))
        cash -= charge_amount
        print(f'Charge of {charge_amount} for {reason} applied. Updated balance: {cash}')
        # Log the charge reason, amount, and current balance in the charges file
        with open(charges_file_path, 'a') as charges_file:
            charges_file.write(f'{date.strftime("%Y-%m-%d %H:%M")}: Charge - {reason}: {charge_amount}, \n')
    elif choose == 4:
        # Show all activity from the charges file
        with open(charges_file_path, 'r') as charges_file_read:
            activity = charges_file_read.read()
            print("Activity:\n", activity)
    elif choose == 5:
        # Update the balance in the cash file before closing
        cash_file.seek(0)
        cash_file.write(f'{cash}\n')
        cash_file.truncate()
        break
    elif choose == 99:
        # Ask for confirmation before resetting files
        confirmation = input("Are you sure you want to reset the files? (y/n): ").lower()
        if confirmation == 'y':
            # Clear both files and set balance to 0.0
            with open(cash_file_path, 'w') as cash_file_clear:
                cash_file_clear.write("0.0\n")
            with open(charges_file_path, 'w') as charges_file_clear:
                charges_file_clear.write("")
            cash = 0.0
            print("Files cleared. Balance set to 0.0.")
        else:
            print("Reset canceled.")
    elif choose == 11:
        print('Creator: Eftihis Papasifakis\nsocial links: https://instagram.com/eftihis06\nIn assistance with: ChatGPT 3.5')
        
    else:
        print("Invalid option. Please choose a valid option.")
    
    print("\n\n\n")

# Close both files when done using them
cash_file.close()
charges_file.close()
