'''
File contains the Artifical Neural Network machine learning model and applying it the Pens_Data set 
(whcih contains the opponent, goals for, and goals against) and predicting how many goals the penguins will score

'''

#import the libaries
import numpy as np
import pandas as pd
from sklearn.cluster import k_means
import tensorflow as tf

tf.__version__


'''
the colomns in the data set are
opponent, goals for, and goals against, outcome

take the opponent and goals against and the outcome guess if how many goals are scored

'''
dataset = pd.read_csv('/home/ish/Projects/Python_Projects/Pens_Betting/Pens Game Data/Pens_Data.csv')

