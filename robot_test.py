# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:24:49 2019

@author: Amin Saffar
"""
import numpy as np

world = np.array ([ ['o', 'b', 'o', 'o', 'b'],
                    ['o', 'o', 'b', 'o', 'o'],
                    ['b', 'o', 'o', 'b', 'o'],
                    ['b', 'o', 'o', 'o', 'o'] ])

measurement = ['b', 'o']


def find_match(world,measurement):
    possible_locations= []
    col = world.shape[1]
    row = world.shape[0]
    for i in range(0,row):
        for j in range(0,col):
            if j < col-1:
                if (measurement[0] == world[i][j]) and (measurement[1] == world[i][j+1]):
                    possible_locations.append([i,j])
    return (possible_locations)
locations = find_match(world,measurement)
print(locations)
                
            

