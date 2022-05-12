import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.animation as ani
from matplotlib.pylab import *


warnings.filterwarnings("ignore")

def mean_ship(order_date):
    return a[a['Order Date'] - order_date < dt.timedelta(days=30)]['Shipping Time'].mean()

def percentile_ship(order_date):
    return a[a['Order Date'] - order_date < dt.timedelta(days=30)]['Shipping Time'].quantile(0.25)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

a = pd.read_csv('Superstore.csv')
a["Order Date"] = pd.to_datetime(a["Order Date"])
a["Ship Date"] = pd.to_datetime(a["Ship Date"])
a["Shipping Time"] = a["Ship Date"].sub(a["Order Date"], axis=0)
a["Shipping Time"] = a["Shipping Time"].dt.days
a.sort_values(by="Order Date", inplace=True)

fig = plt.figure(figsize=(16, 12))

ax01 = subplot2grid((2, 2), (0, 0))
ax02 = subplot2grid((2, 2), (0, 1))
ax11 = subplot2grid((2, 2), (1, 0))
ax12 = subplot2grid((2, 2), (1, 1))
fig.suptitle("Shipping Times Over Time")
ax01.hist(a[a["Order Date"] < dt.datetime(2015, 1, 1)]["Shipping Time"], bins=7, color="b")
ax01.set_title("2014-2015")
ax01.set_xlabel("Shipping Time (Days)")
ax01.set_ylabel("# of Orders")
ax01.set_ylim(0, 3000)
ax02.hist(a[a["Order Date"] < dt.datetime(2016, 1, 1)]["Shipping Time"], bins=7, color="b")
ax02.set_title("2015-2016")
ax02.set_xlabel("Shipping Time (Days)")
ax02.set_ylabel("# of Orders")
ax02.set_ylim(0, 3000)
ax11.hist(a[a["Order Date"] < dt.datetime(2017, 1, 1)]["Shipping Time"], bins=7, color="b")
ax11.set_title("2016-2017")
ax11.set_xlabel("Shipping Time (Days)")
ax11.set_ylabel("# of Orders")
ax11.set_ylim(0, 3000)
ax12.hist(a[a["Order Date"] < dt.datetime(2018, 1, 1)]["Shipping Time"], bins=7, color="b")
ax12.set_title("2017-2018")
ax12.set_xlabel("Shipping Time (Days)")
ax12.set_ylabel("# of Orders")
ax12.set_ylim(0, 3000)
fig.tight_layout()
# plt.savefig("Visualization3.png")


plt.show()
