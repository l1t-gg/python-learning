from calendar import c


print("Welcome to Choose Your Adventure")
print("Type in the options to progress your game.")
print("Let's go!!")
a = input(print("Which way would you go? Left or Right"))
if a=="left":
    print("You have reached at the sea shore.")
    b= input(print("Would you like to wait for a boat or swim?"))
    if b=="boat":
        print("You have found the treasure island and won the game!")
    else:
        print("You died due to sharks in the sea. Better luck next time!")
else:
    print("You are now at the entrance of a jungle.")
    c = input(print("Would you like to take an axe or a torch?"))
    if c=="torch":
        print("Congrats! You found the treasure due to light.")
    else:
        print("Uh oh! You died due to poison ivy.")