import numpy as np
import matplotlib.pyplot as plt

temps = np.array([42, 45, 48, 52, 55, 61, 65, 70])

plt.hist(temps, bins=5, edgecolor="black")
plt.title("Distribution of CPU Temperatures")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
