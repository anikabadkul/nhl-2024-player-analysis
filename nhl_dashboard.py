import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/anikabadkul/Desktop/Projects/NHL_Webscrapping/cleaned_nhl_stats.csv")

st.title("🏒 NHL 2024 Player Analytics Dashboard")
st.sidebar.header("Filter Players")
teams = st.sidebar.multiselect('What teams do you want to filter by: ',df["Tm"].unique())
positions = st.sidebar.multiselect('What positions do you want to filter by: ',df["Pos"].unique())
filtered_df = df.copy()
if teams:
    filtered_df = filtered_df[filtered_df["Tm"].isin(teams)]
if positions:
    filtered_df = filtered_df[filtered_df["Pos"].isin(positions)]
player = st.text_input("Search for a Player:")
if player:
    filtered_df = filtered_df[filtered_df["Player"].str.contains(player, case=False, na=False)]


team_avg = filtered_df.groupby("Tm")
team_avg = team_avg[["Net_Takeaway", "Possession_Score"]].mean()
st.subheader("Team Average Stats")
st.dataframe(team_avg)

team_avg = team_avg.reset_index()
fig, ax = plt.subplots()
sns.scatterplot(data=team_avg,x="Net_Takeaway",y="Possession_Score",ax=ax)
for i, row in team_avg.iterrows():
    ax.text(row["Net_Takeaway"], row["Possession_Score"], row["Tm"], fontsize=8, ha='right')
ax.set_title("Team-Level Averages: Net Takeaway vs. Possession Score")
st.pyplot(fig)


filtered_df["LastName"] = filtered_df["Player"].str.split().str[-1]  
all_players = filtered_df.sort_values(by="LastName")
st.subheader("All Players Sorted by Last Name")
st.dataframe(all_players[["Player", "TK", "GV", "Net_Takeaway"]])


filtered_df = filtered_df.sort_values(by="Net_Takeaway", ascending = False).head(10)
st.subheader("Top 10 Players by Net Takeaway")
st.dataframe(filtered_df[["Player", "TK", "GV", "Net_Takeaway"]])

fig, ax = plt.subplots()
sns.barplot(x="Net_Takeaway", y="Player", data=filtered_df, ax=ax)
ax.set_title("Top 10 NHL Players by Net Takeaway")
st.pyplot(fig)

possession_df = filtered_df.sort_values(by="Possession_Score", ascending = False).head(10)
st.subheader("Top 10 Players by Possesion Score")
st.dataframe(possession_df[["Player", "CF%", "FF%", "Possession_Score"]])

fig, ax = plt.subplots()
sns.barplot(x="Possession_Score", y="Player", data=possession_df, ax=ax)
ax.set_title("Top 10 NHL Players by Possesion Score")
st.pyplot(fig)


fig, ax = plt.subplots()
sns.scatterplot(x="Age", y="Possession_Score", data=filtered_df, ax=ax, hue="Possession_Score", size="Possession_Score", sizes=(40, 300))
ax.set_title("Player Age vs. Possession Efficiency (Top 10 by Possession Score)")
st.pyplot(fig)
