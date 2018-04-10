import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

ages = np.random.normal(75,25,5)
#ages = np.append(ages,99999)
print(np.mean(ages))
print(ages)
print(np.median(ages))

salaries = np.random.randint(50,high=150,size=200)
from scipy import stats
print(stats.mode(salaries))


plt.hist(ages,5)
plt.show()
