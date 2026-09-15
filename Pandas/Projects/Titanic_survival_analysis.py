import pandas as pd 
import numpy as np

# Load and First Look 

df = pd.read_csv("/home/dileep-kumar/Desktop/Data/Pandas/titanic.csv")
print(f"Shape : {df.shape} \n ")
print(f"Dtypes : \n{df.dtypes} \n")
print(f"Null Counts : \n {df.isnull().sum()} \n\nTotal Null Count {df.isnull().sum().sum()} \n")
print(f"Description : \n{df.describe()}\n")
print(f"Value Counts : \n {df['Sex'].value_counts()} \n") # Freq of Each Value 


# Data Cleaning 

df["Age"]=df["Age"].fillna(df["Pclass"].median())
df["Embarked"]=df["Embarked"].fillna(df["Pclass"].mode())
df.drop(columns="Cabin") #  df.drop(columns="Cabin") only returns a temporary copy 
# 1. df=df.drop(columns="Cabin")
# 2 . df.drop(columns="Cabin", inplace=True)
df["Title"]=df["Name"].str.extract(r',\s*([^\.]+)\.')


# Feature Engineering 

df["FamilySize"]=df["SibSp"]+df["Parch"] + 1 
df["AgeGroup"]=pd.cut(df["Age"],
                      bins=[0,12,18,35,60,100],
                      labels=["Child","Teen","Adult","Middle","Senior"])

# groupby Analysis 
print(df.groupby(["Pclass","Sex"])["Survived"].mean().unstack())
# Sex       female      male
# Pclass                    
# 1       0.968085  0.368852
# 2       0.921053  0.157407
# 3       0.500000  0.135447
print("\n\n")
print(df.groupby("AgeGroup")["Survived"].agg(["mean","count","sum"]))
#              mean  count  sum
# AgeGroup                      
# Child     0.373984    246   92
# Teen      0.428571     70   30
# Adult     0.382682    358  137
# Middle    0.400000    195   78
# Senior    0.227273     22    5

# Merge - Join Passenger with Cabin Data 
# Create a separate DataFrame of passengers with cabin info (non-NaN Cabin rows).
# Merge back and compare survival rates of cabin-holders vs non-holders.

cabin_df=df.dropna(subset=["Cabin"])[["PassengerId","Cabin"]].copy() # np.array(subset)[check].tolist())
df=pd.merge(df,cabin_df,on="PassengerId", how="left", suffixes=("","_known"))

# Summary 
top3=df.groupby(["Pclass","Sex","AgeGroup"])["Survived"].mean().nlargest(3)
print(f"Total Paseengers : {df.shape[0]}") # or len(df)
print(f"Overall survival: {df['Survived'].mean():.1%}")
print(top3)

# Total Paseengers : 891
# Overall survival: 38.4%
# Pclass  Sex     AgeGroup
# 1       female  Teen        1.0
#                 Senior      1.0
# 2       female  Child       1.0
# Name: Survived, dtype: float64
