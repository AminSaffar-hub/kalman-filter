# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:15:41 2019

@author: Amin Saffar
"""

def update(mean1, var1, mean2, var2): #var 1 and var 2 are already power 2
    new_mean = (1/((var1)+(var2)))*((var2)*mean1+(var1)*mean2)
    new_var = (1/((1/(var1))+(1/(var2))))
    return [new_mean, new_var]
def predict(mean1, var1, mean2, var2):
    new_mean =mean1+mean2
    new_var =var1+var2
    return [new_mean, new_var]

def localization(measurements , motion ,measurement_sig,motion_sig , mu, sig ):
    inf = update(mu,sig,measurements[0],measurement_sig)
    print(inf)
    mv_inf = predict(inf[0],inf[1],motion[0],motion_sig)
    print(mv_inf)
    for i in range(1,len(motion)):
        inf = update(mv_inf[0],mv_inf[1],measurements[i],measurement_sig)
        print(inf)
        mv_inf = predict(inf[0],inf[1],motion[i],motion_sig)
        print(mv_inf)
        
#print (predict(10.,4.,12.,4.))

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.
localization(measurements , motion ,measurement_sig,motion_sig , mu, sig )

