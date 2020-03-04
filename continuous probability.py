# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:10:54 2019

@author: Amin Saffar
"""
from matplotlib import pyplot as plt



def bar_heights(intervals, probabilities, total_probability):

    heights = []

    total_relative_prob = sum(probabilities)

    for i in range(0, len(probabilities)):
        bar_area = (probabilities[i] / total_relative_prob) * total_probability
        heights.append(bar_area / (intervals[i + 1] - intervals[i]))

    return heights
def plot_density(liste,intervals):
      width_table=[]
      nintervals = intervals[:-1]
      for i in range (0,len(intervals)):
            if i != 0:
                width = intervals[i]-intervals[i-1]
                width_table.append(width)
      plt.bar(nintervals,liste,width=width_table,align='edge')
      plt.ylim(0, max(liste))
      plt.title(' probablity density')
      plt.xlim(min(intervals),max(intervals))
      plt.show()  
        



hour_intervals = [0, 5, 10, 16, 21, 24]
intervals = [0, 5, 10, 16, 21]

relative_probabilities = [1, 5, 3, 6, 0.5]

total_probability = 0.05


liste = bar_heights(hour_intervals,relative_probabilities,total_probability)
print(liste)
plot_density(liste,hour_intervals)



