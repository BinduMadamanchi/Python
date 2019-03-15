# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:54:25 2019

@author: rishi
"""
import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from numpy import argmax
from keras.utils import to_categorical
# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("Breas Cancer.csv", header=0).values
data=dataset[0:,1]
encoder= LabelEncoder()
encoder.fit(data)
encoded_data = encoder.transform(data)

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,2:31], encoded_data,test_size=0.25, random_state=100)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(10))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))