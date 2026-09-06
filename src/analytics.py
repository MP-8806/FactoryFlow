import pandas as pd

def load_data(path="data/production.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    df["operating_min"] = df["planned_min"] - df["downtime_min"]
    df["availability"] = df["operating_min"] / df["planned_min"]
    df["performance"] = df["total_units"] / (df["operating_min"] * df["ideal_units_per_min"]).clip(lower=1)
    df["quality"] = df["good_units"] / df["total_units"].clip(lower=1)
    df["oee"] = df["availability"] * df["performance"] * df["quality"]
    return df

def line_summary(df):
    return df.groupby("line", as_index=False).agg(
        OEE=("oee","mean"),
        Availability=("availability","mean"),
        Performance=("performance","mean"),
        Quality=("quality","mean"),
        Downtime_Min=("downtime_min","sum")
    ).sort_values("OEE")

def pareto(df):
    return df.groupby("downtime_reason", as_index=False)["downtime_min"].sum().sort_values("downtime_min", ascending=False)
