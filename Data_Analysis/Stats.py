import pandas as pd
import numpy as np
df = pd.read_csv('Superstore.csv')
print(df.columns)
df["Profit Margin"] = df["Profit"]/df["Sales"]
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Shipping Time"] = df["Ship Date"].sub(df["Order Date"], axis=0).apply(lambda x: x.days)
feature = "Ship Mode"
chisq = 0
for x in df[feature].unique():
    a = round(df[df[feature] == x]["Shipping Time"].mean(), 3)
    b = round(df["Shipping Time"].mean(), 3)
    chisq += (a - b)**2 / b
    print(str(x) +" & " + str(a) + " & " + str(b) +"\\\\")

print("All", df["Shipping Time"].mean())
print("Chi-Square:", chisq)