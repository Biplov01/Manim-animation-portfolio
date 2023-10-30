import matplotlib.pyplot as plt
import numpy as np

# Simulated data points
concentration = np.array([989, 965, 923, 718, 923, 1000, 984, 990])  # Simulated gas concentration in ppm
voltage_output = np.array([4.0, 3.8, 3.6, 3.3, 3.0, 2.8, 2.5, 2.3])  # Simulated voltage output in volts

# Create the characteristic curve
plt.figure(figsize=(10, 6))
plt.plot(concentration, voltage_output, marker='o', linestyle='-')
plt.title("MQ-4 Sensor Characteristic Curve")
plt.xlabel("Gas Concentration (ppm)")
plt.ylabel("Voltage Output (V)")
plt.grid(True)
plt.show()
