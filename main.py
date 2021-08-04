from matplotlib import pyplot as plt
import numpy as np

# TiTle
plt.title('Pie Chart')

# Percentage
y = np.array([25, 25, 25, 25])

# Name && Separation
mylabels = ['Apple', 'Bananas', 'Orange', 'Guava']
myexplode = [0, 0, 0, 0]

# Run
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()