import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

r, p = stats.pearsonr(df["age"], df["thalach"])
print("Pearson r:", round(r, 3), "p:", p)

rho, p2 = stats.spearmanr(df["age"], df["thalach"])
print("Spearman rho:", round(rho, 3), "p:", p2)

fit = stats.linregress(df["age"], df["thalach"])
print("slope:", round(fit.slope, 3), "intercept:", round(fit.intercept, 2))

x = np.array([df["age"].min(), df["age"].max()])

plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], s=14, alpha=0.7)
plt.plot(x, fit.intercept + fit.slope * x, color="red")
plt.xlabel("age")
plt.ylabel("thalach (max heart rate)")
plt.title("Age vs max heart rate")
plt.tight_layout()
plt.savefig("age_thalach.png", dpi=120)