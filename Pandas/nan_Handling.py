import pandas as pd
import numpy as np

# Missing Data is Represented as NaN(float) or np.nan or None dependending on dtyep .
# Never Use ==np.nan to check , ALways Use isna() or isnull()

# Never use df["score"] == np.nan.
# NaN is not equal to anything — even itself. 
# This always returns False.
# Always use df["score"].isna() or pd.isna(val)


df=pd.DataFrame({
    "Name" : ["Alice","Bob",np.nan , "David","Eva"],
    "Age"  : [25,np.nan,30,22,28],
    "Score" : [85,90,78,np.nan,92]
})

print(df)

# Detecting Null Values
print("\nDetecting Null Values\n")

df.isnull() # bollean DataFrame - True where NaN 
print(df.isnull().sum()) # Count of NaN per Column 
# Name     1
# Age      1
# Score    1
# dtype: int64

print(df.isnull().sum().sum()) # 3 -> Total NaN Count
df.notnull() # True where not NAN

print(df["Score"].isna()) # or isnull()
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# Name: Score, dtype: bool


# Dropping Missing Values
print("\nDropping Missing Values")

df.dropna() # drop rows with any NAN
df.dropna(how="all") # drop where All values are Nan 
df.dropna(how="any") # Drop row if any Val is NAn 
df.dropna(axis=1) # drop coulmns with anu Nan 
df.dropna(thresh=3) # keep rows with atleast 3-non Nan

# Filling Missing Values 
print("\n Filling Missing Values\n")

df.fillna(0) # replace all Nan with 0
df["Score"]=df["Score"].fillna(df["Score"].mean())
print(df["Score"])
# 0    85.00
# 1    90.00
# 2    78.00
# 3    86.25 -> Changed 
# 4    92.00
# Name: Score, dtype: float64

df=df.fillna({"Age":18,"Name":"Unknown"}) # Diff fill per col
print(df)
#       Name   Age  Score
# 0    Alice  25.0  85.00
# 1      Bob  18.0  90.00
# 2  Unknown  30.0  78.00
# 3    David  22.0  86.25
# 4      Eva  28.0  92.00
 

# Forward and Backward Fill -> Useful for Time Series : Fill Gaps with Last Unknow Value

print("\n FOrward and Backward Fill\n")

# df.ffill()   -> Forward Fill : Copy Previous Values , prev ROw
# df.bfill()   -> Backward Fill : Copy Next values , next row 

data =pd.DataFrame( {
    'Date': ['2026-09-01', '2026-09-02', '2026-09-03', '2026-09-04', '2026-09-05'],
    'Price': [100, np.nan, 105, np.nan, 110]
})
df_ffill=data.ffill()
print(df_ffill)
#          Date  Price
# 0  2026-09-01  100.0
# 1  2026-09-02  100.0
# 2  2026-09-03  105.0
# 3  2026-09-04  105.0
# 4  2026-09-05  110.0

df_bfill=data.bfill()
print(df_bfill)
#          Date  Price
# 0  2026-09-01  100.0
# 1  2026-09-02  105.0
# 2  2026-09-03  105.0
# 3  2026-09-04  110.0
# 4  2026-09-05  110.0

# InterPolation 
df["Score"].interpolate(method="linear") # Fill NaN by Linaer Interpretatiojn

# Replace Specific Values 
df.replace(-999,np.nan) # sentinel -> nan 
df["Grade"].replace({"A":4,"B":3,"C":2}) # map Values 
