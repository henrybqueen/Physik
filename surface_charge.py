import numpy as np
from math import pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Number of divisions for the grid
steps = 1000  # Adjust this for smoother plots

# Create linearly spaced values for theta and phi
t = np.linspace(0, 2 * pi, steps)
p = np.linspace(0, pi, steps)


# Use torch.meshgrid to create a grid of theta and phi values
theta, phi = np.meshgrid(t, p, indexing="ij")

# Define the parametrization function
def X(theta, phi):
    return np.stack([
        np.sin(phi) * np.cos(theta),
        np.sin(phi) * np.sin(theta),
        np.cos(phi)
    ], axis=-1)

# Compute the parametrization on the grid
S = X(theta, phi)





X_theta = np.gradient(S, t, axis=0)
X_phi = np.gradient(S, p, axis=1)


N = np.cross(X_theta, X_phi)

Norm = np.linalg.norm(N, axis=-1)


dt = t[1]-t[0]
dp = p[1]-p[0]

Area = np.sum(Norm) * dt * dp
print(Area)

















