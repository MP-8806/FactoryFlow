import streamlit as st
import plotly.express as px
from analytics import load_data, line_summary, pareto

st.set_page_config(page_title="FactoryFlow", layout="wide")
st.title("🏭 FactoryFlow")
st.caption("Production Efficiency & Downtime Analyzer")

df = load_data()
line_filter = st.sidebar.multiselect(
    "Production Line",
    sorted(df["line"].unique()),
    default=sorted(df["line"].unique())
)
shift_filter = st.sidebar.multiselect(
    "Shift",
    sorted(df["shift"].unique()),
    default=sorted(df["shift"].unique())
)
df = df[
    df["line"].isin(line_filter) &
    df["shift"].isin(shift_filter)
]

avg_oee = df.oee.mean()*100
availability = df.availability.mean()*100
performance = df.performance.mean()*100
quality = df.quality.mean()*100

c1,c2,c3,c4 = st.columns(4)
c1.metric("OEE", f"{avg_oee:.1f}%")
c2.metric("Availability", f"{availability:.1f}%")
c3.metric("Performance", f"{performance:.1f}%")
c4.metric("Quality", f"{quality:.1f}%")

st.divider()
st.subheader("Line Efficiency")
summary = line_summary(df)
display = summary.copy()
for col in ["OEE","Availability","Performance","Quality"]:
    display[col] = (display[col]*100).round(1)
st.dataframe(display, use_container_width=True)

st.subheader("Downtime Pareto")
p = pareto(df)
fig = px.bar(p, x="downtime_min", y="downtime_reason", orientation="h",
             title="Downtime by Root Cause", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Daily OEE Trend")
daily = df.groupby("date", as_index=False)["oee"].mean()
daily["oee"] *= 100
st.plotly_chart(px.line(daily, x="date", y="oee", title="Average Daily OEE"), use_container_width=True)

worst = summary.iloc[0]
st.warning(f"Potential bottleneck: {worst['line']} has the lowest OEE at {worst['OEE']*100:.1f}%. Investigate its downtime and performance drivers.")
