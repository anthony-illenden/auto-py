import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
heights = np.random.rand(100) * 10
colors = np.random.rand(100) 
colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
cmap = np.random.choice(colormaps)
plt.bar(x, heights, color=plt.get_cmap(cmap)(colors))
plt.title('Random Bar Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('output/output.png')
