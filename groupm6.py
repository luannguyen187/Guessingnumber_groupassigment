#Luan Nguyen, Aiperi Moldobaeva, Alina zholdubaeva

#May 24th 2023

#write a guessing program

#Randomly choose  the number
import random
def guess_num():
    chosen_number = random.randint(1,10)

    guess = int(input("Please guess number between 1 to 10: \n"))
            # print ("Please guess lower")

    if guess > chosen_number:
        print ("Please guess lower")
        guess = input()
    elif guess < chosen_number:
        print("Please guess upper")
        guess = input()
    else:
        guess == chosen_number
        print("Well done, you guessed it")

    print("TRY AGIAN")
    guess_again = input("Would you like to guess another number (Y/N): \n")
    if guess_again =="Y":
        guess_num()
    else:
        guess_again == "N"
        print("SEE YOU SOON")
guess_num()


