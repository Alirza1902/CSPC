import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")
cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, c in zip(axes.ravel(), cols):
    stats.probplot(df[c], dist="norm", plot=ax)
    ax.set_title("Q-Q plot: " + c)
plt.tight_layout()
plt.savefig("qq.png", dpi=120)

for c in cols:
    w, p = stats.shapiro(df[c])
    print(f"{c}: skew={stats.skew(df[c]):.2f}, kurtosis={stats.kurtosis(df[c]):.2f}, Shapiro W={w:.3f}, p={p:.2g}")