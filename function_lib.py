import csv
import math
CSV_LOC = '/home/ish/Projects/Python_Projects/Pens_Betting/Pens Game Data/Pens_Data.csv'


#Dictionary for teams
Teams = {
  "Ducks": 0.0,
  "Coyotes": 1.0,
  "Bruins": 2.0,
  "Sabres": 3.0,
  "Flames": 4.0,
  "Hurricanes": 5.0,
  "Blackhawks": 6.0,
  "Avalanche": 7.0,
  "Blue Jackets": 8.0,
  "Stars": 9.0,
  "Red Wings": 10.0,
  "Oilers": 11.0,
  "Panthers": 12.0,
  "Kings": 13.0,
  "Wild": 14.0,
  "Canadiens": 15.0,
  "Predators": 16.0,
  "Devils": 17.0,
  "Islanders": 18.0,
  "Rangers": 19.0,
  "Senators": 20.0,
  "Flyers": 21.0,
  #not sure if the pens should be here
  "Sharks": 22.0,
  "Kraken": 23.0,
  "Blues": 24.0,
  "Lightning": 25.0,
  "Maple Leafs": 26.0,
  "Canucks": 27.0,
  "Golden Knights": 28.0,
  "Capitals": 29.0,
  "Jets": 30.0

}

#Dictionary for the full teams names
Full_Teams = {
  "Ducks": "Anaheim Ducks",
  "Coyotes": "Arizona Coyotes",
  "Bruins": "Boston Bruins",
  "Sabres": "Buffalo Sabres",
  "Flames": "Calgary Flames",
  "Hurricanes": "Carolina Hurricanes",
  "Blackhawks": "Chicago Blackhawks",
  "Avalanche": "Colorado Avalanche",
  "Blue Jackets": "Columbus Blue Jackets",
  "Stars": "Dallas Stars",
  "Red Wings": "Detroit Red Wings",
  "Oilers": "Edmonton Oilers",
  "Panthers": "Florida Panthers",
  "Kings": "Los Angeles Kings",
  "Wild": "Minnesota Wild",
  "Canadiens": "Montreal Canadiens",
  "Predators": "Nashville Predators",
  "Devils": "New Jersey Devils",
  "Islanders": "New York Islanders",
  "Rangers": "New York Rangers",
  "Senators": "Ottawa Senators",
  "Flyers": "Philidelphia Flyers",
  #not sure if the pens should be here
  "Sharks": "San Jose Sharks",
  "Kraken": "Seattle Kraken",
  "Blues": "St. Louis Blues",
  "Lightning": "Tampa Bay Lightning",
  "Maple Leafs": "Toronto Maple Leafs",
  "Canucks": "Vancouver Canucks",
  "Golden Knights": "Vegas Golden Knights",
  "Capitals": "Washington Capitals",
  "Jets": "Winnapeg Jets"

}

#Funtions for grabing the team names

def TeamSelect(team):
    return Teams[team]
def FullTeamSelect(team):
    return Full_Teams[team]

def GetAverageGoalsAgainst(team):
  #go through every game the other team has gotten and get the avearage goals scored by them.
  #that will be used as input for the calculation.
  count = 0
  average_goals = 0
  total_goals = 0
  goals_list = []

  team_agaisnt = FullTeamSelect(team)


  with open(CSV_LOC) as f:
      reader = csv.reader(f)
      for row in reader:
        if row[0] == team_agaisnt:
          total_goals += int(row[2])
          goals_list.append(row[2])
  

  average_goals = total_goals / len(goals_list)
  floor_average_goals = math.floor(average_goals) 
  return floor_average_goals
          

#GetAverageGoalsAgainst('Ducks')