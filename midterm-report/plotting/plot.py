#!/usr/bin/python2 -i

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(2.55,2.5))
ax = fig.add_subplot(1,1,1)

t = np.arange(0., 1., 0.001)
z = np.zeros(1000)
curve = ax.plot((1-t)*(1-t), 2*t*(1-t), color='black', linewidth=2.)
ax.plot(z, t, 'k:', lw=1.5)
ax.plot(t, z, 'k:', lw=1.5)
ax.plot(t, 1-t, 'k:', lw=1.5)

ax.set_xlabel('P[X=0]')
ax.set_ylabel('P[X=1]')
ax.set_xticks([0,0.5,1])
ax.set_yticks([0,0.5,1])
ax.axis([-0.2, 1.2, -0.2, 1.2])
#ax.axis('equal')

fig.subplots_adjust(left=0.3,bottom=0.25)


plt.show(block=False)
