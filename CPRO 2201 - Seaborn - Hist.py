import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

temps = np.array([42, 45, 48, 52, 55, 61, 65, 70])

sns.histplot(x=temps, bins=5, kde=True)
plt.title("Distribution of CPU Temperatures")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
