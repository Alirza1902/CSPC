import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("heart.csv")
cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
for ax, c in zip(axes.ravel(), cols):
    ax.hist(df[c], bins=20, edgecolor="black")
    ax.set_title(c)
    ax.set_xlabel(c)
    ax.set_ylabel("count")

plt.tight_layout()
plt.savefig("hist.png", dpi=120)
print("hist.png saved")