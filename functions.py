def experience(data):
    """Through this function I can get the number of experienced players"""
    players_experienced = 0
    for dict in data:
        if dict['experience'] == True:
            players_experienced += 1
        else:
            continue
    return players_experienced






def boolean(string):
    """This function transforms a string into a boolean"""
    if string == 'YES':
        return True
    else:
        return False





def clean_data(data):
    """This function transforms the given data into a more proper data"""
    new_data = []
    for dict in data:
        new_dict = {}
        new_dict['name'] = dict['name']
        new_dict['guardians'] = dict['guardians'].split(' and ')
        new_dict['height'] = dict['height'].split(' ')
        new_dict['height'] = int(dict['height'][:2])
        new_dict['experience'] = boolean(dict['experience'])
        new_data.append(new_dict)
    return new_data





def create_teams(teams, data):
    """This function distributes players into the given teams in a cetain way"""
    data_copy = data.copy()
    Number_Teams = len(teams)
    Number_Players = len(data_copy)
    Players_Team = Number_Players / Number_Teams
    i = 0
    n_team = []
    Teams = teams.copy()
    while i < len(teams) - 1:
        while len(n_team) < Players_Team:
            for dict in data:
                while experience(n_team) < experience(data_copy) / Number_Teams:
                    if dict['experience'] == True:
                        n_team.append(dict)
                        data.remove(dict)
                        break
                    else:
                        break
            break
        while len(n_team) < Players_Team:
            for dict in data:
                if dict['experience'] == False:
                    n_team.append(dict)
                    data.remove(dict)
                    break
        Teams[i] = n_team
        n_team = []
        i += 1
    while Number_Players % Number_Teams != 0:
        while experience(data) > experience(Teams[0]):
            for dict in data:
                if dict['experience'] == True:
                    data.remove(dict)
                    break
                else:
                    continue
    while Number_Players % Number_Teams != 0:
        for dict in data:
            if dict['experience'] == False:
                data.remove(dict)
                break
    Teams[i] = data
    return Teams






def average_height(Team):
    """This function returns the average height of a given team"""
    heights = []
    for h in Team:
        heights.append(h['height'])
    return sum(heights)/len(Team)






def players_on_Team(Team):
    """This function returns the names of the players of a given team"""
    players = set()
    for player in Team:
        p = player['name']
        set(p)
        players.add(p)
    return players






def guardians_on_Team(Team):
    """This function returns the names of the guardians of a given team"""
    guardians_list = []
    for guardian in Team:
        if type(guardian['guardians']) == list:
            for g in guardian['guardians']:
                guardians_list.append(g)
        else:
            guardians_list.append(guardian)
    guardians = set(tuple(guardians_list))
    return guardians






def depure(team, Team):
    """This function takes the team's information and returns what really matters about that team"""
    Depured_Team = {}
    Depured_Team['Team'] = team + ' Stats'
    Depured_Team['Total players'] = len(Team)
    Depured_Team['Total experienced'] = experience(Team)
    Depured_Team['Total inexperienced'] = len(Team) - experience(Team)
    Depured_Team['Average height'] = float(average_height(Team))
    Depured_Team['Average height'] = "{:.2f}".format(Depured_Team['Average height'])
    return Depured_Team


if __name__ == "__main__":
    print("In this module I define 8 functions in order to manage data in a proper way")
