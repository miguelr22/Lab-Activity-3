#Miguel Rodriguez
#March 4,2021
#CSS 225 Lab Activity 3
#player_actions.py


def check_play_again(user_input):
    if user_input == "Y":
        print("I would like to play again.")
    elif user_input == "N":
        print("I would not like to play again.")
    else:
        print("Invalid input")

check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))




#x = 1
##Defining x as 1

#if x == 0:
##Checks if x is EXACTLY EQUAL to 0
#    print("Hello!")
#elif x == 1:
##If the statement on line 12 doesn't pass, checks if x is EXACTLY EQUAL to 1
#    print("Hey!")
#else:
##If neither line 12 or line 15 pass, this automatically passes.
#    print("Bye!")