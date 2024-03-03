import random

def print_emoji():
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    print("4) 🦎")
    print("5) 🖖")

def main():
    print_emoji()
    user = int(input("Pick a number: "))
    cpu = random.randint(1,5)
    if user == 1:
        print("You chose: ✊")
    elif user == 2:
        print("You chose: ✋")
    elif user == 3:
        print("You chose: ✌️")
    elif user == 4:
        print("You chose: 🦎")
    elif user == 5:
        print("You chose: 🖖")
    if cpu == 1:
        print("CPU chose: ✊")
    elif cpu == 2:
        print("CPU chose: ✋")
    elif cpu == 3:
        print("CPU chose: ✌️")
    elif cpu == 4:
        print("CPU chose: 🦎")
    elif cpu == 5:
        print("CPU chose: 🖖")
    if user == cpu:
        print("It's a tie!")
    elif user == 1 and cpu == 3:
        print("You win!")
    elif user == 1 and cpu == 4:
        print("You win!")
    elif user == 2 and cpu == 1:
        print("You win!")
    elif user == 2 and cpu == 5:
        print("You win!")
    elif user == 3 and cpu == 2:
        print("You win!")
    elif user == 3 and cpu == 4:
        print("You win!")
    elif user == 4 and cpu == 2:
        print("You win!")
    elif user == 4 and cpu == 5:
        print("You win!")
    elif user == 5 and cpu == 1:
        print("You win!")
    elif user == 5 and cpu == 3:
        print("You win!")
    else:
        print("You lose!")
main()


