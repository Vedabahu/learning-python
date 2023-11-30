import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # noqa: F401
# import scienceplots

# plt.style.use(['science', 'ieee', 'grid'])
plt.rcParams["text.usetex"] = True

# Single Points
ax = plt.axes(projection="3d")

x = np.arange(0, 2 * np.pi, 0.01)
y = np.arange(0, 2 * np.pi, 0.01)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X * 1.2) * np.cos(Y * 1.2)

ax.plot_surface(X, Y, Z, cmap="inferno")
ax.view_init(azim=55, elev=25)

plt.show()
