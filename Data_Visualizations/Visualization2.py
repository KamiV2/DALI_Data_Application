import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.animation as ani

from matplotlib.pylab import *

warnings.filterwarnings("ignore")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)


a = pd.read_csv('Superstore.csv')
a["Order Date"] = pd.to_datetime(a["Order Date"])
a["Ship Date"] = pd.to_datetime(a["Ship Date"])
a["Shipping Time"] = a["Ship Date"].sub(a["Order Date"], axis=0)
a["Profit Margin"] = a["Profit"]/a["Sales"]

b = a.groupby(["State"])
map = {}
map["State"] = []
map["Sales"] = []

for x in b:
    s = x[0]
    r = x[1]["Sales"].sum()
    print(r)
    map["State"].append(s)
    map["Sales"].append(r)
map["State"].append("Alaska")
map["Sales"].append(0)

print(map)
revenue_by_state = pd.DataFrame(map)
revenue_by_state.columns = ["State", "Sales"]
revenue_by_state.sort_values(["Sales"], ascending=False, inplace=True)
revenue_by_state.reset_index(inplace=True)
revenue_by_state = revenue_by_state.drop(["index"], axis=1)

print(revenue_by_state)
revenue_by_state.to_csv("revenue_by_state.csv", index=False)
print(revenue_by_state.describe(percentiles=[0.2, 0.4, 0.6, 0.8]))
while True:
    ip = input("Enter a state: ")
    print(revenue_by_state[revenue_by_state["State"] == ip]["Sales"].sum())