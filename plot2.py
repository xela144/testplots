import numpy as np
import matplotlib.pyplot as plt
from numpy import nan as NA
import csv

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
t = []
a = []

with open('data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
	    # define the dataframe
		t.append(row[0])
		a.append(row[1])	

ax.plot(t,a)

plt.xlabel('t')
plt.ylabel('airpseed')
plt.show()
