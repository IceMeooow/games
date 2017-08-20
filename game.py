import random

def game():
    number = random.randint(1,10)
    numbers = list()
    
    while len(numbers) < 3:
        try:
            your_number = int(input("Your number is : "))
        except ValueError:
            print("It is not a number")
        else:
            if your_number == number:
                print("Congratulations ! You win!")
                break
            elif your_number < number:
                print("My number is hight than {}.".format(your_number))
            else:
                print("My number is lower than {}.".format(your_number))
            numbers.append(your_number)
    else:
        print("My number was {}".format(number))
    new_game = input("Do you want play again? (yes/no)")

    if new_game == "yes":
        game()
    else:
        print("Bye")

game()
