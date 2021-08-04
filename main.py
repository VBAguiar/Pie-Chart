from matplotlib import pyplot as plt
import numpy as np

y = np.array([50, 50])

mylabels = ['Apple', 'Bananas']
myexplode = [0.1, 0.1]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()