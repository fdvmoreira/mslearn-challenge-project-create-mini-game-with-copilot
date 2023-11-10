import random

# list of options for the user to choose from
options = {1:"rock", 2:"paper", 3:"scissors"}

# welcome the user to the game
print("Welcome to Rock, Paper, Scissors!")
# create a game loop that will run until the user chooses to quit
while True:
    
        # wrap the code in a try block to catch any errors
    try:
        # print the menu
        
        print("1) Rock")
        print("2) Paper")
        print("3) Scissors")
        print("4) Quit")
        print()
        
        # get the user's choice
        user_choice = int(input("Enter your choice : "))
    
        # if the user chooses to quit, break out of the loop
        if user_choice == 4:
            break
    
        # get the computer's choice
        computer_choice = random.randint(1, 3)
    
        # determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 1 and computer_choice == 2:
            print("Computer wins!")
        elif user_choice == 1 and computer_choice == 3:
            print("You win!")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
        elif user_choice == 2 and computer_choice == 3:
            print("Computer wins!")
        elif user_choice == 3 and computer_choice == 1:
            print("Computer wins!")
        elif user_choice == 3 and computer_choice == 2:
            print("You win!")
    
        # print the choices
        print("You chose " + options[user_choice] + ".")
        print("Computer chose " + options[computer_choice] + ".")
        print()
    except:
        print("You made an invalid choice. Try again.")
        continue