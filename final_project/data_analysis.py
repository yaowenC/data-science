#-*- coding=utf-8 -*-
import nltk
from sklearn.naive_bayes import *
import sys
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mlxtend.plotting import plot_decision_regions
import scikitplot as skplt

data = pd.read_csv("C:\\Users\\Jennifer\\Desktop\\data_num.csv")
X= data.iloc[:,:-2]
y= data.iloc[:,-2:]
b = y.iloc[:,1] #0是學校,1是科系
features = []
for i in range(0,321):
    a = X.iloc[i,:]
    features.append(a)

train_X, test_X, train_y, test_y = train_test_split(X, b, test_size=0.33, shuffle=1)

model = DecisionTreeClassifier() 
#model = GaussianNB()
#model = MultinomialNB()
#model = KNeighborsClassifier()
model.fit(train_X,train_y)
predicted = model.predict(test_X)
print(cross_val_score(model, test_X, test_y, cv=10))
print(np.mean(cross_val_score(model, test_X, test_y, cv=10)))

#skplt.metrics.plot_roc_curve(test_y, predicted)
# confusion_matrix: C_{i, j} is equal to the number of observations known to be in group i but predicted to be in group j.
print(confusion_matrix(test_y, predicted))
'''
# display the relative importance of each attribute
importances = model.feature_importances_
print(importances)
indices = np.argsort(importances)[::-1]
# Plot the feature importances of the forest
print("Feature ranking:")
for f in range(train_X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
plt.figure()
plt.title("Feature importances")
plt.bar(range(train_X.shape[1]), importances[indices],
       color="r", align="center")
plt.xticks(range(train_X.shape[1]), indices)
plt.xlim([-1, train_X.shape[1]])
plt.show()
'''
skplt.estimators.plot_learning_curve(model, train_X, train_y)
plt.show()

