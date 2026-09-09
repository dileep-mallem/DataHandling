import pandas as pd 
import numpy as np
# DF -> A Data Frame iS a 2-D labelled Table- Like a Spread Sheet or SQL Table .
# Each Column is a Series a Sharies the SamE INdex , Primary Pandas Object .


# Creation 
df=pd.DataFrame({
    "name" :["Dileep Kumar","Jon Snow","Thor","Sonny Hayes"],
    "age":[20,30,1500,53],
    "score":[88.5,74.0,np.nan,91.2],
    "passed":[True,True,None,True]
})

print(df)

# From list of Dicts 
df2=pd.DataFrame([
    {"name":"x","val":1},
    {"name":"y","val":2}
])
print("\n",df2)

# Key Attributes 

df.shape        # (4, 4)   — rows × cols
df.dtypes       # dtype of each column
df.columns      # Index(['name','age','score','passed'])
df.index        # RangeIndex(start=0, stop=4, step=1)
df.info()       # shape + dtypes + non-null counts + memory
df.describe()   # stats for numeric columns
df.head(3)      # first 3 rows
df.tail(2)      # last 2 rows
df.sample(2)    # 2 random rows

print(f"\n Shape : {df.shape}\n Data Types : {df.dtypes}\n Columns : {df.columns} \n ")
print(f"\nIndex :\n {df.index} \n Info : {df.info()} \n Describe : \n {df.describe()} \n")
print(f"Head : {df.head(3)} \nTail \n: {df.tail(2)} \nSample \n: {df.sample(2)}")


# Column Access 
print("\n\n\n Column Access")

print(df["name"])
# 0    Dileep Kumar
# 1        Jon Snow
# 2            Thor
# 3     Sonny Hayes
# Name: name, dtype: object
print(df[["name","score"]])
#            name  score
# 0  Dileep Kumar   88.5
# 1      Jon Snow   74.0
# 2          Thor    NaN
# 3   Sonny Hayes   91.2

print(df.name)  # same as df["name"] — attribute style (avoid for ambiguous names)


# Adding / Removing Colmns / Renaming  

df["grade"]=["A","B","F","A+"] # add Column 
print("\n",df)

df["scaled"]=df["score"]/100 # Derived Column -> Derived by Using Another COlumn 
print("\n",df)

df=df.drop(columns=["scaled"]) # Removing Columns 
print("\n",df)

df=df.rename(columns={"name":"Name","grade":"Grade"})
print("\n",df)

# Updating 

df.loc[2,"Name"]="Thor Odinson"
print(df.loc[2,"Name"]) # Thor Odinson 

# Accesing


print(df.loc[1])
# Name      Jon Snow
# age             30
# score         74.0
# passed        True
# Grade            B
# Name: 1, dtype: object

print(df.loc[1:3,["Name","Grade"]]) # Stop -> Inclusive
#            Name Grade
# 1      Jon Snow     B
# 2  Thor Odinson     F
# 3   Sonny Hayes    A+

