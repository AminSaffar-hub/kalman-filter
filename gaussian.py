# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:26:31 2019

@author: Amin Saffar
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def gaussian_density(x,mu,sigma):
    y=[]
    for k in x:
        y.append((1/np.sqrt(2*np.pi*np.power(sigma, 2.))) * np.exp(-np.power(k - mu, 2.) / (2 * np.power(sigma, 2.))))
    return y

def plot_gaussian(x, mu, sigma):

    y = gaussian_density(x, mu, sigma)

    plt.plot(x, y)
    plt.title('Gaussian Probability Density Function')
    plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.show()
def gaussian_probability(mean, stdev, x_low, x_high):
    return norm(loc = mean, scale = stdev).cdf(x_high) - norm(loc = mean, scale = stdev).cdf(x_low)
x = np.arange(1, 17, 0.5).tolist()
plot_gaussian(x,5,1)
