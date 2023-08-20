import random 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
length = int(input("enter length of password:-  "))
password= " "

for a in range (length):
    password+=random.choice(chars)
print(password)