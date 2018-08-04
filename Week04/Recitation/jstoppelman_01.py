import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from utils import PlotPC1PC2

def generatePCS(X):
    m,n = X.shape
    U, s, Vt = np.linalg.svd(X)
    print(U.shape)
    S = np.concatenate((np.diag(s), np.zeros((m-n, n))), axis = 0)
    print(S.shape)
    print(Vt.shape)
    PCs = np.dot(U, S)
    return (PCs, s)
def describe_variance(scaled_eigenvalues, thresh):
    eig_sum = 0
    for i in range(len(scaled_eigenvalues)):
        eig_sum += scaled_eigenvalues[i]
        if eig_sum >= thresh:
            break
    print(str(eig_sum*100) + '% of the variance is described by ' + str(i+1) + ' components.')

X, y = load_wine(return_X_y=True)
m, n = X.shape
index=[8,9,10,11,12]
Y=np.delete(X,index,axis=1)
m,n=Y.shape
print((m,n))
Y -= np.mean(Y, axis = 0, keepdims=True)
PCs, s = generatePCS(Y)
PlotPC1PC2(PCs, y)

print(np.max(Y, axis = 0))
print(np.min(Y, axis = 0))
Y /= np.std(Y, axis = 0, keepdims=True)
scaled_eigenvalues = s**2/np.sum(s**2)
_ = np.arange(len(s)) + 1
plt.plot(_, scaled_eigenvalues)
plt.show()

np.savetxt("week4.csv", Y, delimiter=",")

