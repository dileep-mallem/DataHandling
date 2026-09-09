# A series a 1-D like Array - like One column of a spreadsheet.
# Every Column of an Data Frame is an Series 

import pandas as pd 
import numpy as np 

# Creating A Series 

s1=pd.Series([10,20,30,40]) # Default Indesic : 0 1 2 3 
print(s1)
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

s2=pd.Series([10,20,30],index=["a","b","c"]) # Custom Index 
print(s2)
# a    10
# b    20
# c    30
# dtype: int64

# From Dictionaries 

s3=pd.Series({"x":1.5,"y":2.5,"z":3.5})
print(s3)
# x    1.5
# y    2.5
# z    3.5
# dtype: float64

# From NumPy array 
s4=pd.Series(np.random.randn(5),name="scores") # .randn() -> Return a sample (or samples) from the "standard normal" distribution.
print(s4)
# 0    1.391828
# 1    0.069542
# 2    0.282207
# 3   -0.467504
# 4   -1.418883
# Name: scores, dtype: float64

# Key Attributes 
print(s2.index) # Index(['a', 'b', 'c'], dtype='object')
print(s3.values) # [1.5 2.5 3.5]
print(s4.dtype) # float64
print(s2.shape) # (3,)
print(s1.name)  # None(unnamed)

# Indexing 

print(s2["b"]==s2[1]) # True
print(s2.iloc[0]) # 10
print(s2.loc["a"]) # 10 

# Vectorized Operations 

print(s2*2)
print(s2[s2>10])
s=s2[s2>s2.mean()]
print(s2.mean()," Values above Global Mean : ",s) # 20.0  Values above Global Mean :  c    30
print(s2.describe())
# count     3.0
# mean     20.0
# std      10.0
# min      10.0
# 25%      15.0
# 50%      20.0
# 75%      25.0
# max      30.0
# dtype: float64