import numpy as np

import matplotlib
#mpl.use("pgf")
from matplotlib.backends.backend_pgf import FigureCanvasPgf
matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_pdflatex={
    "pgf.texsystem":"pdflatex",
    "pgf.preamble":[
        r"\usepackage[utf8x]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{cmbright}",
        ]
}
matplotlib.rcParams.update(pgf_with_pdflatex)




import matplotlib.pyplot as plt
from numpy import nan as NA
import csv
import pdb

fig = plt.figure()

ax = fig.add_subplot(1,2,1)
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#fig.suptitle('Oscillator Power at DC inputs', fontsize=14, fontweight='bold')
t = []
a = []

with open('3_13vdc.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # define the dataframe
            #print(row[0])
            #pdb.set_trace()
            #nn = row[0]
            #nn = np.log10(int(nn))
            #print(nn)
            t.append(row[0])
            a.append(row[4])    

ax1.scatter(t,a)
ax1.set_xscale('log')


ax1.grid(True, 'both')
ax1.autoscale(enable=True, axis='x', tight=True)
ax1.set_ylabel('Power at f$_c$ [dBm]', size=14)
ax1.set_xlabel('log$_{10}$(V$_{dc}$)', size=14)

t2 = []
a2 = []

with open('3_13vdc.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # define the dataframe
            #print(row[0])
            #pdb.set_trace()
            #nn = row[0]
            #nn = np.log10(int(nn))
            #print(nn)
            t2.append(row[0])
            a2.append(row[4])    

ax2.scatter(t2,a2)
ax2.grid(True, 'both')
#ax2.autoscale(True,'both',True)
ax1.set_ylabel(u'Power at f$_c$ [dBm]', size=14)
ax2.set_xlabel('V$_{dc}$', size=14)

#ax.set_xlabel('V')
fig.subplots_adjust(bottom=.15, top=.9)

#plt.xlabel('log(V_dc)')
#plt.ylabel('Power at f_c [dBm]')
plt.show()
