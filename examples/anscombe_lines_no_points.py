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

# pull out only sets "II" and "III" into a new dataframe
df_2_and_3 = df.loc[(df['dataset'] == "II") | (df['dataset'] == "III")]



# Change the data column names to make better labels
df = df.rename(columns={"x":"x (unitless)", "y":"y (unitless)"})


## use hue (colour) to differentiate the data sets

# get the figure when the canvas is blank -- once drawn, we can save it
fig = plt.figure()

# Draw on the canvas using a seaborn plotting tool.
# This creates a lineplot with NO points (markers=True)
sns.lineplot(x = "x (unitless)", y = "y (unitless)",
		style="dataset", hue="dataset", markers=False,
		data=df_2_and_3)

# Remove the top and right box lines from the plot frame
sns.despine()

# save the canvas to a PDF file named after the data set
fig.savefig('anscombe-lines-NO-points.pdf', bbox_inches="tight")

