# code_user.py
# Mike Solak
# 22 Jan 2020

from cryptography.fernet import Fernet

import key_from_pass


def encode_account(acc_list: list, key: bytes):
    '''acc_list = ['username', 'password']
    will then return acc_list but encoded
    '''
    f = Fernet(key)  # key created from password
    index = 0
    while index < len(acc_list):
        cred = acc_list[index]
        # print(f'Normal:{cred}')
        cred = cred.encode('utf-8')
        #print(cred)
        cred = f.encrypt(cred)
        cred = cred.decode('utf-8')
        #print(cred)
        acc_list[index] = cred
        # print(acc_list[index])
        index += 1
    return(acc_list)


def encode_accounts(accs_list: list, key: bytes):
    for list in accs_list:
        print(list)
        list = encode_account(list, key)
    return accs_list


def decode_account(acc_list: list, key: bytes):
    '''acc_list = ['username', 'password']
    will then return acc_list but decoded
    '''
    f = Fernet(key)  # key created from password
    index = 0
    while index < len(acc_list):
        #print(acc_list[index])
        cred = acc_list[index]
        # print(acc_list)
        # make str
        # print(cred)
        # print(type(cred))
        cred = cred.encode('utf-8')
        #print(cred)
        cred = f.decrypt(cred)
        cred = cred.decode('utf-8')
        #print(cred)
        acc_list[index] = cred
        # print(acc_list[index])
        index += 1
    return(acc_list)


def decode_accounts(accs_list: list, key: bytes):
    # decodes nested list
    # sends inner list to decode account
    # print(accs_list)
    for list in accs_list:
        list = decode_account(list, key)
    return (accs_list)


if __name__ == '__main__':
    key = key_from_pass.main()
    accs_list = [['yolanda', 'pass123'], ['marvin', 'gaye']]
    encrypted_accounts = encode_accounts(accs_list, key)
    print(encrypted_accounts)
    decrypted_accounts = decode_accounts(encrypted_accounts, key)
    print(decrypted_accounts)
    re_encrypted_accounts = encode_accounts(decrypted_accounts, key)
    print(re_encrypted_accounts)
    re_decrypted_accounts = decode_accounts(re_encrypted_accounts, key)
    print(re_decrypted_accounts)
