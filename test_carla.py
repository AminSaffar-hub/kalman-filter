# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:43:14 2019

@author: Amin Saffar
"""
import numpy as np 
from car_class import Car 


height = 4
width = 6 
initial_position= [0,0]
initial_velocity = [0,1]
world = np.zeros((height,width))


carla = Car(initial_position,initial_velocity,world)
carla.move()
carla.move()
carla.turn_left()
carla.move()
carla.turn_right()
carla.move()
carla.move()
carla.turn_right()
carla.move()
carla.display_world()


initial_velocity = [1,0]
world = np.zeros((height,width))
eya = Car(initial_position,initial_velocity,world,'y')
eya.move()
eya.move()
eya.turn_right()
eya.move()
eya.turn_left()
eya.move()
eya.turn_right()
eya.move()
eya.display_world()