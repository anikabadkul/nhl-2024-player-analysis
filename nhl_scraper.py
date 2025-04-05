import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("/Users/anikabadkul/Desktop/Projects/NHL_Webscrapping/sportsref.csv", skiprows=1)
df = df.dropna(subset=["Player"])
df = df.drop(columns=["Rk"])
cols = ["Age", "GP", "CF%", "GV"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["Net_Takeaway"] = df["TK"] - df["GV"]
df["Possession_Score"] = (df["CF%"] + df["FF%"]) / 2
print(df.head())  
print(df.columns)

top_takeaways = df.sort_values(by="Net_Takeaway", ascending = False).head(10)
print(top_takeaways[["Player", "TK", "GV", "Net_Takeaway"]])
sns.barplot(x="Net_Takeaway", y="Player", data=top_takeaways)
plt.title("Bottom 10 NHL Players by Net Takeaway (2024)")
plt.xlabel("Net_Takeaway")
plt.ylabel("Player")
plt.tight_layout()
plt.show()


takeaways = df.sort_values(by="Possession_Score", ascending = False).head(10)
print(takeaways[["Player", "TK", "GV", "Possession_Score"]])
sns.barplot(x="Possession_Score", y="Player", data=takeaways)
plt.title("Top 10 NHL Players by Possession Score (2024)")
plt.xlabel("Possession_Score")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

t = df.sort_values(by="Possession_Score", ascending = False).head(10)
print(t[["Player", "TK", "GV", "Possession_Score"]])
sns.scatterplot(x="Age", y="Possession_Score", hue="Possession_Score", size="Possession_Score", sizes=(40, 300),data=t)
plt.title("Player Age vs. Possession Efficiency (Top 10 by Possession Score))")
plt.xlabel("Age")
plt.ylabel("Player")
plt.tight_layout()
plt.show()

df.to_csv("cleaned_nhl_stats.csv", index=False)
