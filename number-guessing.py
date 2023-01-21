import random 

top_of_range=input("type a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
     
    if top_of_range<=0:
        print("please type a number larger than 0")
        quit()
    else:
        print("plese type a next time.")
        quit()

random_number=random.randint(0, top_of_range)

while True:
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("plese type a next time.")
        continue
    if user_guess == random_number:
        print("you got it!")
        break
    else:
        if user_guess > random_number:
            print("You were below the number!")
        else:
            print("You were below the number!")

print("You got it in", guesses,"guesses")



