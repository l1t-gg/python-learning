import random
print("What do you choose?")
r = print(input("Type 0 for Rock, 1 for Paper and 2 for Scissors"))

n = random.randint(0,2)
if n == 0:
    print("Computer chose Rock!")
elif n == 1:
    print("Computer chose Paper!")
elif n == 2:
    print("Computer chose Scissors!")

if r == n:
    print("It's a tie")
elif r==0 and n==1:
    print("Computer won!")
elif r==0 and n==2:
    print("You won!")
elif r==1 and n==0:
    print("You won!")
elif r==1 and n==2:
    print("Computer won!")
elif r==2 and n==0:
    print("Computer won!")
elif r==2 and n==1:
    print("You won!")
