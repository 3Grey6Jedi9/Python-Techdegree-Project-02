def experience(data):
    players_experienced = 0
    for dict in data:
        if dict['experience'] == True:
            players_experienced += 1
        else:
            continue
    return players_experienced


def boolean(string):
    if string == 'YES':
        return True
    else:
        return False


def clean_data(data):
    new_data = []
    for dict in data:
        new_dict = {}
        new_dict['name'] = dict['name']
        new_dict['guardians'] = dict['guardians'].split('and')
        new_dict['height'] = dict['height'].split(' ')
        new_dict['height'] = int(dict['height'][:2])
        new_dict['experience'] = boolean(dict['experience'])
        new_data.append(new_dict)
    return new_data


def create_teams(teams, data):
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

#This function will take the teams' name (teams) and the characteristics of each team (Teams)
#and it will return a dictionary with the most important facts about those teams in a very depurated way"""


def average_height(Team):
    heights = []
    for h in Team:
        heights.append(h['height'])
    return sum(heights)/len(Team)





def players_on_Team(Team):
    players = set()
    for player in Team:
        p = player['name']
        set(p)
        players.add(p)
    return players



def guardians_on_Team(Team):
    guardians = set()
    for guardian in Team:
        g = guardian['guardians']
        set(g)
        guardians.add(g)
    return guardians






def depure(team, Team):
    Depured_Team = {}
    Depured_Team['Team'] = team + ' Stats'
    Depured_Team['Total players'] = len(Team)
    Depured_Team['Total experienced'] = experience(Team)
    Depured_Team['Total inexperienced'] = len(Team) - experience(Team)
    Depured_Team['Average height'] = average_height(Team)
    return Depured_Team
