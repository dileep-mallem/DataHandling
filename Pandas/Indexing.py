import pandas as pd 
import numpy as np 

# Pandas used uses two Indeexres : .loc[] -> Lable Based and .iloc[] -> Position based 

# df.loc[rows,cols] , Lables[indedx values , column Names ] , slice end(Incl) , df.loc[0:3,"name":score]
# df.iloc[rows,cols] , integer posiontions (0 based) , slice ned(exl) , df.iloc[0:3,1:3]

# df.loc[col] , col name only 
# df[bool_mask] , Boolean Series , df[df["score"]>80]

df=pd.DataFrame({
    "name":["A","B","C","D"],
    "score":[85,72,90,60],
    "dept":["CS","EE","CS","ME"]
})

print("DataFrame \n",df)
print()
# loc : label Based 

print(df["name"]) # can only one Column 

print(df.loc[1:3])
#  name  score dept
# 1    B     72   EE
# 2    C     90   CS
# 3    D     60   ME

print(df.loc[0:3:2,["name","dept"]])
#   name dept
# 0    A  CSE
# 2    C   CS

print(df.loc[0:3,"score":"dept"])
#    score dept
# 0     85  CSE
# 1     72   EE
# 2     90   CS
# 3     60   ME

# iloc[] -> Position Based 
# Lets get smae above 

# for df["name"]
print(df.iloc[:,0])
# 0    A
# 1    B
# 2    C
# 3    D
# Name: name, dtype: object

print(df.iloc[0:3,0:2])
#  name  score
# 0    A     85
# 1    B     72
# 2    C     90

print(df.iloc[-1])  # last row
# name      D
# score    60
# dept     ME
# Name: 3, dtype: object

print(df.iloc[0,1]) # 1st row , 2nd col # 85 

# Boolean Masking 

print(df[df["score"]>80])
#   name  score dept
# 0    A     85  CSE
# 2    C     90   CS

print(df[(df["score"]>70) & (df["dept"]=="CS")]) # AND , for OR |
#   name  score dept
# 0    A     85   CS
# 2    C     90   CS

print(df[df["dept"].isin(["CS","EE"])]) # isin Filter
#   name  score dept
# 0    A     85   CS
# 1    B     72   EE
# 2    C     90   CS
print(df[~(df["score"]<70)]) # NOT 
#   name  score dept
# 0    A     85   CS
# 1    B     72   EE
# 2    C     90   CS

# Print Only names for condition
print(df["name"][df["score"]>80])
# 0    A
# 2    C
# Name: name, dtype: object

print(df.loc[:,["name","dept"]][df["score"]>80]) # Accesing[Boolean_mask]
#   name dept
# 0    A   CS
# 2    C   CS
