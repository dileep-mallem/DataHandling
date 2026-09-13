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
df["date"] = pd.to_datetime(df["date"])
df["year"]  = df["date"].dt.year


# Memory Efficent Dtypes 

#dtype="category" - massive memeory dsavings for low=crdinality strings
df["dept"]=df["dept"].astype("category")
print(df["dept"].cat.categories) # Index(['CS', 'EE', 'ME'], dtype='object')
print(df["dept"].cat.codes)
# 0    0
# 1    1
# 2    0
# 3    2
# dtype: int8

# Reduce Memory by Down-casting NUmric Memory Types 
df["age"]=pd.to_numeric(df["age"],downcast="integer") # int64 -> int8
df["score"]=pd.to_numeric(df["score"],downcast="float") #float64 -> float32

# check memory before and After 
print(df.memory_usage(deep=True)) # bytes per Col
# Index     128
# name      249
# age         4
# score      16
# passed    132
# dept      289
# date       32
# dtype: int64
print(df.memory_usage(deep=True).sum()/1024**2) # 0.0008106231689453125 -> Total MB



# 2. Views vs Copies
print("\nViews vs Copies \n") 

# Slicing with .loc often returns a view (modifying it changes the original)
# Boolean indexing always returns a copy
# The SettingWithCopyWarning signals you might be operating on a copy

# WRONG — may not modify original
subset=df[df["score"]>70]
subset["grade"]="Pass" # SettingWithCopyWarning

# CORRECT — use .loc on the original
df.loc[df["score"]>70,"grade"]="Pass"
print(df)

# CORRECT — explicit copy when you want independence
subset=df[df["score"]>70].copy()
subset["grade"]="Pass" # safe — operates on the copy



# Efficient Iteration 
print("\nEfficient Iteration \n")

# Slow 
for idx,row in df.iterrows() :
    # print(idx,row)
    df.loc[idx,"result"]=row["score"]*1.1

# FAST Vectorizatiokn 
df["result"]=df["score"]*1.1

# itertuples -> faster than iterrows() when you you must iterate 
for row in df.itertuples(index=False) : #  index : bool, default True ,If True, return the index as the first element of the tuple.
    print(row.name,row.score)
# Dileep 88.5
# Priya 74.0
# Ravi nan
# Ananya 91.19999694824219

# FASTEST bult computation - to_numpy() then NUnmPY 
arr=df[["score","age"]].to_numpy()
result=arr[:,0]*0.8 + arr[:,1]*0.2
print(df)
#   name  age      score passed dept       date grade      result
# 0  Dileep   21  88.500000   True   CS 2026-01-01  Pass   97.349998
# 1   Priya   20  74.000000   True   EE 2026-01-02  Pass   81.400002
# 2    Ravi   22        NaN   None   CS 2026-01-03   NaN         NaN
# 3  Ananya   21  91.199997   True   ME 2026-01-04  Pass  100.320000


# 4 . MultiIndex 
print("\nMultiINdex\n")

# MultiIndex — hierarchical indexing for complex grouped data
arrays=[["CS","CS","EE","EE"],[2023,2024,2023,2024]]
midx=pd.MultiIndex.from_arrays(arrays,names=["dept","year"])
s=pd.Series([88,91,75,78],index=midx)

print("\n",s["CS"]) # all CS rows
# year
# 2023    88
# 2024    91
# dtype: int64
print("\n",s["CS",2023]) # 88
print("\n",s.unstack()) # Convert Inner Index to cols 
# year  2023  2024
# dept            
# CS      88    91
# EE      75    78
print("\n",midx)
# MultiIndex([('CS', 2023),
#             ('CS', 2024),
#             ('EE', 2023),
#             ('EE', 2024)],
#            names=['dept', 'year'])


# groupby naturally creates MultiIndex results
result=df.groupby(["dept","year"])["score"].mean()
print("\n",result)
# dept  year
# CS    2026    88.500000
# EE    2026    74.000000
# ME    2026    91.199997
# Name: score, dtype: float32
print("\n",result.reset_index())  # flatten MultiIndex back to columns
#   dept  year      score
# 0   CS  2026  88.500000
# 1   EE  2026  74.000000
# 2   ME  2026  91.199997

# 5.PipeLine Pattern (Used in SKLEARN Integration)
print("\nPipeLine Pattern")

result=(
    pd.read_csv("Pandas/students.csv")
    .drop_duplicates()
    .dropna(subset=["attendance_rate"])
    .assign(
        avg = lambda df : (df["math_score"] + df["science_score"] + df["english_score"])/3,
        passed = lambda df: df["avg"] >= 60,
        adult = lambda df : df["age"]>18
    )
    .query("passed == True") # Only Passed Students
    .sort_values("avg",ascending=False)
    .reset_index(drop=True)
)
print(result)
#   student_id             name  age gender  grade_level  math_score  science_score  english_score attendance_rate  passed        avg  adult
# 0         110       Ava Thomas   17      F           12       100.0           98.0           99.0             99%    True  99.000000  False
# 1         101       Liam Smith   15      M           10        88.0           92.0           85.0             95%    True  88.333333  False
# 2         108  Isabella Taylor   16      F           11        83.0           85.0           87.0             91%    True  85.000000  False
# 3         105    Oliver Miller   16      M           11        72.0           75.0           70.0             85%    True  72.333333  False


