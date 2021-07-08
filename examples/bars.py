#!/usr/bin/env python

# Example adapted from:
#     https://seaborn.pydata.org/examples/anscombes_quartet.html

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


# set overall theme for seaborn plotting
sns.set_theme(style="whitegrid")

# load the seaborn "tips" example data
tips = sns.load_dataset("tips")


# Rename a number of columns at once to have better names
# by using a dictionary
renameDict = {
			"total_bill" : "Total Bill (US$)",
			"day": "Day",
			"sex":"Sex",
			"smoker":"Smoker",
			"tip":"Tip",
			"time":"Time",
			"size":"Size"}
tips = tips.rename(columns=renameDict)


# Tell seaborn to use a larger font scale, and a white background.
# Note that any call to set() must contain all changes from default,
# or values from previous calls to set() will be changed back to the
# default values.
sns.set(
	rc={'axes.facecolor':'white', 'figure.facecolor':'white'},
	font_scale=2)

# get the figure when the canvas is blank -- once drawn, we can save it
fig = plt.figure()

# create a vertical bar plot
sns.barplot(x = "Day", y = "Total Bill (US$)", data=tips)

# remove the top and right databox lines
sns.despine()

# save the plot
fig.savefig(f'barplot-tips.pdf', bbox_inches="tight")

# clear the figure for the next plot
fig.clf()


# Tell seaborn to use a very large font scale, and again setting
# the background to white.
#
# Again we must supply all values, as above.
sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'},
		font_scale=4)

# get the figure when the canvas is blank -- once drawn, we can save it
fig = plt.figure()

# create a HORIZONTAL plot (note that y and x are transposed from the
# above example)
ax = sns.barplot(y = "Day", x = "Total Bill (US$)", data=tips)

# remove the top and right databox lines
sns.despine()

# reprogram the x axis to force 5 ticks (default is too low for this plot)
ax.xaxis.set_major_locator(ticker.MaxNLocator(5))

# save the results
fig.savefig(f'barplot-tips-horizontal.pdf', bbox_inches="tight")


