# gen_key_from_pass.py
# Mike Solak
# 22 Jan 2020
# https://nitratine.net/blog/post/encryption-and-decryption-in-python/
# generates key from user input

import base64
import os

# import main

# look deeper into these imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# common import
from cryptography.fernet import Fernet

# Used os.urandom(16) to create your own a custom salt
# then change custom_salt = b'' to custom_salt = b'randomValueHere'

custom_salt = b'' # past your value in between the quotes! eample = b'value''

# handles default or custom salts
if len(custom_salt) > 4:
    salt = custom_salt
else:
    salt = b's\x03`\nJL\xe5S\x12<>\xac\xbc\xee\xd4\x88'

def get_pass():
    # obtain password and return encoded password
    password_provided = input('Your encryption password: ')
    # converts to type bytes
    encoded_password = password_provided.encode()
    return encoded_password

def get_key(byte_password):
    
    # Can only use kdf once??
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend = default_backend()
    )
    # convert key to url safe base 64
    key = base64.urlsafe_b64encode(kdf.derive(byte_password))
    return key

def print_key(encoded_key):
    print(encoded_key.decode())

def main():
    password = get_pass()
    key = get_key(password)
    return key

if __name__ == '__main__':
    key = main()
    print(key.decode())



