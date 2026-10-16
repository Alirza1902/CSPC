import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

sick = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]

print("sick:", len(sick), "mean:", round(sick.mean(), 2))
print("healthy:", len(healthy), "mean:", round(healthy.mean(), 2))

t, p = stats.ttest_ind(sick, healthy, equal_var=False)
print("Welch t:", round(t, 2), "p:", p)

u, p2 = stats.mannwhitneyu(sick, healthy)
print("Mann-Whitney p:", p2)

s = np.sqrt((sick.var() + healthy.var()) / 2)
print("Cohen d:", round((sick.mean() - healthy.mean()) / s, 2))

means = []
errs = []
for name, g in [("healthy", healthy), ("sick", sick)]:
    sem = stats.sem(g)
    err = stats.t.ppf(0.975, len(g) - 1) * sem
    means.append(g.mean())
    errs.append(err)
    print(name, "mean:", round(g.mean(), 2), "SEM:", round(sem, 2), "95% CI: +/-", round(err, 2))

plt.figure(figsize=(4.5, 5))
plt.errorbar(["Healthy", "Disease"], means, yerr=errs, fmt="o", capsize=8)
plt.ylabel("mean thalach (bpm), 95% CI")
plt.title("Max heart rate by group")
plt.tight_layout()
plt.savefig("means_ci.png", dpi=120)