import numpy as np

def exponential_inverse_transform(rate=2.0, n=10000):
    U = np.random.uniform(0, 1, size=n)
    X = -np.log(1 - U) / rate
    return X

samples = exponential_inverse_transform(rate=2.0, n=10000)
print(samples[:11])