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
