import pandas as pd 

# Folows , split -> apply -> Combine 
# Split Data intoGropus by a key , apply a function to each group 
#   combine results back into a DataFrame 

df=pd.DataFrame({
    "dept":["CS","EE","CS","EE","CS"],
    "name":["A","B","C","D","E"],
    "score":[85,72,90,68,78],
    "year":[2,2,3,3,2],
})

print("\nDataFrame\n",df,"\n")

# groupby -> Split -> Apply Fun -> Combine

# Basic Aggregation 

print(df.groupby("dept")["score"].mean())
# dept
# CS    84.333333
# EE    70.000000
# Name: score, dtype: float64

# Multiple Aggs

x=df.groupby("dept").agg(
    avg_score=("score","mean"),
    max_score=("score","max"),
    count=("name","count")
)
print(x)
#  avg_score  max_score  count
# dept                             
# CS    84.333333         90      3
# EE    70.000000         72      2

# Transform -> returns same shape as Input 

df["dept_avg"]=df.groupby("dept")["score"].transform("mean")
df["above_avg"]=df["score"]>df["dept_avg"]
print(f"\n{df}\n")
#   dept name  score  year   dept_avg  above_avg
# 0   CS    A     85     2  84.333333       True
# 1   EE    B     72     2  70.000000       True
# 2   CS    C     90     3  84.333333       True
# 3   EE    D     68     3  70.000000      False
# 4   CS    E     78     2  84.333333      False

# filter 

print(df.groupby("dept").filter(lambda g : g["score"].mean()>75))
#   dept name  score  year   dept_avg  above_avg
# 0   CS    A     85     2  84.333333       True
# 2   CS    C     90     3  84.333333       True
# 4   CS    E     78     2  84.333333      False


# apply 
def top_student(group) : 
    return group.nlargest(1,"score")
x=df.groupby("dept").apply(top_student,include_groups=False) # include_groups=False -> To silence (FutureWarning) Warning 
print(x)
#        dept name  score  year   dept_avg  above_avg
# dept                                               
# CS   2   CS    C     90     3  84.333333       True
# EE   1   EE    B     72     2  70.000000       True

# or
 
# Select only the columns needed for the calculation + the group if needed
x=df.groupby("dept")[["name","score"]].apply(top_student)
print(x)
# dept              
# CS   2    C     90
# EE   1    B     72

# Iterate Over Groups 

for dept,group_df in df.groupby("dept") :
    print(f" {dept} : {group_df['score'].mean():.1f}")

#  CS : 84.3
#  EE : 70.0