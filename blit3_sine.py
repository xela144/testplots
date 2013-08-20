import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import time
import pdb
#pdb.set_trace()
x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

fig, axes = plt.subplots(nrows=1)

style = 'r'

line = axes.plot(x,y,style,animated=True)[0]
print("line:", line)

fig.show()
fig.canvas.draw()
background=fig.canvas.copy_from_bbox(axes.bbox)
tstart = time.time()
for i in range(1,2000):
    fig.canvas.restore_region(background)
    line.set_ydata(np.sin(x + i/10.0))
    axes.draw_artist(line)
    fig.canvas.blit(axes.bbox)
print('fps', 2000/(time.time()-tstart))
