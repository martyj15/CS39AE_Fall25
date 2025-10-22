import pandas as pd
import plotly.express as px

# Read CSV
df = pd.read_csv("pie_demo.csv")

# Build interactive pie chart
fig = px.pie(
    df,
    names="Player",
    values="CompositeScore",
    title="Best Players in the NBA (Demo Composite Score)",
    hole=0.0  # change to 0.4 for donut
)

fig.update_traces(
    texttemplate="%{label}<br>%{percent}",
    textposition="inside",
    hovertemplate="<b>%{label}</b><br>Score: %{value}<br>%{percent} of total<extra></extra>"
)

# Save interactive HTML
fig.write_html("3_Pie.html", include_plotlyjs="cdn", full_html=True)
print("✅ Wrote 3_Pie.html — open it in your browser to explore!")
