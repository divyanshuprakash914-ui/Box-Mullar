import numpy as np
def box_muller(n=10000):  # This means we are creating 10000 random values of z1 and z2.
    U1 = np.random.uniform(1e-12, 1, size=n)
    U2 = np.random.uniform(0, 1, size=n)

    R = np.sqrt(-2 * np.log(U1))
    theta = 2 * np.pi * U2

    Z1 = R * np.cos(theta)
    Z2 = R * np.sin(theta)

    return Z1 , Z2


Z1, Z2 = box_muller(n=10000)

print("Mean of Z1 :", np.mean(Z1))
print("Variance of Z1 :", np.var(Z1))
print("Mean of Z2 :", np.mean(Z2))
print("Variance of Z2 :", np.var(Z2))
