from Goals_For import Predict_Goals_For
from function_lib import *
import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry('700x400')
        self.root.title('Pittsburgh Penguins Win Model')
        self.mainframe = tk.Frame(self.root, background = 'white')
        self.mainframe.pack(fill = 'both', expand = True)


        self.text = ttk.Label(self.mainframe, text = 'Will the Pens Win', background= 'white', font = ("Brass Mono", 30))
        self.text.grid(row = 0, column = 0)

        self.text = ttk.Label(self.mainframe, text = 'this is where the output will go', background= 'white', font = ("Brass Mono", 30))
        self.text.grid(row = 5, column = 0)
        

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row = 1, column = 0, pady = 10, sticky = 'NWES')
        set_text_button = ttk.Button(self.mainframe, text = 'Opponent', command = self.set_text)
        set_text_button.grid(row = 1, column = 1, pady = 10)

        self.root.mainloop()

        return

    
    def set_text(self):
        newtext = self.set_text_field.get()
        user_input = TeamSelect(newtext)
        goals_against = GetAverageGoalsAgainst(newtext)
        prediction = Predict_Goals_For(user_input, goals_against)
        output_text = "My Model predicts the Penguins will score {} goals against the {}".format(round(prediction,2), newtext)
        print(output_text)

        

if __name__ == '__main__':
    App()


# def User_Input():
# #Cleaning up variables for displaying purposes
#     team_name = input("Which team do you want to predict against: ")
#     user_input = TeamSelect(team_name)
#     goals_against = GetAverageGoalsAgainst(team_name)
    
#     prediction = Predict_Goals_For(user_input, goals_against)

#     print("My Model predicts the Penguins will score {} goals against the {}".format(round(prediction,2), team_name))



# User_Input()