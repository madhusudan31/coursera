# Compute the derivative of a sin function using finite-difference method

import numpy as np
import matplotlib.pyplot as plt

xmax = 10.0                     # physical distance [Meter]
nx = 200                        # number of points
dx = xmax/(nx-1)                # grid spacing [Meter]
x = np.linspace(0,xmax,nx)      # x-coordinate

l = 40*dx                       # Wavelength [Meter]
k = 2 * np.pi/l                 # Wavenumber 1/[Meter]
f = np.sin(k*x)

nder = np.zeros(nx)             # numerical derivative
ader = np.zeros(nx)             # analytical derivative

for i in range(1, nx-1):
    nder[i] = (f[i+1] - f[i-1])/(2 * dx)

ader = k * np.cos(k*x)

ader[0] = 0.0
ader[nx-1] = 0.0

rms = np.sqrt(np.mean((nder-ader)**2))

plt.plot(x, nder, "b+", label="Numerical Result")
plt.plot(x, ader, "r-", label="Analytical result")

plt.xlabel("x, m")
plt.ylabel("der of sin(kx)")
plt.title("First derivative, Err (rms) = %.6f " % (rms))
plt.legend(loc="best")
plt.show()
