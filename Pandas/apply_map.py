import pandas as pd 
import numpy as np 

import pandas as pd 
import numpy as np 

df = pd.DataFrame({
    "name":   ["Dileep", "Priya", "Ravi", "Ananya"],
    "age":    [21, 20, 22, 21],
    "score":  [88.5, 74.0, np.nan, 91.2],
    "passed": [True, True, None, True],
    "dept": ["CS","EE","CS","ME"]
})
df['date'] = pd.date_range(start='2026-01-01', periods=len(df), freq='D')

# apply on Series - Element Wise 
df["grade"]=df["score"].apply(lambda x :
                              "A+" if x>=90 else "A" if x>=80 else "B" if x>=70 else "C")

print(df)
#      name  age  score passed       date grade
# 0  Dileep   21   88.5   True 2026-01-01     A
# 1   Priya   20   74.0   True 2026-01-02     B
# 2    Ravi   22    NaN   None 2026-01-03     C
# 3  Ananya   21   91.2   True 2026-01-04    A+

# Apply on DataFrame - along axis 
# df.apply(lambda col : col.max() -col().min(),axis=0)  # Range per Col
# df.apply(lambda row : row["score"] * 0.8 + row["bonus"],axis=1)

# map - Series ONly (elements Wise)
df["dept_code"]=df["dept"].map({"CS":1,"EE":2,"ME":3})

#  vectorized alternative — MUCH faster than apply
# Use numpy/pandas vectorized ops whenever possible
# apply() is slow because it calls Python function N times

df["pass/fail"]=(df["score"]>=50).map({True : "pass",False :"Fail"})

# numpy where — fastest conditional assignment
df["result"]=np.where(df["score"]>=50,"Pass","Fail")

#  pd.cut — bin continuous values
df["band"]=pd.cut(df["score"],
                  bins=[0,50,70,85,100],
                  labels=["F","C","B","A"],
                  include_lowest=True)
print(df)

#      name  age  score passed dept       date grade  dept_code pass/fail result band
# 0  Dileep   21   88.5   True   CS 2026-01-01     A          1      pass   Pass    A
# 1   Priya   20   74.0   True   EE 2026-01-02     B          2      pass   Pass    B
# 2    Ravi   22    NaN   None   CS 2026-01-03     C          1      Fail   Fail  NaN
# 3  Ananya   21   91.2   True   ME 2026-01-04    A+          3      pass   Pass    A
