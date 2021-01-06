# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (computer_choice == 'r' and user_choice == 's'):
    print('Computer chose rock. You chose scissors. Compter wins')
    print('Sorry. You lose.')

elif (computer_choice == 'r' and user_choice == 'p'):
    print('Computer chose rock. You chose paper. You win')
    print('You win. Yay!')

elif (computer_choice == 'r' and user_choice == 'r'):
    print('Computer chose rock. You chose rock. You tie.')
    print("It's a tie. Play again?")

elif (computer_choice == 's' and user_choice == 's'):
    print('Computer chose scissors. You chose scissors. You tie.')
    print("It's a tie. Play again?")

elif (computer_choice == 's' and user_choice == 'r'):
    print('Computer chose scissors. You chose rock. You win.')
    print('You win. Yay!')

elif (computer_choice == 's' and user_choice == 'p'):
    print('Computer chose scissors. You chose paper. Computer wins.')
    print('Sorry. You lose.')

elif (computer_choice == 'p' and user_choice == 'p'):
    print('Computer chose paper. You chose paper. You tie.')
    print("It's a tie. Play again?")

elif (computer_choice == 'p' and user_choice == 'r'):
    print('Computer chose paper. You chose rock. Computer wins.')
    print('Sorry. You lose.')

elif (computer_choice == 'p' and user_choice == 's'):
    print('Computer chose paper. You chose scissors. You win.')
    print('You win. Yay!')

else: print('I do not understand that choice. Please try again.')