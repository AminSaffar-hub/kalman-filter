# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:40:23 2019

@author: Amin Saffar
"""

def predict_state(state, dt):
    # Assume that state takes the form [x, vel] i.e. [0, 50]
    
    ## TODO: Calculate the new position, predicted_x
    ## TODO: Calculate the new velocity, predicted_vel
    ## These should be calculated based on the contant motion model:
    ## distance = x + velocity*time
    
    predicted_x = 0
    predicted_vel = 0
    predicted_x  = state[1] * dt +state[0]
    predicted_vel = state[1]
    
    # Constructs the predicted state and returns it
    predicted_state = [predicted_x, predicted_vel]
    return predicted_state


## TODO: Click Test Run!

# A state and function call for testing purposes - do not delete
# but feel free to change the values for the test variables
test_state = [10, 3]
test_dt = 5

test_output = predict_state(test_state, test_dt)
print(test_output)