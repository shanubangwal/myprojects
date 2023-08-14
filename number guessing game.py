import random 
n= random.randrange(1,100)
guess=int(input("num any :")) 
while n != guess:
    if guess < n:
        print("too low :")
        guess =int(input("enter again :"))
    elif guess > n:
        print("too high")
        guess =int(input("enter again :"))
    else:
        break
    print("sucessfull")
        
