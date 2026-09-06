from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
root = Path(__file__).resolve().parents[1]
data = root / "data"
data.mkdir(exist_ok=True)

lines = ["Line A", "Line B", "Line C", "Line D"]
shifts = ["A", "B", "C"]
causes = ["Material Shortage", "Machine Failure", "Changeover", "Quality Hold", "Planned Maintenance", "No Downtime"]

rows = []
for day in pd.date_range("2026-04-01", "2026-06-30"):
    for line in lines:
        for shift in shifts:
            planned = 480
            downtime = int(rng.choice([0, 10, 20, 30, 45, 60, 90, 120], p=[.18,.16,.18,.15,.12,.08,.08,.05]))
            good = int(rng.integers(350, 720))
            scrap = int(rng.integers(5, 60))
            ideal_per_min = 1.6
            operating = planned - downtime
            actual = good + scrap
            rows.append([day,line,shift,planned,downtime,ideal_per_min,actual,good,scrap,
                         rng.choice(causes)])
df = pd.DataFrame(rows, columns=["date","line","shift","planned_min","downtime_min","ideal_units_per_min","total_units","good_units","scrap_units","downtime_reason"])
df.to_csv(data/"production.csv", index=False)
print("Generated data/production.csv")
