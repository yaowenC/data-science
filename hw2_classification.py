import sys
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

if sys.argv[1]=='R':
    data = pd.read_csv(sys.argv[2])
    test = pd.read_csv(sys.argv[3])
    lr=linear_model.LogisticRegression(penalty='l2',solver='lbfgs',multi_class='ovr')
    X= data.iloc[:,:-1]
    y= data.iloc[:,-1]

    lr.fit(X,y)
    
    result=lr.predict(test)
    df = pd.DataFrame(result)
    df.to_csv('predict.csv',index=0)

elif sys.argv[1]=='D':
    data = pd.read_csv(sys.argv[2],index_col=0)
    test = pd.read_csv(sys.argv[3],index_col=0)
    dct = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0)
    X= data.iloc[:,:-1]
    y= data.iloc[:,-1:]

    dct.fit(X,y)
    
    result=dct.predict(test)
    df = pd.DataFrame(result)
    df.to_csv('predict.csv',index=0)

elif sys.argv[1]=='S':
    data = pd.read_csv(sys.argv[2],index_col=0)
    test = pd.read_csv(sys.argv[3],index_col=0)
    svc_model = svm.SVC(C=400, kernel='rbf', degree=3 , gamma=0.001, decision_function_shape='ovr')
    X= data.iloc[:,:-1]
    y= data.iloc[:,-1]
    
    svc_model.fit(X, y)
    
    result=svc_model.predict(test)
    df = pd.DataFrame(result)
    df.to_csv('predict.csv',index=0)

elif sys.argv[1]=='N':
    data = pd.read_csv(sys.argv[2],index_col=0)
    test = pd.read_csv(sys.argv[3],index_col=0)
    scaler = StandardScaler()
    X= data.iloc[:,:-1]
    y= data.iloc[:,-1]
    scaler.fit(X)
    X = scaler.transform(X)
    test = scaler.transform(test)
    mlp = MLPClassifier(activation='tanh',solver='adam',hidden_layer_sizes=(200,),max_iter=2000)

    mlp.fit(X,y)

    result = mlp.predict(test)
    df = pd.DataFrame(result)
    df.to_csv('predict.csv',index=0)


    

