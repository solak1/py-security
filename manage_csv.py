import csv

# imports below are unneccessary if not contained in a packaged 
import key_from_pass
import code_user
# this csv file handles everything that 
# needs to used as a csv
# --add new list from ui--
# console/ui -> sends a name a list of new accs
# csv -> new csv 
# --login to account list-
# /mousehunt/login.py ->

def open_csv(file_name):
    '''Opens csv at file name and prints by row
    '''
    file_name = file_name + '.csv'
    print(file_name)
    csv_opened = csv.reader(open(file_name), delimiter=',')
    for row in csv_opened:
        print(f'Username: {row[0]} \t\t Password: {row[1]}')
    return csv_opened

def csv_data_to_list(file_name):
        '''
        file_name = file_name + '.csv'
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            acc_list = list(reader)
            return acc_list
        '''
        accs_list= []
        csv_opened = csv.reader(open(f'{file_name}.csv'), delimiter=',')
        # file_name.csv not found?????
        for row in csv_opened:
                acc_list = []
                acc_list.append(f'{row[0]}')
                acc_list.append(f'{row[1]}')
                accs_list.append(acc_list)
        return accs_list

def new_csv(file_name:str, data:list):
    # make sure to pass in a string with underscores
    # to prevent breaking when trying to read csv
    with open(f'{file_name}.csv', mode='w') as account_file:
        new_row = csv.writer(account_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        while len(data) > 0:
            new_row.writerow(data[0])
            data.pop(0)

def new_encoded_csv(file_name:str, acc_list:list):
    # take file_name and data from ui
    # encode
    # add to csv
    key = key_from_pass.main()
    with open(f'{file_name}.csv', mode='w') as account_file:
        new_row = csv.writer(account_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        encoded_accs = code_user.encode_accounts(acc_list, key)
        print(f'Encoded prior to adding to csv: {encoded_accs}\n{len(encoded_accs)}')
        for acc in encoded_accs:
                print(acc)
                new_row.writerow(acc)

if __name__ == '__main__':
    test_list = [['login1','pass1'],['login2', 'pass2'], ['login3', 'pass3']]
    account_list_1 = "test_accounts"
    new_encoded_csv(account_list_1, test_list)
    open_csv("test_accounts")
    