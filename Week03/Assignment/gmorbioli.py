# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 16:46:29 2018

@author: morbi
"""

#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt, matplotlib,numpy as np

#creating the dataframes - MAKE SURE YOU'RE IN THE SAME DIRECTORY OF THE FILES
surveys_df = pd.read_csv("surveys.csv",
                         keep_default_na=False, na_values=[""])

species_df = pd.read_csv("species.csv",
                         keep_default_na=False, na_values=[""])


#creating the merged document containing the info from both documents
merged_inner = pd.merge(left=surveys_df,right=species_df, 
                        left_on='species_id', right_on='species_id')

#merged_inner.to_csv('out.csv', index=False) #save a .csv of the merged data

#plot the figure
def figure_bar(arg, title = None):
    '''  Plots a bar graph using the dataset provided'''

    axes = arg
    axes.set_xlabel('plot_id') #gives name to the x-axis
    axes.set_ylabel('Number of counts') #gives name to the y-axis
    axes.set_title(title) #gives a title to the graph
    
    # Only show ticks on the left and bottom spines
    axes.yaxis.set_ticks_position('left')
    axes.xaxis.set_ticks_position('bottom')
    
    #places the legend outside the plot
    axes.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, shadow=True, ncol=1)

    plt.show() # shows the figure

    
dataset = merged_inner.groupby(['plot_id','taxa']) #groups the dataset by the site and the taxa
Counts_PT = dataset.count()['record_id'] #count the number of obs for the grouped data
axes1 = Counts_PT.unstack().plot(kind='bar', stacked=True) #plots the bar graph, stacking the data

datasetMF = merged_inner.groupby(['plot_id','taxa','sex']) #groups the dataset by the site and the taxa and the sex
Counts_PTMF = datasetMF.count()['record_id'] #count the number of obs for the grouped data
axes2 = Counts_PTMF.unstack(level=[1, 2]).plot(kind='bar', stacked=True) #plots the bar graph, stacking the data

figure_bar(axes1,'Number of species of each taxa per site')
figure_bar(axes2,'Number of species of each taxa per site per sex')
