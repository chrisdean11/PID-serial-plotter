#!/usr/bin/env python2.7
# Written by Chris Dean
# Portland State

# Plots data from the specified text file with an optional horizontal line indicating the set point in your 
# control loop algorithm.
# The text file must be a series of integers, one per line, in sequential order (the line number is that data point's x-value)

import sys
import argparse
from struct import unpack
from pylab import *

# Command line argument parsing
# This block of code allows you to run this program with arguments from the command line. 
# USAGE: serial_plotter2.py [-h] [-s SETPOINT] filename algorithm

parser = argparse.ArgumentParser(description = 'Plots data produced from your control loop algorithm.\nCopy the datapoints in your debug console produced from printf commands into a text file with one data member per line.\n')
parser.add_argument("filename", type=str, help=".txt file to plot")
parser.add_argument("algorithm", type=str, help="Name of the algorithm to appear in plot title")
parser.add_argument("-s", "--setpoint", type=float, help="Set point to show on plot")
args = parser.parse_args()
filename = args.filename
setpoint = args.setpoint
algorithm = args.algorithm

# x and y axis data, respectively
time = []
data = []
n = 1

# Open file
with open(filename, 'rb') as myfile:
	for line in myfile:
		try:
			data.append(float(line))
			time.append(n)
			n += 1
		except ValueError:
			print 'WARNING: Text file must only contain lines with a single number each. No non-numeric characters, spaces, or blank lines.'
			#sys.exit()

# Ensures both lists have the same length so plot() doesn't barf
while(len(time) !=len(data)):
	if (len(time) > len(data)): del time[-1]
	if (len(time) < len(data)): del data[-1]


# Plot the data
plot(time, data, linewidth=1.0)
xlabel('Sample Index')
ylabel('Feedback Value')
mytitle = 'Closed Loop Control: '
mytitle += algorithm
mytitle += ' Plot'
title(mytitle)
grid(True)
axes = plt.gca()
axes.set_ylim([0,1.1*max(data)])
plt.plot((time[0], time[-1]), (setpoint, setpoint), 'k-')
show()