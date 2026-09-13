import pandas as pd 
import numpy as np 

df = pd.DataFrame({
    "name":   ["Dileep", "Priya", "Ravi", "Ananya"],
    "age":    [21, 20, 22, 21],
    "score":  [88.5, 74.0, np.nan, 91.2],
    "passed": [True, True, None, True]
})
# Creates consecutive daily dates starting from Jan 1, 2026
df['date'] = pd.date_range(start='2026-01-01', periods=len(df), freq='D')


# Duplicated Rows 
df.duplicated() # True for Duplicated Rows 
df.drop_duplicates() # Remove Exact Duplicates 

df.duplicated(subset=["name","score"]) # Cheack ONly These Rows 
df.drop_duplicates(subset=["name"],keep="last") # keep Last , "first" -> keep First 

# Dtype Conversion 
print("\nDtype Conversion\n")

df["age"].astype(float)
print(df["passed"].astype(bool))
# 0     True
# 1     True
# 2    False
# 3     True
# Name: passed, dtype: bool

pd.to_numeric(df["score"],errors="coerce") # invlid -> NaN (safe conversion)
pd.to_datetime(df["date"],format="%Y-%m-%d")

# String Cleaning 


df["name"].str.strip() # Remove leading/traling Spcae
df["name"].str.title()
df["name"].str.replace(r"\s+"," ",regex=True)  # collapse spaces

# Outlier Detection and Capping 
print("\nOutlier detection and capping\n")

q1=df["score"].quantile(0.25)
q3=df["score"].quantile(0.75)

iqr=q3-q1 
lower,upper = q1 - 1.5*iqr , q3 + 1.5*iqr 
df_clean=df[(df["score"] >= lower) & (df["score"] <= upper)]
print(df_clean)

#      name  age  score passed       date
# 0  Dileep   21   88.5   True 2026-01-01
# 1   Priya   20   74.0   True 2026-01-02
# 3  Ananya   21   91.2   True 2026-01-04

# Complete Cleaning Pieline 
print("\nComplete Cleaning PipeLine\n")

def clean_df(df) : 
    df=df.copy()

    df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
    df=df.drop_duplicates()
    df["score"]= pd.to_numeric(df["score"], errors="coerce")
    df["score"]=df["score"].fillna(df["score"].median())
    df["name"]=df["name"].str.strip().str.title()
    return df
c=clean_df(df)
print(c)
#      name  age  score passed       date
# 0  Dileep   21   88.5   True 2026-01-01
# 1   Priya   20   74.0   True 2026-01-02
# 2    Ravi   22   88.5   None 2026-01-03
# 3  Ananya   21   91.2   True 2026-01-04