import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.wind(return_type="pandas")

# Print first and last 10 rows
print("FIRST 10 ROWS:")
print(df.head(10))
print("\nLAST 10 ROWS:")
print(df.tail(10))

# Clean 'strength' -> float
# The strength values look like "0-1", "1-2", etc. We'll convert to a numeric midpoint.
# Example: "1-2" becomes 1.5
strength_range = df["strength"].str.replace(r"[^\d\-\.]", "", regex=True)
parts = strength_range.str.split("-", expand=True)

df["strength_float"] = (parts[0].astype(float) + parts[1].astype(float)) / 2

# Interactive scatter plot
fig = px.scatter(
    df,
    x="strength_float",
    y="frequency",
    color="direction",
    title="Wind: Strength vs Frequency (colored by direction)",
    labels={"strength_float": "Strength (midpoint)", "frequency": "Frequency"}
)

# Save to HTML
fig.write_html("assignment12/wind.html")

print("\nSaved interactive plot to assignment12/wind.html")