import numpy as np

def custom_triangular(n=10000):
    U = np.random.uniform(0, 1, size=n)

    X = np.where(
        U <= 0.5,
        np.sqrt(2 * U),
        2 - np.sqrt(2 * (1 - U))
    )

    return X

samples = custom_triangular(n=10000)
print(samples[:10])