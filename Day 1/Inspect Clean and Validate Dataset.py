Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import codecademylib3
import pandas as pd
import numpy as np
# code goes here
df=pd.read_csv("diabetes.csv")
print(df.head())
print(len(df.columns)) #check Columns
print(df.shape) #check rows and columns
print(len(df)) #check columns only
print(df.info()) #getting summary
print(df.isnull().sum()) #check if value in the dataset is null
print(df.describe())
df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
print(df.isnull().sum())
print(df.info())
print(df[df.isnull().any(axis=1)]) #Print out all of the rows that contain missing (null) values.
print(df.dtypes) #print data types of each column
print(df.Outcome.unique())