# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:32:18 2023

@author: swank
"""

Starting with a Graph
Defining the plot
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
plt.plot(range(1,11), values)
plt.show()
Drawing multiple lines and plots
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
plt.plot(range(1,11), values)
plt.plot(range(1,11), values2)
plt.show()
Saving your work to disk
import matplotlib.pyplot as plt
#%matplotlib auto
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
plt.plot(range(1,11), values)
plt.ioff()
plt.savefig('C:\\Users\\swank\\OneDrive\\Desktop\\P4DS\\MySamplePlot.png', format='png')
Setting the Axis, Ticks, Grids
Getting the axes
import matplotlib.pyplot as plt
#%matplotlib notebook
​
values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
ax = plt.axes()
plt.plot(range(1,11), values)
plt.show()
Formatting the axes
import matplotlib.pyplot as plt
#%matplotlib notebook
​
values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
ax = plt.axes()
ax.set_xlim([0, 11])
ax.set_ylim([-1, 11])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.plot(range(1,11), values)
plt.show()
Adding grids
import matplotlib.pyplot as plt
#%matplotlib notebook
​
values = [0, 5, 8, 9, 2, 0, 3, 10, 4, 7]
ax = plt.axes()
ax.set_xlim([0, 11])
ax.set_ylim([-1, 11])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.grid()
plt.plot(range(1,11), values)
plt.show()
Defining the Line Appearance
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
plt.plot(range(1,11), values, '--')
plt.plot(range(1,11), values2, ':')
plt.show()
Using colors
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
plt.plot(range(1,11), values, 'r')
plt.plot(range(1,11), values2, 'm')
plt.show()
Adding markers
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
plt.plot(range(1,11), values, 'o--')
plt.plot(range(1,11), values2, 'v:')
plt.show()
Using Labels, Annotations, and Legends
Adding labels
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
plt.xlabel('Entries')
plt.ylabel('Values')
plt.plot(range(1,11), values)
plt.show()
Annotating the chart
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
plt.annotate(xy=[1,1], s='First Entry')
plt.plot(range(1,11), values)
plt.show()
Creating a legend
import matplotlib.pyplot as plt
#%matplotlib inline
​
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
line1 = plt.plot(range(1,11), values)
line2 = plt.plot(range(1,11), values2)
plt.legend(['First', 'Second'], loc=4)
plt.show()