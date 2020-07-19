# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/176r8IaOo1uQjkQE24vn1EtfCxO0RY4Bw
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

print(data.head())

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

print(data.head())

predict = "G3"

#array for attributes
x = np.array(data.drop([predict], 1))

#array for labels that we are trying to predict, store values of G3
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

accuracy = linear.score(x_test, y_test)
accuracy_percentage = accuracy * 100
print("Accuracy of predictions: " + str(round(accuracy_percentage, 2)) + "%")

print("Coefficients:\n", linear.coef_)
print("Intercept:\n", linear.intercept_)

predictions = linear.predict(x_test)

for p in range(len(predictions)):
  print(predictions[p], x_test[p], y_test[p])
  print()
