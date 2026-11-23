import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

usage = np.array([20, 25, 35, 45, 55, 70, 80, 95])
temps = np.array([42, 45, 48, 52, 55, 61, 65, 70])

sns.regplot(x=usage, y=temps)
plt.xlabel("CPU Usage (%)")
plt.ylabel("Temperature (°C)")
plt.title("Usage vs Temperature")
plt.tight_layout()
plt.show()
