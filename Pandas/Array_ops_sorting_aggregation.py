import pandas as pd 


df=pd.DataFrame({
    "Name" : ["Jai","Ojas","Sanjay Saahu","Balu"],
    "Age" : [30,45,28,25],
    "Score" :[56,85,95,100]
})

print(df)
# Arithmetic -> Vectorized , No loops needed 
df["Score_scaled"]=df["Score"]/100
df["Bonus"]=df["Score"] * 0.1 + 5

print("\n After adding Columns \n",df)


# String Op's Thorgh .str Accessor
print("\n\nString Op's Thorgh .str Accessor\n") 

print(df["Name"].str.upper()) # have other .str methods also 

# print(df) -> Doesnt Change orginal DF , until you Chnage it as df["name"]=df["Name"].str.upper()

print(df["Name"].str.contains("Ja",case=False)) # def : True -> only checks Starting , False Checks Total String or Value
# 0     True
# 1     True
# 2     True
# 3    False
# Name: Name, dtype: bool
print(df["Name"].str.contains("Ja"))
# 0     True
# 1    False
# 2    False
# 3    False
# Name: Name, dtype: bool

print(df["Name"].str.len()) # Returns length of each value in Name column
print(df["Name"].str.strip().str.title())
# 0             Jai
# 1            Ojas
# 2    Sanjay Saahu
# 3            Balu
# Name: Name, dtype: object



# DataTime Op's via .dt Accessor
print("\n\nDataTime Op's via .dt Accessor \n")
df["Date"]=["2023-01-15", "2022-06-20", "2024-11-05", "2021-03-12"]

df["Date"]=pd.to_datetime(df["Date"])
print(df)

# .dt Accessor
df["Year"]=df["Date"].dt.year
df["Month_Name"]=df["Date"].dt.strftime("%B")
df["Day_Name"]=df["Date"].dt.day_name()

print("\n",df,"\n")
#             Name  Age  Score  Score_scaled  Bonus       Date  Year Month_Name Day_Name
# 0           Jai   30     56          0.56   10.6 2023-01-15  2023    January   Sunday
# 1          Ojas   45     85          0.85   13.5 2022-06-20  2022       June   Monday
# 2  Sanjay Saahu   28     95          0.95   14.5 2024-11-05  2024   November  Tuesday
# 3          Balu   25    100          1.00   15.0 2021-03-12  2021      March   Friday 



# Sorting
print("\n\nSorting \n")

df=df.sort_values("Age",ascending=False) # Desscending , def : True 
print(df)

print(df.sort_values(["Score","Year"],ascending=[False,True])) # Doesn;t change Orginal , Now ,(No df=)
#            Name  Age  Score  Score_scaled  ...       Date  Year  Month_Name Day_Name
# 3          Balu   25    100          1.00  ... 2021-03-12  2021       March   Friday
# 2  Sanjay Saahu   28     95          0.95  ... 2024-11-05  2024    November  Tuesday
# 1          Ojas   45     85          0.85  ... 2022-06-20  2022        June   Monday
# 0           Jai   30     56          0.56  ... 2023-01-15  2023     January   Sunday

# [4 rows x 9 columns]

df.sort_index() # Sort by Row Index




# Value Counts / Unique
print("\n\nValue Counts and Unique\n")

print(df["Age"].value_counts()) # Frequency of each Value
# Age
# 45    1
# 30    1
# 28    1
# 25    1
# Name: count, dtype: int64

print(df["Year"].nunique()) # 4  ->  No of Unique Values
print(df["Age"].unique()) # [45 30 28 25] -> Array of Unique Value


# Aggregation 
print("\n\nAggregation\n")

print(df["Age"].mean()) # 32.0 # .median() , .mode() , .var() .std() 

# Multiple Aggs at a time 
print(df.agg({"Age":["mean","max","min","sum","values"]}))
#         Age
# mean   32.0
# max    45.0
# min    25.0
# sum   128.0
# values  [45, 30, 28, 25]