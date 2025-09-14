import numpy as np
import matplotlib.pyplot as plt

# Parameters
T_ref = 60.0     # ambient temperature (F)
T0 = 90.0        # initial temperature (F)
T10 = 88.0       # temperature at t=10 min (F)

# Determine k from T(10) = 88 = 60 + 30 e^(10 k)
k = (1/10.0) * np.log((T10 - T_ref) / (T0 - T_ref))

def T(t):
    """Temperature (F) at time t (minutes) under Newton's law of cooling."""
    return T_ref + (T0 - T_ref) * np.exp(k * t)

# Values to report
T20 = T(20.0)
t_to_65 = np.log(1/6.0) / k  # solve 65 = 60 + 30 e^{k t}

# Print key numbers
print(f"k = {k:.6f} per minute")
print(f"T(20 min) = {T20:.4f} F")
print(f"Time to reach 65 F ≈ {t_to_65:.2f} minutes (≈ {t_to_65/60:.2f} hours)")

# Plot
t = np.linspace(0, max(300, t_to_65*1.05), 600)
plt.figure()
plt.plot(t, T(t))
plt.scatter([0, 10, 20, t_to_65], [T(0), T(10), T20, 65])
plt.title("Problem 16: Newton's Cooling (Ambient 60°F)")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.tight_layout()
plt.show()
