import pandas as pd 

students = pd.DataFrame({
    "id" : [1,2,3,4],
    "name":["A","B","C","D"],
    "dept_id":[10,20,10,30]
})

depts=pd.DataFrame({
    "dept_id":[10,20],
    "dept_name":["CS","EE"]
})

# merge -> like SQL join 
print(pd.merge(students,depts,on="dept_id",how="inner"))
# how: "inner" (default), "left", "right", "outer"
# inner: only matching keys  (A,B,C  — D dropped, no dept 30)

#    id name  dept_id dept_name
# 0   1    A       10        CS
# 1   2    B       20        EE
# 2   3    C       10        CS


# left:  all left rows       (A,B,C,D — D's dept_name is NaN)
print(pd.merge(students,depts,on="dept_id",how="left"))
#    id name  dept_id dept_name
# 0   1    A       10        CS
# 1   2    B       20        EE
# 2   3    C       10        CS
# 3   4    D       30       NaN
print(pd.merge(students,depts,on="dept_id",how="right"))
#    id name  dept_id dept_name
# 0   1    A       10        CS
# 1   3    C       10        CS
# 2   2    B       20        EE
# outer: all rows from both
print(pd.merge(students,depts,on="dept_id",how="outer"))
#    id name  dept_id dept_name
# 0   1    A       10        CS
# 1   3    C       10        CS
# 2   2    B       20        EE
# 3   4    D       30       NaN

df1,df2=students,depts
# Merge on two diff Cols names 
print(pd.merge(df1,df2,left_on="id",right_on="dept_id"))
# Empty DataFrame
# Columns: [id, name, dept_id_x, dept_id_y, dept_name]
# Index: []

# Concat - stack DataFrames vertically or hor
c1=pd.concat([df1,df2],axis=0,ignore_index=True) # stack Rows 
print(c1)
#     id name  dept_id dept_name
# 0  1.0    A       10       NaN
# 1  2.0    B       20       NaN
# 2  3.0    C       10       NaN
# 3  4.0    D       30       NaN
# 4  NaN  NaN       10        CS
# 5  NaN  NaN       20        EE
c2=pd.concat([df1,df2],axis=1)
print(c2)
#    id name  dept_id  dept_id dept_name
# 0   1    A       10     10.0        CS
# 1   2    B       20     20.0        EE
# 2   3    C       10      NaN       NaN
# 3   4    D       30      NaN       NaN

# pivot and melt - reshape 

# pivot : long -> wide 
df = pd.DataFrame({
    "dept":   ["CS","EE","CS","EE","CS"],
    "name":   ["A","B","C","D","E"],
    "score":  [85,72,90,68,78],
    "year":   [2,2,3,3,2],
})
df["bonus"]= df["score"] * 0.1 + 5
df=df.pivot_table(index="dept",columns="year",values="score",aggfunc="mean")
print(df)
# year     2     3
# dept            
# CS    81.5  90.0
# EE    72.0  68.0

# melt : wide -> long 

df=pd.melt(df,id_vars=["name"],value_vars=["score","bonus"])
print(df)


