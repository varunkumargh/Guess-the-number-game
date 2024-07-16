import random
        
def guess(a, b):
    print("Guess the number from 1 to 20")
    number = random.randint(a,b)
    # print(number)
    guess = 0
    while (True):
        guess_number = int(input("Enter your guess : "))
        if(guess_number>20):
            print("Sorry but the number should be in range from 1 to 20")
            continue
        if(guess_number == number):
            print("your guess is right")
            print("you won")
            guess += 1
            print(f"you took {guess} chances to guess the number")
            break
        else:
            if(guess_number>number):
                print("Your guess is too high")
                print("Try again!")
                guess += 1
                continue
            elif(guess_number<number):
                print("Your guess is too low")
                print("Try again!")
                guess += 1
                continue
            
guess(1, 20)
while True:
    ask = str(input("Would you like to play again? (type y for yes and n for no) : "))
    if (ask.lower() == "y"):
        guess(1, 20)
    if (ask.lower() == "n"):
        quit()
    else:
        print("Invalid")
    