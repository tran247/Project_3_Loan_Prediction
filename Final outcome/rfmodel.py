# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler

def loan():
    #read file
    train_df = pd.read_csv("input/updated_csv.csv")
    X =train_df.drop("Loan_Status", axis=1)
    y_df= train_df['Loan_Status']
    X["Dependents"] = X["Dependents"].astype(float)
    #Use Dummy Encoding to transform each categorical feature into new columns 
    X_dummies= pd.get_dummies(X[["Gender", "Married", "Education",'Self_Employed']])
    #Drop duplicate columns

    data_1= X_dummies.drop(columns=['Gender_Female','Married_No','Education_Graduate','Self_Employed_No'])
    #Replace string value in property Area to numerical values
    X['Property_Area'] = X['Property_Area'].replace(to_replace=['Semiurban'], 
                                                value= 0, regex= True)
    X['Property_Area'] = X['Property_Area'].replace(to_replace=['Urban'], 
                                                value= 1, regex= True)
    X['Property_Area'] = X['Property_Area'].replace(to_replace=['Rural'], 
                                                value= 2, regex= True)
    X['Property_Area'].value_counts()
    X_df= pd.concat([X, data_1], axis=1)
    #drop duplicate columns
    X_df= X_df.drop(columns=['Gender','Married','Education','Self_Employed'])

    X_df["Dependents"] = X_df["Dependents"].astype(float)
    feature_names = X_df.columns
    y= pd.get_dummies(y_df)
    y= y.drop(columns=['N'])
    y= y.values.reshape(-1, 1)
    target_names = ["Yes", "No"]
    #Split data into training and testing data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_df, y, random_state=42)
    from sklearn.preprocessing import StandardScaler

    # Create a StandardScater model and fit it to the training data
    X_scaler = StandardScaler().fit(X_train)

    # Transform the training and testing data using the X_scaler
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    #create random forest model
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=200)
    rf = rf.fit(X_train_scaled, y_train)
    rf.score(X_test_scaled, y_test)
    #Look at column that affect model result
    sorted(zip(rf.feature_importances_, feature_names), reverse=True)
    import pickle

    filename = 'finalized_model.sav'

    pickle.dump(rf, open(filename, 'wb'))
    
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    # result = loaded_model.score(X_test_scaled, y_test)
    