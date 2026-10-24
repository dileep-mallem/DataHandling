import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv(r'C:\Users\Mr.Dileep Kumar\Desktop\DataHandling\Matplotlib_visualization\projects\sales_data.csv')

df["revenue"] = df['units_sold'] * (df['unit_price'] *(100- df['discount_pct']) / 100 ).round(2)
df['date']=pd.to_datetime(df['date'])
df['month']=df['date'].dt.month # int 
# df['month']=df['date].dt.month_name() -> str 

monthly=df.groupby('month',as_index=False)["revenue"].sum()

def plot1(ax):
    sns.lineplot(
        data=df,
        x="month",
        y="revenue",
        marker="o",
        linewidth=2.5,
        ax=ax
    )

    ax.set_title("Monthly Revenue Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")


# Display the individual plot
fig, ax = plt.subplots(figsize=(10, 5))
plot1(ax)
plt.tight_layout()
plt.show()

def plot2(ax):
    sns.barplot(
        data=df,
        x="category",
        y="revenue",
        ax=ax
    )

    ax.set_title("Revenue by Category")


# Display the individual plot
fig, ax = plt.subplots(figsize=(10, 5))
plot2(ax)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(2,1, figsize=(18, 10))

plot1(ax[0])  # First row, first column
plot2(ax[1])  # First row, second column


plt.tight_layout()
plt.savefig("combined_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()