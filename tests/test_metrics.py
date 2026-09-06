import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
import pandas as pd
from analytics import load_data

def test_metrics_exist(tmp_path):
    f = tmp_path / "production.csv"
    pd.DataFrame({
        "date":["2026-01-01"],"line":["A"],"shift":["A"],
        "planned_min":[480],"downtime_min":[30],
        "ideal_units_per_min":[1.0],"total_units":[400],
        "good_units":[390],"scrap_units":[10],"downtime_reason":["Failure"]
    }).to_csv(f,index=False)
    df = load_data(f)
    assert {"availability","performance","quality","oee"} <= set(df.columns)
    assert 0 <= df.oee.iloc[0] <= 1
