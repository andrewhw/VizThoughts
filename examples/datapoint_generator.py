#!/usr/bin/env python

# Generate the data points for the boxplots

# This is a python "module" - it simply contains functions,
# but no code that is not inside a function.  We can then import
# it just like any other python module, and call the functions as
# we would call any module functions.
#
# This is an excellent way to provide a function that you want to
# call in two or more different python programs.  Take a look at
# the "boxplot" python programs to see how this is called

import sys
import numpy as np
import math
import random


## Randomly generate some data according to different distribution types
def generate_points(filename):

	# open a file to save our data to
	with open(filename, "w") as dfile:

		# the "dfile" variable is valid within this indented block,
		# once the block completes, the file will be closed

		# write a header to the file
		dfile.write("Group,Source,Measure\n")

		# loop 35 times -- we will end up with 70 points
		# of each distribution, as we write pairs of points
		# in the loop
		for i in range(0,35):

			# Gaussian data, mu=10, sigma=4
			dfile.write("G,A,%f\n" % random.gauss(10,4))
			dfile.write("G,A,%f\n" % random.gauss(10,4))

			# Laplacian data, mu=10, lambda=2.5
			dfile.write("G,B,%f\n" % np.random.laplace(10,2.5))
			dfile.write("G,B,%f\n" % np.random.laplace(10,2.5))

			# Gaussian within Gaussian: N_0(4,2), N_1(16,1)
			dfile.write("G,C,%f\n" % random.gauss(4,2))
			dfile.write("G,C,%f\n" % random.gauss(16,1))

			# two separate blocks of equally and densely spaced points
			dfile.write("U,D,%f\n" % ((i/4.0)-2.0))
			dfile.write("U,D,%f\n" % ((i/4.0)+20.0))

			# two overlapping blocks of equally and densely spaced points
			dfile.write("U,E,%f\n" % ((i/3.0)-1.0))
			dfile.write("U,E,%f\n" % ((i/3.0)+2.0))

			# two overlapping uniform density blocks
			dfile.write("U,F,%f\n" % random.uniform(2,20))
			dfile.write("U,F,%f\n" % random.uniform(2,20))

			# exponential distribution (lambda = 0.125)
			dfile.write("P,G,%f\n" % random.expovariate(0.125))
			dfile.write("P,G,%f\n" % random.expovariate(0.125))

