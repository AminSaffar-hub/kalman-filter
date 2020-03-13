# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:04:36 2019

@author: Amin Saffar
"""
import matplotlib.pyplot as plt
import numpy as np

class Car(object):
    def __init__(self,position,velocity,world,color='r'):
        self.status = [position,velocity]
        self.world = world
        self.color = color
        self.path = []
        self.path.append(position)
    def move(self,dt = 1):
        
        position = self.status[0]
        velocity = self.status[1]
        predicted_position = [position[0] + dt * velocity[0],position[1] + dt * velocity[1]]
        self.status = [predicted_position,velocity]
        self.path.append(predicted_position)
        
        
    def turn_left(self):
        velocity = self.status[1]
        self.status[1]=[velocity[1],-velocity[0]]


    def turn_right(self):
        velocity = self.status[1]
        self.status[1]=[-velocity[1],velocity[0]]
        
        
    def display_world(self):   
        # Store the current position of the car
        position = self.status[0]
        
        # Plot grid of values + initial ticks
        plt.matshow(self.world, cmap='gray')

        # Set minor axes in between the labels
        ax=plt.gca()
        rows = len(self.world)
        cols = len(self.world[0])

        ax.set_xticks([x-0.5 for x in range(1,cols)],minor=True )
        ax.set_yticks([y-0.5 for y in range(1,rows)],minor=True)

        # Plot grid on minor axes in gray (width = 2)
        plt.grid(which='minor',ls='-',lw=2, color='gray')

        # Create a 'x' character that represents the car
        # ha = horizontal alignment, va = verical
        ax.text(position[1], position[0], 'x', ha='center', va='center', color=self.color, fontsize=30)
            
        # Draw path if it exists
        if(len(self.path) > 1):
            # loop through all path indices and draw a dot (unless it's at the car's location)
            for pos in self.path:
                if(pos != position):
                    ax.text(pos[1], pos[0], '.', ha='center', va='baseline', color=self.color, fontsize=30)

        # Display final result
        #plt.show()
        plt.show(block=True) #modified for python console

        