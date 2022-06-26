import constants
import functions


players = functions.clean_data(constants.players)
Teams = functions.create_teams(constants.teams, players)

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
            if choice not in range(1,int(i)):
                raise ValueError
            print(functions.depure(constants.teams[choice-1], Teams[choice-1]))
        except ValueError:
            print("You must select one of the options using an integer from 1 to {}".format(i))

    except ValueError:
        print("You must enter 1 or 2 please")
