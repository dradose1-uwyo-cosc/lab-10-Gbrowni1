# Grant Browning
# UWYO COSC 1010
# 11/24/24
# Lab XX
# Lab Section: Austin 
# Sources, people worked with, help given to: 
# 

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-else block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
def read_passlist(file_path: str) -> list:
    """Reads list of passwords on rockyou.txt and returns them in listed string form."""
    path = Path(file_path)
    try:
        with open("rockyou.txt", "r") as file:
           contains = path.read_text()
           passwords = contains.splitlines()
           return passwords
        
    except:
        print("Error: File not found.")
        passwords = []
        return passwords
    
def crackin(hash: str, rockyou: str):
    """Crack hashed password by checking password list output in SHA-256"""
    passwords = read_passlist("rockyou.txt")

    if not passwords:
        print("No passwords in list")
        
        return None

    print("Releasing the crackin")   

    with open("hash", "l") as file:
        given_hash = password.strip[0] in file 
    
    for password in passwords:
        hashed_password = get_hash(password)

        if hashed_password == hash: #something wrong here i think
            print(f"Cracked. The password is {password}")
            return password
    
    print("Password not found in list.")
    return None

crackin("hash", "rockyou.txt")

def runner():
    hash_path = Path(hash)
    try:
        with open("hash", "l") as file:
           hash_contains = hash_path.read_text()
           given_hash = hash_contains.splitlines(0)
                   
    except:
        print("Error: File not found.")
        given_hash = []
        return given_hash

 
    crackin(given_hash, "rockyou.txt")

runner()
#**1 for loop after turning into an array**