#!/usr/bin/env python

# Simple boxplot examples

import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import math
import random

import datapoint_generator as gen	# our own point generator


# check if we have some data, and if not, use our generator
# module to create some
if not os.path.exists("boxplot-data.csv"):
	gen.generate_points("boxplot-data.csv")

# Data now created, so read into a pandas dataframe
df = pd.read_csv("boxplot-data.csv")

# set overall theme for seaborn plotting
sns.set_theme(style="ticks")


# get the figure when the canvas is blank -- once drawn, we can save it
fig = plt.figure()


# Draw on the canvas using a seaborn plotting tool.
# This creates a scatter plot for a single data set
ax = sns.boxplot(x="Source", y="Measure", data=df)


# Uncomment to add the points on top of the plot
## Add the "swarmed" datapoints on top of the current plot
#ax = sns.swarmplot(x="Source", y="Measure", data=df, size=3, color="k")

# reassign y axis label to a better value.  Note the use of
# $$ "quoting" to enter LaTeX math mode to have access to the
# Greek letter "mu"
plt.ylabel(r'Measure [$\mu$S]')

# Remove the top and right box lines from the plot frame
sns.despine()

# save the canvas to a PDF file named after the data set
fig.savefig(f'boxplot.pdf', bbox_inches="tight")

