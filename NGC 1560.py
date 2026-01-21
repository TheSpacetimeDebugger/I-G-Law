import matplotlib.pyplot as plt
import numpy as np

# --- Data for Challenge 3: NGC 1560 ---
# Radius in kiloparsecs (kpc)
rad = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
# Observed Velocity (km/s) from SPARC data
v_obs = np.array([25.2, 42.1, 55.4, 63.8, 68.2, 70.5, 72.1, 74.3, 75.8, 77.1, 78.5, 79.2, 79.8, 80.1, 80.5])
# Newtonian Prediction (Visible Stellar/Gas Disk contribution)
v_disk = np.array([5.1, 12.3, 19.5, 25.4, 30.1, 33.5, 36.2, 38.4, 40.1, 41.5, 43.2, 44.5, 45.3, 45.9, 46.2])

# --- I-G Law Formulation: Geometric Complexity Mapping ---
# Optimized parameters for NGC 1560 (LSB Spiral)
# Strength factor: 84, Curvature scale: 1.4
v_extra = 84 * (rad / (rad + 1.4)) 

# Resultant Velocity: Combining baryonic contribution with structural information force
v_ig = np.sqrt(v_disk**2 * 0.5 + v_extra**2) 

# --- Visualization ---
plt.figure(figsize=(10, 6))

# Plotting Observed Data
plt.scatter(rad, v_obs, color='red', s=45, edgecolors='black', label='Observations (NGC 1560)')

# Plotting Newtonian Prediction (Baseline)
plt.plot(rad, v_disk, '--', color='blue', alpha=0.3, label='Newtonian Prediction (Visible)')

# Plotting I-G Law Prediction (Information-Based Gravity)
plt.plot(rad, v_ig, color='green', linewidth=3, label='I-G Law Prediction (Final Strike)')

# Graph Metadata
plt.title('I-G Law Validation: NGC 1560 Rotation Curve')
plt.xlabel('Radius (kpc)')
plt.ylabel('Velocity (km/s)')
plt.ylim(0, 100)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Display Output
plt.show()
