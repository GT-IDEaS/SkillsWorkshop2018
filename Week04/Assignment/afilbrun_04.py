
# coding: utf-8

# In[135]:


import numpy as np
import matplotlib.pyplot as plt


# In[136]:


from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)


# In[137]:


m, n = X.shape
print('X shape = ', (m,n))
print(str(m) + ' examples, ' + str(n) + ' features/variables')
print('There are ' + str(np.unique(y)) + ' classes.')


# In[138]:


X -= np.mean(X, axis = 0, keepdims = True) #broadcasting 

def generatePCS(X):
    m,n = X.shape
    U,s,Vt = np.linalg.svd(X)
    print(U.shape)
    S = np.concatenate((np.diag(s),np.zeros((m-n,n))), axis = 0)
    print(S.shape)
    print(Vt.shape)
    PCs = np.dot(U,S)
    return (PCs, s)

from utils import PlotPC1PC2 #Loading a helper function to plot and save time
PCs, s = generatePCS(X)
PlotPC1PC2(PCs, y)


# In[139]:


print(np.max(X, axis= 0))
print (np.min(X, axis = 0))


# In[140]:


X /= np.std(X, axis = 0, keepdims = True)

PCs, s = generatePCS(X)
PlotPC1PC2(PCs, y)


# In[141]:


scaled_eigenvalues = s**2/np.sum(s**2)


# In[173]:


def describe_variance_2(scaled_eigenvalues, thresh):
    eig_sum = 0
    reduced_dataset = []
    for i in range(len(scaled_eigenvalues)):
        reduced_dataset.append(X[:,i])
        eig_sum += scaled_eigenvalues[i]
        if eig_sum >= thresh:
            break
    reduced_dataset = np.array(reduced_dataset).transpose()
    np.savetxt("a_filbrun_dataset.csv", reduced_dataset, delimiter=",")
    print(str(eig_sum*100) + '% of the variance is describe by ' + str(i+1) + ' components.')


# In[174]:


reduced_dataset = describe_variance_2(scaled_eigenvalues, thresh = 0.90)

