# -*- coding: utf-8 -*-
"""
Created on Fri May 27 12:25:18 2022

@author: Shalini Bharathkumar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.datasets import load_iris
from scipy.stats import chi2_contingency
from scipy.stats import chi2

app=Flask(__name__)
Swagger(app)

pickle_in = open("C:/Users/Shalini Bharathkumar/application/classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    """Species Identification 
   This is using docstrings for specifications.
   ---
   parameters:  
     - name: sepal length (cm)
       in: query
       required: true
     - name: sepal width (cm)
       in: query
       required: true
     - name: petal length (cm)
       in: query
       required: true
     - name: petal width (cm)
       in: query
       required: true
   responses:
       200:
           description: The output values
       
   """
    sepallength=request.args.get("sepal length (cm)")
    sepalwidth=request.args.get("sepal width (cm)")
    petallength=request.args.get("petal length (cm)")
    petalwidth=request.args.get("petal width (cm)")
    prediction=classifier.predict([[sepallength,sepalwidth,petallength,petalwidth]])
    print(prediction)
    
    data = load_iris()
    df = pd.DataFrame(data.data, columns = data.feature_names)
    df['target'] = data.target
    train, test = train_test_split(df, test_size=0.3,random_state = 40)
    stat, p, dof, expected = chi2_contingency(df)
    # interpret test-statistic
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
    if abs(stat) >= critical:
        print('There is a drift (reject H0)')
    else:
        print('There is no drift (fail to reject H0)')
    # interpret p-value
    alpha = 1.0 - prob
    print('significance=%.3f, p=%.3f' % (alpha, p))
    if p <= alpha:
        print('There is a drift (reject H0)')
    else:
        print('There is no drift (fail to reject H0)')
            
        return str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Species Identification
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))  



    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)