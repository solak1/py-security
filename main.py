# main.py
# Mike Solak
# 22 Jan 2020

import code_user
import manage_csv
import key_from_pass
 

def simple_ui():
    # master ui?
    print('\nNote: You should create your own salt in key_from_pass.py')
    print("Otherwise, your information could be cracked.")
    handle_options()

def handle_options():
    print('Options:\n1. Encrypt new list\n2. Decrypt existing list\n3. Encrypt existing list\n4. Print list \n5. Quit using by pressing q or 4.')
    option = input("Your option: ")
    if option in '1234':
        if option == '1':
            encrypt_new_ui()
            handle_options()
        elif option == '2':
            decrypt_ui()
            handle_options()
        elif option == '3':
            encrypt_ui()
            handle_options()
        else:
            list_name = input('Your list name: ')
            print_list(list_name)
            handle_options()
    elif option == 'q':
        print('good bye!')
        quit()
    else:
        print("Please press 1,2,4, or q.")
        handle_options()
        
def setup_accs_list(file_name):
    print(f'Using {file_name}.csv for your account file name.')
    num_accs = input("How many accounts? (ex. 3): ")
    try:
        num_accs = int(num_accs)
        list_of_accounts = []
        count = 0
        while count < num_accs:
            account = []
            new_user = input("Username: ")
            account.append(new_user)
            new_pwd = input("Password: ")
            account.append(new_pwd)
            list_of_accounts.append(account)
            count += 1
        print(list_of_accounts)
        return list_of_accounts
    except ValueError:
        setup_accs_list(file_name)   

def encrypt_new_ui():
    print("Your file will be saved in this directory.")
    print("\nNote: Your file name must not have spaces.")
    print("Example: decode_accounts_list_1\n")
    file_name = (input("File Name: "))
    if (' ' in file_name):
        simple_ui()
    else:
        accounts_list = setup_accs_list(file_name)
        manage_csv.new_encoded_csv(file_name, accounts_list)
        manage_csv.open_csv(file_name)
        print("done.")
        # include path to file name


def decrypt_ui():
    print("Your file must be in this directory.")
    print("\nNote: Your file name must not have spaces.")
    print("Example: encoded_accounts_list_1\n")
    file_name = (input("File Name: "))
    if (' ' in file_name):
        decrypt_ui()
    else:
        key = key_from_pass.main()
        acc_list = manage_csv.csv_data_to_list(file_name)
        print(acc_list)
        accounts = code_user.decode_accounts(acc_list, key)
        print(accounts)
        return accounts
        # include path to file name
        # accounts_list = setup_accs_list(file_name)
        # manage_csv.new_encoded_csv(file_name, accounts_list)

def encrypt_ui():
    print("Your file must be in this directory.")
    print("\nNote: Your file name must not have spaces.")
    print("Example: decoded_accounts_list_1\n")
    file_name = (input("File Name: "))
    if (' ' in file_name):
        encrypt_ui()
    else:
        key = key_from_pass.main()
        acc_list = manage_csv.csv_data_to_list(file_name)
        print(acc_list)
        accounts = code_user.encode_accounts(acc_list, key)
        print(accounts)
        return accounts
        # include path to file name
        # accounts_list = setup_accs_list(file_name)
        # manage_csv.new_encoded_csv(file_name, accounts_list)


def print_list(list_name: str):
    manage_csv.open_csv('list_name')

if __name__ == '__main__':
    simple_ui()

