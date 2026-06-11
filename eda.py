import  pandas as pd

import pandas as pd

df = pd.read_csv("titanic.csv")

print("FIRST 5 RECORDS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSTATISTICS")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nTOTAL PASSENGERS")
print(len(df))

print("\nSURVIVAL COUNT")
print(df["Survived"].value_counts())

print("\nAVERAGE AGE")
print(df["Age"].mean())

print("\nSURVIVAL BY GENDER")
print(df.groupby("Sex")["Survived"].mean())