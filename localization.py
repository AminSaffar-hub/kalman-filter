# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:07:31 2019

@author: Amin Saffar

"""
import numpy as np
world = ['green','red','red','green','green']
z = ['red','red']
motions=[1,1]
n = 5
p_x =[1.0/n for x in range (0,n)]
p_Hit, p_Miss = 0.6,0.2
p = [0,1,0,0,0]
p_exact = 0.8
p_undershoot = 0.1
p_overshoot = 0.1 

def move(p,U):
    q=np.zeros(len(p))
    for i in range (len(p)):
        q[i] += (p[(i-U) % len(p)]) * p_exact 
        q[i] += (p[(i-U-1) % len(p)]) * p_undershoot
        q[i] += (p[(i-U+1) % len(p)]) * p_overshoot
    return(q)

def sense(p_x,world,z):
    p_Hit, p_Miss = 0.6,0.2
    n = len(world)
    for j in range(0,n):
            hit = (z == world[j])
            p_x[j] = p_x[j] * (hit *p_Hit + (1-hit)*p_Miss)
    s = sum(p_x)
    p_x =[x/s for x in p_x]
    return p_x
        

def sense_and_move(p_x,world,z,motions):
    n = len(z)
    for i in range (0,n):
        p_x=sense(p_x,world,z[i])
        p_x=move(p_x,motions[i])
    return(p_x)
    





print(sense_and_move(p_x,world,z,motions))
