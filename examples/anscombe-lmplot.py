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


# create an linear model plot to include the regression line
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df, col_wrap=2)

sns.despine()
# force the limits of the axes to a constant value
plt.ylim(3,13)
plt.xlim(3,20)
# here we call show() because the lmplot doesn't get properly saved to the file
plt.show()

