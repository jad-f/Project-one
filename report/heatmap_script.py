# filename: report/heatmap_script.py

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- locate folders ----------
try:
    # running as a .py file
    here = Path(__file__).resolve()          # .../DS-project/report/heatmap_script.py
    report_dir = here.parent                 # .../DS-project/report
    project_root = report_dir.parent         # .../DS-project
except NameError:
    # running inside a notebook (no __file__)
    report_dir = Path.cwd()
    project_root = report_dir if (report_dir / "data").exists() else report_dir.parent

data_dir = project_root / "data" / "raw"
print("Looking in:", data_dir)

# ---------- read data ----------
paths = sorted(data_dir.glob("experiment_*.csv"))
print("Found:", [p.name for p in paths])
if not paths:
    raise FileNotFoundError(f"No CSVs matched in {data_dir}")

df = pd.concat((pd.read_csv(p) for p in paths), ignore_index=True)

# ---------- prepare numeric matrix ----------
X = df.select_dtypes("number")
X = X.apply(pd.to_numeric, errors="coerce").replace([np.inf, -np.inf], np.nan).fillna(0)
X = X.loc[:, X.nunique() > 1]   # drop constant columns

# ---------- correlation heatmap ----------
corr = X.corr(numeric_only=True)
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(report_dir / "correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------- clustered heatmap ----------
g = sns.clustermap(
    corr,
    metric="correlation",
    method="average",
    cmap="YlGnBu",
    linewidths=0.3,
    figsize=(12, 10),
    dendrogram_ratio=(0.15, 0.1),
    cbar_pos=(0.02, 0.8, 0.03, 0.18),
)
g.savefig(report_dir / "correlation_clustermap.png", dpi=300, bbox_inches="tight")

print("Saved to:", report_dir)
print("Files: correlation_heatmap.png, correlation_clustermap.png")

