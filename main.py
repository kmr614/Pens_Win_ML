from Goals_For import Predict_Goals_For
from function_lib import *



def User_Input():
#Cleaning up variables for displaying purposes
    team_name = input("Which team do you want to predict against: ")
    user_input = TeamSelect(team_name)
    goals_against = input("How many goals will the {} score: ".format(team_name))
    
    prediction = Predict_Goals_For(user_input, goals_against)

    print("My Model predicts the Penguins will score {} goals against the {}".format(round(prediction,2), team_name))



User_Input()