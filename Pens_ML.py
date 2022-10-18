'''
File contains the Artifical Neural Network machine learning model and applying it the Pens_Data set (whcih contains the opponent, goals for, and goals against) and predicting if the penguins win or not.
'''


#importing the libaries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from Goals_For import *

tf.__version__


#Importing the Dataset
dataset = pd.read_csv('/home/ish/Projects/Python_Projects/Pens_Betting/Pens Game Data/Pens_Data.csv')
X = dataset.iloc[:, :-1].values # the Opponent and the goals for and against
Y = dataset.iloc[:, -1].values # W or L 

#print(X)
#print(Y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(Y)
#print(Y)


'''
Encodes the Teams into numbers 0 - 31
'''
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
ct = ColumnTransformer(transformers=[('encoder', OrdinalEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)


''' Split the test and training set'''
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

'''Standardize the dataset and use the fit method on the independent variables'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

''' Create the Artifical Neural Network'''
ann = tf.keras.models.Sequential()

#Creating the hidden layers of the network
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))

#Creating the output layer
ann.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))

#Compling the ANN
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Using backpropagation to retrain the model
ann.fit(X_train, Y_train, batch_size = 32, epochs = 100)

#print(ann.predict(sc.transform([[0.0, 0, 0]])) > 0.5)

# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
np.concatenate((y_pred.reshape(len(y_pred),1), Y_test.reshape(len(Y_test),1)),1)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, y_pred)
#print(cm)
print(accuracy_score(Y_test, y_pred))

user_input = input("Which team do you want to predict: ")
print(ann.predict(sc.transform([[user_input, 0, 0]])) > 0.5)





