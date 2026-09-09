import pandas as pd 
import numpy as np 

# Reading Cv 

df=pd.read_csv("Pandas/students.csv")
print(df)

#check after loading 
print(df.shape) #(10,10)

print(df.dtypes) 
# student_id           int64
# name                object
# age                  int64
# gender              object
# grade_level          int64
# math_score         float64
# science_score      float64
# english_score      float64
# attendance_rate     object
# passed                bool
# dtype: object

print(df.isnull().sum())   # missing values per column
# student_id         0
# name               0
# age                0
# gender             0
# grade_level        0
# math_score         1
# science_score      1
# english_score      1
# attendance_rate    1
# passed             0
# dtype: int64
print(df.duplicated().sum())  # 0 # duplicate rows 


# Most Imp Parameters 
df = pd.read_csv(
    "data.csv",
    index_col="id",          # use 'id' column as the index
    usecols=["name","score"],  # only load these columns (saves memory)
    dtype={"score": float},   # force column dtype
    na_values=["N/A","-"],    # extra strings to treat as NaN
    parse_dates=["date"],     # auto-parse date columns
    nrows=1000,               # only read first 1000 rows
    skiprows=[1,2],           # skip specific rows
    encoding="utf-8",         # handle non-ASCII files
    sep=";",                  # delimiter (default ",")
)

#writing 
df.to_csv("output.csv", index=False)   #don't write index as column
df.to_json("output.json", orient="records")
df.to_excel("output.xlsx", sheet_name="Data")

# Other read functions 
pd.read_json("data.json")
pd.read_excel("data.xlsx", sheet_name="Sheet1")
pd.read_sql("SELECT * FROM table", connection) # type: ignore
pd.read_parquet("data.parquet")         # fast columnar format

