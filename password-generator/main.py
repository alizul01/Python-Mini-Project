# Project password generator

import random as rd

print("Welcome to the password generator!")
print("Made by : @alizul01\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"
password = ""
length = 0

while length < 8:
    length = int(input("Enter the length of your password: "))
    if length < 8:
        print("Password must be at least 8 characters long")
    else:
        break

while length > 0:
    for i in range(length//2):
        if rd.randint(0,1) == 0:
            password += alphabet[rd.randint(0,25)].lower()
        else:
            password += alphabet[rd.randint(0,25)].upper()
        length -= 1
        
    for i in range(length//2):
        password += numbers[rd.randint(0,9)]
        length -= 1
        
    for i in range(length):
        password += symbols[rd.randint(0,9)]
        length -= 1
        
randomPass = [x for x in set(password)]       
 
print("Password kamu adalah \t: " + "".join(randomPass))
print("Panjang passwordmu \t: " + str(len(randomPass)))