#!/usr/bin/env python

# Example adapted from:
#     https://seaborn.pydata.org/examples/anscombes_quartet.html

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# set overall theme for seaborn plotting
sns.set_theme(style="ticks")


# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Change the data column names to make better labels
df = df.rename(columns={"x":"x (unitless)", "y":"y (unitless)"})


## use hue (colour) to differentiate the data sets

# get the figure when the canvas is blank -- once drawn, we can save it
fig = plt.figure()

# Draw on the canvas using a seaborn plotting tool.
# This creates a scatter plot for a single data set
sns.scatterplot(x = "x (unitless)", y = "y (unitless)",
		hue="dataset", alpha=0.65,
		data=df)

# Remove the top and right box lines from the plot frame
sns.despine()

# save the canvas to a PDF file named after the data set
fig.savefig('anscombe-scatter-hue.pdf', bbox_inches="tight")

