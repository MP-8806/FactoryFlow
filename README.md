# FactoryFlow — Production Efficiency & Downtime Analyzer

A production-excellence analytics application for identifying bottlenecks, downtime drivers and line-level efficiency gaps.

## Features
- Synthetic production-line dataset
- OEE-style availability, performance and quality metrics
- Downtime Pareto analysis
- Line comparison
- Shift-level productivity analysis
- Automated bottleneck identification
- Interactive Streamlit dashboard

## Run

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python src/generate_data.py
streamlit run src/app.py
```

## Metrics

**Availability** = operating time / planned production time

**Performance** = actual output / theoretical output

**Quality** = good units / total units

**OEE** = Availability × Performance × Quality

The data is synthetic and designed for portfolio demonstration.
