# 🏒 NHL 2024 Player Analytics Dashboard

This project provides an interactive analytics dashboard and supporting data pipeline for NHL player performance during the 2023–2024 season using advanced possession and takeaway metrics.

---

## 📁 Project Files

### 1. `nhl_scraper.py`
A standalone Python script that:
- Loads advanced NHL player stats from a local CSV (`sportsref.csv`)
- Cleans and processes the data
- Adds two key custom metrics:
  - `Net_Takeaway = TK - GV`
  - `Possession_Score = (CF% + FF%) / 2`
- Generates exploratory visualizations:
  - Top 10 by Possession Score
  - Bottom 10 by Net Takeaway
  - Age vs. Possession bubble chart
- Exports the cleaned dataset to `cleaned_nhl_stats.csv`

### 2. `nhl_dashboard.py`
A fully interactive [Streamlit](https://streamlit.io) dashboard that:
- Lets users filter players by team, position, or name
- Displays:
  - 📊 Top 10 players by Net Takeaway and Possession Score
  - 🔢 All players sorted by last name
  - 🧠 Team-level average stats
  - 🔘 Age vs. Possession Score bubble chart
  - 📍 Annotated scatterplot of team-level efficiency
- Intended for deployment on Streamlit Cloud

---

## 📊 Key Metrics Explained

- **Net Takeaway**: A custom metric subtracting giveaways from takeaways, reflecting puck control.
- **Possession Score**: Average of Corsi For % (CF%) and Fenwick For % (FF%) as a proxy for puck possession dominance.

---

## 🚀 How to Run

### 📌 Locally
```bash
streamlit run nil_dashboard.py
