import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)

plt.title('Histogram')
plt.show()




for col in 'xy':
    sns.kdeplot(data[col], shade=True)

plt.title('Kernel Density Estimation')
plt.show()

sns.distplot(data['x'])
sns.distplot(data['y']);
plt.title('Histogram and KDE Combined')
plt.show()

sns.kdeplot(data);
plt.title('Two-Dimensional KDE Plot')
plt.show()
