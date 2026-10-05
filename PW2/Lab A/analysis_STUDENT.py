"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", np.mean(a))
print("Std of acceleration:", a.std())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_int = cumulative_trapezoid(a, t, initial=0) + v[0]
y_int = cumulative_trapezoid(v_int, t, initial=0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axs[0].plot(t, y, label="measured")
axs[0].plot(t, y_int, "--", label="integrated")
axs[0].set_ylabel("position (m)")
axs[0].legend()

axs[1].plot(t, v, label="from gradient")
axs[1].plot(t, v_int, "--", label="integrated")
axs[1].set_ylabel("velocity (m/s)")
axs[1].legend()

axs[2].plot(t, a, label="from gradient")
axs[2].axhline(-9.81, color="r", linestyle="--", label="true -9.81")
axs[2].set_ylabel("acceleration (m/s^2)")
axs[2].set_xlabel("time (s)")
axs[2].legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)
print("Max position error after integration:", np.max(np.abs(y_int - y)))
