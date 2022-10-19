'''
File contains the Artifical Neural Network machine learning model and applying it the Pens_Data set 
(whcih contains the opponent, goals for, and goals against) and predicting how many goals the penguins will score

'''

#import the libaries
from re import X
import numpy as np
import pandas as pd
from sklearn.cluster import k_means
import tensorflow as tf

tf.__version__


'''
the colomns in the data set are
opponent, goals for, and goals against, outcome

take the opponent and goals against and the outcome guess if how many goals are scored

X will be a set of the opponent and the goals for
Y will be the goals for

'''
dataset = pd.read_csv('/home/ish/Projects/Python_Projects/Pens_Betting/Pens Game Data/Pens_Data.csv')
x = dataset.iloc[:, 0:-1:2].values 
y = dataset.iloc[:, 1:2].values 

#print(x)
#print(y)


'''
Encodes the teams into 0.0 - 31.0 using the OrdinalEncoder
'''

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
ct = ColumnTransformer(transformers=[('encoder', OrdinalEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)

'''Split the test and training set'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)


ann = tf.keras.models.Sequential()

ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))
ann.add(tf.keras.layers.Dense(units = 6, activation = 'relu'))

ann.add(tf.keras.layers.Dense(units = 1, activation = 'relu'))

ann.compile(optimizer = 'adam', loss = 'mean_squared_error')#, metrics = ['accuracy'])

ann.fit(x_train, y_train, batch_size = 32, epochs = 100)

train_mse = ann.evaluate(x_train, y_train, verbose = 0)
test_mse = ann.evaluate(x_test, y_test, verbose = 0)

# print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))


#Predicting the Test set results
y_pred = ann.predict(x_test)

user_input = input("Which team do you want to predict: ")
goals_against = input("How many goals will they score: ")

prediction = ann.predict(sc.transform([[user_input, goals_against]]))


print("My Model predics the Penguins will score: {}".format(prediction))

