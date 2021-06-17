# ACTIVIDAD
# ---------

import numpy as np

def sigmoide(x, w):
    z = np.dot(x, w.T)
    print(x.shape, w.shape, z.shape, w.T.shape)
    return 1/(1+np.exp(-z))

x = np.array([[ 0., -0.80204467, -1.18935522], [ 0.,  0.75579627, -1.36645791]])
w = np.random.normal(loc=4e-4, scale=1e-5, size=(1, x.shape[1]))

print(sigmoide(x, w))