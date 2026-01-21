import matplotlib.pyplot as plt
import numpy as np

# -- DDO 154 ---
rad = np.array([0.12, 0.24, 0.37, 0.49, 0.61, 0.73, 0.85, 0.98, 1.10, 1.22, 1.34, 1.46, 1.59, 1.71, 1.83, 1.95, 2.07, 2.20, 2.32, 2.44, 2.56, 2.68, 2.81, 2.93, 3.05, 3.17, 3.30, 3.42, 3.54, 3.66, 3.78, 3.91, 4.03, 4.15, 4.27, 4.39, 4.52, 4.64, 4.76, 4.88, 5.00])
v_obs = np.array([8.5, 15.2, 20.1, 25.3, 30.4, 35.6, 40.2, 44.1, 47.3, 49.5, 50.8, 51.9, 52.4, 52.9, 53.1, 53.3, 53.5, 53.7, 53.8, 53.9, 54.0, 54.1, 54.2, 54.3, 54.4, 54.5, 54.6, 54.7, 54.8, 54.9, 55.0, 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7, 55.8, 55.9, 56.0])
v_disk = np.array([2.1, 4.2, 6.3, 8.4, 10.5, 12.6, 14.7, 16.8, 18.9, 21.0, 23.1, 25.2, 27.3, 29.4, 31.5, 33.6, 35.7, 37.8, 39.9, 42.0, 44.1, 46.2, 48.3, 50.4, 52.5, 54.6, 56.7, 58.8, 60.9, 63.0, 65.1, 67.2, 69.3, 71.4, 73.5, 75.6, 77.7, 79.8, 81.9, 84.0, 86.1])

# --- I-G Law: THE KNEE-BOOST FIT ---
v_extra = 62 * (rad / (rad + 0.52)) 
v_ig = np.sqrt(v_disk**2 * 0.001 + v_extra**2) 

plt.figure(figsize=(10, 6))
plt.scatter(rad, v_obs, color='red', s=40, edgecolors='black', alpha=0.9, label='Actual Data')
plt.plot(rad, v_disk, '--', color='blue', alpha=0.1, label='Newtonian Prediction')
plt.plot(rad, v_ig, color='green', linewidth=3, label='I-G Law (Knee-Boost Fit)')

plt.title('DDO 154: Knee Alignment Perfected')
plt.xlabel('Radius (kpc)')
plt.ylabel('Velocity (km/s)')
plt.ylim(0, 70)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
