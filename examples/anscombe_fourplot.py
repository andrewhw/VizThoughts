#!/usr/bin/env python

# Example adapted from:
#     https://seaborn.pydata.org/examples/anscombes_quartet.html

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# set overall theme for seaborn plotting
sns.set(font_scale=2)
sns.set_theme(style="ticks")


# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Change the data column names to make better labels
df = df.rename(columns={"x":"x (unitless)", "y":"y (unitless)"})


# divide the quartet up by data set, so we can plot one at a time
df_by_dataset = {}
for dataset in [ "I", "II", "III", "IV" ]:
	df_by_dataset[dataset] = df.loc[df['dataset'] == dataset]

# create a separate plot for each of the data sets
for dataset in df_by_dataset:

	# get the figure when the canvas is blank -- once drawn, we can save it
	fig = plt.figure()

	# Draw on the canvas using a seaborn plotting tool.
	# This creates a scatter plot for a single data set
	sns.scatterplot(x = "x (unitless)", y = "y (unitless)", style="dataset", hue="dataset", data=df_by_dataset[dataset])

	# locate the legend into a common good place
	plt.legend(loc="lower right")

	# Remove the top and right box lines from the plot frame
	sns.despine()

	# fix the axes so that all four plots are the same
	plt.ylim(3,13)
	plt.xlim(3,20)

	# save the canvas to a PDF file named after the data set
	fig.savefig(f'anscombe-scatter-dataset-{dataset}.pdf', bbox_inches="tight")

	# clear the canvas for the next plot in this loop
	fig.clf()

