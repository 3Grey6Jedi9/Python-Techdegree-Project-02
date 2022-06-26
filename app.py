import constants
import functions
import pdb


print("""BASKETBALL TEAM STATS TOOL

---- MENU ----

Here are your choices:
    1) Display Team Stats
    2) Quit\n""")

while ValueError:
    try:
        choice = int(input("Enter an option --> "))
        if choice not in range(1,3):
            raise ValueError

        if choice == 1:
            i = 1
            for team in constants.teams:
                print("{}) {}".format(i, team))
                i += 1
        else:
            exit()
        try:
            choice = int(input("Enter an option --> "))
            #Continue from here (I have to manage posible errors and then display all the characteristics of the team selected

    except ValueError:
        print("You must enter 1 or 2 please")
    
