# PID-serial-plotter
Small Python program to plot the text output from a separate PID program. It's a program I made while practicing the "argparse" and "pylab" libraries.

Serial Plotter program by Chris Dean, Spring 2016

This program was created to plot PID controller datapoints for another project, but
can be used for plotting any serial data. Includes optional command line arguments
for adding a set-point line and displaying help text.

sample.txt contains an example file for serial_plotter to read.
It contains a characterization plot which ramps from 0 to Max.

INSTRUCTIONS FOR USE

1. Save your data as a .txt file with one data value per line. Data points 
should be a single integer. The x-axis sample index is simply the line number.
See the provided sample.txt for an example.

2. Open a linux terminal and navigate to the directory containing 
serial_plotter.py and your data file.

3. Type the command:
	"./serial_plotter.py myfile.txt algorithm-I-used"
   For example, try:
	"./serial_plotter.py sample.txt PID"

4. A plot will show the data, with the name of your algorithm in
the chart title. Also include the command "-s [int setpoint]" to
create a horizontal line indicating the setpoint.


HELP TEXT
***************************************************************************
usage: serial_plotter2.py [-h] [-s SETPOINT] filename algorithm

Plots data produced from your control loop algorithm. Copy the datapoints in
your debug console produced from printf commands into a text file with one
data member per line.

positional arguments:
  filename              .txt file to plot
  algorithm             Name of the algorithm to appear in plot title

optional arguments:
  -h, --help            show this help message and exit
  -s SETPOINT, --setpoint SETPOINT
                        Set point to show on plot
***************************************************************************
