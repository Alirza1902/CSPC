import pandas as pd

df = pd.read_csv("heart.csv")
print(df.shape)
print(df.head())

X = df[["age", "chol", "trestbps", "thalach"]]
print(X.head())
