import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

c = pd.read_csv("chemicals_cancer.csv")

print("cadmium vs pollution:", round(c["cadmium"].corr(c["pollution_index"]), 3))
print("benzene vs pollution:", round(c["benzene"].corr(c["pollution_index"]), 3))
print("age vs malignancy:", round(c["age"].corr(c["malignancy"]), 3))
print()

print("narrow pollution groups:")
edges = [30, 40, 50, 60, 70]
for lo, hi in zip(edges[:-1], edges[1:]):
    g = c[(c["pollution_index"] > lo) & (c["pollution_index"] <= hi)]
    rb = g["benzene"].corr(g["malignancy"])
    rc = g["cadmium"].corr(g["malignancy"])
    print(f"{lo}-{hi}: n={len(g)}, benzene r={rb:.3f}, cadmium r={rc:.3f}")
print()

mid = c[(c["pollution_index"] > 45) & (c["pollution_index"] < 55)]
print("pollution 45-55: n =", len(mid))
print("benzene r:", round(mid["benzene"].corr(mid["malignancy"]), 3))
print("cadmium r:", round(mid["cadmium"].corr(mid["malignancy"]), 3))
print()

def remove_pollution(y):
    line = np.polyfit(c["pollution_index"], y, 1)
    return y - np.polyval(line, c["pollution_index"])

mal = remove_pollution(c["malignancy"])
for name in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(remove_pollution(c[name]), mal)
    print("partial", name, "r:", round(r, 3), "p:", p)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(mid["benzene"], mid["malignancy"], s=10)
ax[0].set_xlabel("benzene")
ax[0].set_ylabel("malignancy")
ax[0].set_title("pollution 45-55")
ax[1].scatter(mid["cadmium"], mid["malignancy"], s=10)
ax[1].set_xlabel("cadmium")
ax[1].set_ylabel("malignancy")
ax[1].set_title("pollution 45-55")
plt.tight_layout()
plt.savefig("confounder.png", dpi=120)