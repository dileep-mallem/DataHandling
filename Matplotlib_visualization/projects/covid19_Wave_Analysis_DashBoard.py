import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


np.random.seed(42)
DAYS = 540   # ~18 months of data
t    = np.arange(DAYS)

# Generate synthetic epidemic waves
def make_wave(peak_day, height, width):
    """Gaussian wave shape"""
    return height * np.exp(-((t - peak_day)**2) / (2 * width**2))

def make_country(wave_params, noise_scale):
    signal = sum(make_wave(*p) for p in wave_params)
    noisy  = np.random.poisson(np.clip(signal, 0, None))
    return noisy.astype(float)

countries = {
    "India":  make_country([(80,12000,30),(200,35000,40),(380,25000,45)], 500),
    "UK":     make_country([(90,8000,25), (220,20000,35),(400,45000,50)], 300),
    "Brazil": make_country([(70,6000,28), (190,30000,38),(360,20000,42)], 400),
}
cfr     = {"India": 1.32, "UK": 1.75, "Brazil": 2.80}
colours = {"India": "#e84393", "UK": "#00c9a7", "Brazil": "#f5a623"}
dates   = pd.date_range("2020-03-01", periods=DAYS)

df = pd.DataFrame(countries, index=dates)
rolling = df.rolling(7).mean() 


plt.style.use('dark_background')

fig=plt.figure(figsize=(16,10))
fig.suptitle("COVID-19 Wave Analysis Dashboard", color="white",
             fontsize=17, fontweight="bold", y=0.98)

gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.32)
dark = dict(facecolor="#13131e")

# Panel 1 — Raw vs Smoothed: Plot daily new cases as faint grey bars,
#  then overlay the 7-day rolling average as a bold coloured line for one country. 
# This demonstrates why raw data is noisy and why smoothing is essential.
# Panel 1 : raw vs Rolling Avg for India 

ax1=fig.add_subplot(gs[0,0],**dark)
ax1.bar(dates,df["India"],color='grey',alpha=0.25,width=1)
ax1.plot(dates,rolling["India"],color='red',lw=2,label="7-day Avg")

ax1.set_title("India - Raw vs Rolling Average",color="white")
ax1.legend(facecolor="#13131e",labelcolor="white")
ax1.tick_params(colors="grey")

# Panel 2 — Multi-country comparison: Plot the rolling-average curves for 3 different countries on the same axes,
#  each a different colour, with a vertical shaded band marking the period of a major variant (e.g., Delta wave between day 180 and 260).

ax2=fig.add_subplot(gs[0,1],**dark)

for country,col in colours.items() :  # country name : color 
    ax2.plot(dates,rolling[country],color=col,lw=2,label=country)

delta_star,delta_end=dates[180],dates[260]
ax2.axvspan(delta_star,delta_end,alpha=0.12,color="white")
ax2.text(dates[215],ax2.get_ylim()[1]*0.85,"Delta\nWave",
         color="white",fontsize=8,ha="center")
ax2.set_title("3-Country Comparision (Rolling Avg)",color="white")
ax2.legend(facecolor="#13131e",labelcolor="white")

ax2.tick_params(color="grey")

# Panel 3 — Cumulative cases: Show a stacked area chart of cumulative cases for all 3 countries.
#  Each country's area should be filled with alpha transparency so overlaps are visible.
#  Label the final values at the right edge of the chart.

ax3=fig.add_subplot(gs[1,0],**dark)
cumulative=df.cumsum()
stack_values=[cumulative[country].values for country in colours]
ax3.stackplot(dates,*stack_values,labels=list(colours.keys()),
              colors=list(colours.values()),alpha=0.65)
ax3.set_title("Cumulative Cases (Stacked)",color="white")
ax3.tick_params(colors="grey")

# Panel 4 — Death rate bar chart: Show a horizontal bar chart comparing the simulated case-fatality rate (CFR %) of each country,
#  sorted from highest to lowest. Annotate each bar with its exact value.

ax4 = fig.add_subplot(gs[1, 1], **dark)
sorted_cfr = sorted(cfr.items(), key=lambda x: x[1], reverse=True)
names, vals = zip(*sorted_cfr)
bar_cols    = [colours[n] for n in names]
bars = ax4.barh(names, vals, color=bar_cols, edgecolor="none")
for bar, val in zip(bars, vals):
    ax4.text(val + 0.03, bar.get_y() + bar.get_height()/2,
             f"{val:.2f}%", va="center", color="white", fontsize=10)
ax4.set_title("Case-Fatality Rate (%)", color="white")
ax4.set_xlim(0, 3.5)
ax4.tick_params(colors="grey"); ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)
plt.tight_layout()
fig.savefig("Covid_dashbord.png",dpi=150,bbox_inches="tight")
plt.show()
