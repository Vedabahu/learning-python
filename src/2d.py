import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# plt.style.use(["science", "grid", "ieee"])
plt.style.use("default")

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(1, 1, figsize=(5, 2.7), dpi=200)  # figsize=(10, 5.4)

ax.plot(x, y, "-m", label=r"$\sin(x)$")
ax.plot(x, y2, "--k", label=r"$\cos(x)$")

ax.legend()

ax.set_ylabel(r"$\sin \frac{x^2}{2}$")
ax.set_xlabel(r"Random numbers")
ax.set_title("A Graph")
fig.show()
