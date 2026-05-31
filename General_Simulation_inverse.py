import numpy as np
import matplotlib.pyplot as plt

# Exponential inverse transform
def exponential_inverse_transform(rate=2.0, n=10000):
    U = np.random.uniform(0, 1, size=n)
    return -np.log(1 - U) / rate


# Custom triangular distribution
def custom_triangular(n=10000):
    U = np.random.uniform(0, 1, size=n)

    return np.where(
        U <= 0.5,
        np.sqrt(2 * U),
        2 - np.sqrt(2 * (1 - U))
    )


exp_samples = exponential_inverse_transform(rate=2.0, n=10000)
tri_samples = custom_triangular(n=10000)


# # Plot exponential samples
# plt.figure()
# plt.hist(exp_samples, bins=50, density=True, alpha=0.7)

# x = np.linspace(0, 5, 300)
# plt.plot(x, 2.0 * np.exp(-2.0 * x))

# plt.title("Exponential Distribution using Inverse Transform")
# plt.xlabel("x")
# plt.ylabel("Density")
# plt.show()


# Plot triangular samples
plt.figure()
plt.hist(tri_samples, bins=50, density=True, alpha=0.7)

x1 = np.linspace(0, 1, 100)
x2 = np.linspace(1, 2, 100)

plt.plot(x1, x1)
plt.plot(x2, 2 - x2)

plt.title("Custom Triangular Distribution using Inverse Transform")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()