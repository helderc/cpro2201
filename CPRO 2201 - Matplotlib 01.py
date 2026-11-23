import numpy as np
import matplotlib.pyplot as plt

usage = np.array([20, 25, 35, 45, 55, 70, 80, 95])
temps = np.array([42, 45, 48, 52, 55, 61, 65, 70])

plt.plot(temps, marker="o")
plt.title("CPU Temperature Over Time")
plt.xlabel("Measurement")
plt.ylabel("Temperature (°C)")
plt.show()
