"""
Make a "broken" horizontal bar plot, i.e., one with gaps
"""
import matplotlib.pyplot as plt



fig, ax = plt.subplots()
ax.broken_barh([(50, 2), (100, 2),(150, 2)], (5, 20), facecolors='blue')
"""ax.broken_barh([(70, 80), (100, 20), (130, 10)], (5, 9),facecolors=('red', 'yellow', 'green'))"""
ax.broken_barh([(20, 60)], (5, 5),facecolors=('yellow'))
ax.broken_barh([(80, 40)], (10, 5),facecolors=('blue'))
ax.broken_barh([(90, 20)], (5, 5),facecolors=('red'))
ax.set_ylim(5, 30)
ax.set_xlim(0, 200)

ax.grid(True)
"""
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25])
ax.set_yticklabels(['Bill', 'Jim'])

ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')"""

plt.show()

