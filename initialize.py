import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Random matrix

data_ones = np.random.randint(1, 2, size=(100, 100))
data_both = np.random.randint(0, 2, size=(100, 100))

# Define colormap
print(data_ones.shape)
cmapmine = ListedColormap(['b', 'w'], N=2)

# Plot matrix

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(data_ones, cmap=cmapmine, vmin=0, vmax=1)
ax1.set_title('Ones')
ax2.imshow(data_both, cmap=cmapmine, vmin=0, vmax=1)
ax2.set_title('Zeros and Ones')
plt.show()