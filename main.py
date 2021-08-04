from matplotlib import pyplot as plt
import numpy as np

plt.title('Pie Chart')

y = np.array([25, 25, 25, 25])

mylabels = ['Apple', 'Bananas', 'Orange', 'Guava']
myexplode = [0, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()