# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:37:46 2019

@author: Sheth_Smit
"""
import numpy as np
from scipy.special import gamma as G
from matplotlib import pyplot as plt

N = 160

M = np.random.rand()
while M >= 0.4 and M <= 0.6:
    M = np.random.rand()
print("μML = ", M)

data = np.concatenate((np.ones(int(M * N)), np.zeros(N - int(M * N))))
np.random.shuffle(data)

a = 1.5
b = 2.5


def get_post_prob(M, a, b, m, l):
    gamma_part = G(m + a + l + b) / (G(m + a) * G(l + b))
    bern_part = M**(m + a - 1) * (1-M)**(l + b - 1)
    return gamma_part * bern_part

def plot(a, b, m, l, index):
    mu = 0
    
    P = []
    x_M = []
    
    for i in range(100):
        post_prob = get_post_prob(mu, a, b, m, l)
        P.append(post_prob)
        x_M.append(mu)
        mu += 0.01
        
    print("Graph for <a, b, M> as", a+m, b+l, (a+m)/(a+m+b+l))
    plt.plot(x_M, P)
    plt.xlim(0.0, 1.0)
    plt.ylim(bottom=0.0, top = max(P)+2)
    plt.xlabel('μ')
    plt.ylabel('P')
    plt.text(0.4, max(P)+1, "μML = " + str(round(M, 4)))
    plt.show()
    #path = "./plots/Sequential_" + str(index) + ".png"
    #plt.savefig(path)
    #plt.close()

def sequential():
    m = 0
    l = 0
    plot(a, b, m, l, 0)
    for i in range(1, N+1):
        if data[i-1] == 1:
            m += 1
        else:
            l += 1
        
        if i % 20 == 0:
            plot(a, b, m, l, i)
            
def entire():
    m = 0
    l = 0
    
    for i in range(N):
        if data[i] == 1:
            m += 1
        else:
            l += 1
            
    plot(a, b, m, l, N)
            
if __name__ == '__main__':
    sequential()
    print("Entire data together (Part B)")
    entire()