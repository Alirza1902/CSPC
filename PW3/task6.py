import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

c = pd.read_csv("chemicals_cancer.csv")
print(c.shape)
print(c.head())

for name in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(c[name], c["malignancy"])
    print(name, "r:", round(r, 3), "p:", p)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(c["benzene"], c["malignancy"], s=6)
ax[0].set_xlabel("benzene")
ax[0].set_ylabel("malignancy")
ax[1].scatter(c["cadmium"], c["malignancy"], s=6)
ax[1].set_xlabel("cadmium")
ax[1].set_ylabel("malignancy")
plt.tight_layout()
plt.savefig("naive.png", dpi=120)