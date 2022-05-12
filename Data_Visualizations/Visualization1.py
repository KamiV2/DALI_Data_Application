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
a["Profit Margin"] = a["Profit"]/a["Sales"]


def plot_profit_margin(i):
        min = a["Order Date"].min()
        orders = a[abs(a["Order Date"] - (min + dt.timedelta(days=i)*15)) < dt.timedelta(15)]

        if (min + dt.timedelta(days=i)*15 < a["Order Date"].max()):
            ax01.cla()
            ax02.cla()
            h1 = ax01.hist(orders["Profit Margin"]*100, color="blue", bins=25, density=True, stacked=True, orientation="horizontal")
            mu = np.mean(orders["Profit Margin"]*100)
            i_arr.append((min + dt.timedelta(days=i)*15))
            mu_arr.append(mu)
            ax01.axhline(mu, color='k', linestyle='dashed', linewidth=1)
            ax01.text(0.08, mu-10, f"\u03BC = {int(mu)}%")
            ax01.title.set_text(f"15-day profit margins by sale ({(min + dt.timedelta(days=i)*15).strftime('%m-%d-%y')})")
            ax01.set_ylim(a["Profit Margin"].min()*100, a["Profit Margin"].max()*100)
            ax01.set_xlim(0, 0.1)
            ax01.set_ylabel("Profit Margin (%)")
            ax01.set_xlabel("Proportion of sales")

            ax02.plot(i_arr, mu_arr, marker='o', markersize=1, color="red")
            ax02.title.set_text(f"Profit Margin over time")
            ax02.set_xlim(a["Order Date"].min() - dt.timedelta(days=3), a["Order Date"].max())
            ax02.axvline(min + dt.timedelta(days=15)*i, color='k', linestyle='dashed', linewidth=1)
            ax02.set_ylim(-10, 50)
            ax02.set_ylabel("Average Profit Margin (%)")
            ax02.set_xticks(np.datetime_as_string(np.arange(a["Order Date"].min() - dt.timedelta(days=2), orders["Order Date"].max(), dt.timedelta(days=365 / 2)), unit="D"))
            for tick in ax02.get_xticklabels():
                tick.set_rotation(30)





f0 = figure(num = 0, figsize = (16, 9))
f0.suptitle("Changing Profit Margins Over Time", fontsize=14)
ax01 = subplot2grid((1, 2), (0, 0))
ax02 = subplot2grid((1, 2), (0, 1))
i_arr = []
mu_arr = []
anim = ani.FuncAnimation(f0, plot_profit_margin, interval = 200)
# writergif = ani.PillowWriter(fps=10)
# anim.save("Visualization1.gif", writer=writergif)
plt.show()


