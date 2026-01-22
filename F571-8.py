import matplotlib.pyplot as plt
import numpy as np

# --- Galaxy F571-8 Data (Source: SPARC Database) ---
rad = np.array([0.22, 0.78, 1.33, 2.33, 3.44, 3.78, 4.77, 5.44, 6.11, 7.22, 9.33, 11.1, 15.55])
v_obs = np.array([12.4, 37.5, 56.5, 69.1, 85.5, 87.1, 105.0, 112.0, 116.0, 124.0, 135.0, 140.0, 144.0])
v_disk = np.array([38.29, 85.69, 104.0, 114.45, 107.32, 103.7, 92.03, 86.43, 81.42, 76.23, 68.45, 64.24, 55.43])

# --- I-G Law Re-Calibration for LSB Systems ---
# Reduced alpha and adjusted complexity slope for low-density galaxies
v_target = 150.0
# Adjusted the '0.5' and '2.8' to better match the LSB distribution
v_extra = v_target * (rad**1.5 / (rad**1.5 + 3.9))
v_ig = np.sqrt(v_disk**2 * 0.15 + v_extra**2) 

# --- Professional Plotting Configuration ---
plt.figure(figsize=(10, 6))

# Observed Data Points (Fixed the error by using scatter correctly)
plt.scatter(rad, v_obs, color='red', s=50, edgecolors='black', alpha=0.9, label='Actual Observations (F571-8)')

# Standard Newtonian Model
plt.plot(rad, v_disk, '--', color='blue', alpha=0.5, label='Newtonian Prediction')

# I-G Law Prediction (The New Optimized Fit)
plt.plot(rad, v_ig, color='green', linewidth=3, label='I-G Law Optimized Fit')

plt.title('I-G Law Series #6: Re-Calibrated F571-8', fontsize=14)
plt.xlabel('Radius (kpc)')
plt.ylabel('Velocity (km/s)')
plt.ylim(0, 180)
plt.legend(loc='lower right')
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

print("Status: I-G Law re-calibrated for LSB galaxy density.")
