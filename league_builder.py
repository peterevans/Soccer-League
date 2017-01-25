import csv

# function takes a list of players and splits tehm evenly into three teams
# the loop runs through and adds every thrid player to a specific team roster
def split_to_three_teams(roster):
    index = 0
    while index < len(roster):
        if index % 3 == 0:
            team1_roster.append(roster[index])
        elif index % 3 == 1:
            team2_roster.append(roster[index])
        else:
            team3_roster.append(roster[index])
        index += 1

if __name__ == "__main__":
    # open csv file containing a list of players, convert this to a list of dictionaries
    with open("soccer_players.csv") as csvfile:
        input_file = csv.DictReader(csvfile, delimiter = ",")
        roster_list = list(input_file)

    # set team names and create three empty team lists
    team1_name = "Sharks"
    team1_roster = []
    team2_name = "Dragons"
    team2_roster = []
    team3_name = "Raptors"
    team3_roster = []

    # create two lists, one for experienced players, one for non-experienced players
    experienced_list = []
    nonexperienced_list = []
    for player in roster_list:
        if player["Soccer Experience"] == "YES":
            experienced_list.append(player)
        else:
            nonexperienced_list.append(player)

    # calls the fucntion to take each team list and split it into three team roster_list
    split_to_three_teams(experienced_list)
    split_to_three_teams(nonexperienced_list)

    # creates a new txt file and loops throgh the three team rosters and prints the data on a new line for each entry
    with open("teams.txt", "a") as text_file:
        text_file.write(team1_name + "\n")
        for player in team1_roster:
            text_file.write("{}, {}, {}\n".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
        text_file.write(team2_name + "\n")
        for player in team2_roster:
            text_file.write("{}, {}, {}\n".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))
        text_file.write(team3_name + "\n")
        for player in team3_roster:
            text_file.write("{}, {}, {}\n".format(player["Name"], player["Soccer Experience"], player["Guardian Name(s)"]))


    for player in team1_roster:
        with open("{}.txt".format(player["Name"].lower().replace(" ", "_")), "a") as text_file:
            text_file.write("Dear {},\n\n".format(player["Guardian Name(s)"]))
            text_file.write("Welcome to your new soccer team. Please check the following info on your child\n\n")
            text_file.write("Team Name: {}\n".format(team1_name))
            text_file.write("Name: {}\n".format(player["Name"]))
            text_file.write("First Practice Time: Next Monday at 6:30 PM")
    for player in team2_roster:
        with open("{}.txt".format(player["Name"].lower().replace(" ", "_")), "a") as text_file:
            text_file.write("Dear {},\n\n".format(player["Guardian Name(s)"]))
            text_file.write("Welcome to your new soccer team. Please check the following info on your child\n\n")
            text_file.write("Team Name: {}\n".format(team2_name))
            text_file.write("Name: {}\n".format(player["Name"]))
            text_file.write("First Practice Time: Next Monday at 6:30 PM")
    for player in team3_roster:
        with open("{}.txt".format(player["Name"].lower().replace(" ", "_")), "a") as text_file:
            text_file.write("Dear {},\n\n".format(player["Guardian Name(s)"]))
            text_file.write("Welcome to your new soccer team. Please check the following info on your child\n\n")
            text_file.write("Team Name: {}\n".format(team3_name))
            text_file.write("Name: {}\n".format(player["Name"]))
            text_file.write("First Practice Time: Next Monday at 6:30 PM")
