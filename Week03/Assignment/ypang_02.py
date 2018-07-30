#!/bin/env python

########################################
#      Challenge- More functions       #
########################################

import pandas as pd


def one_year_csv_writer(this_year, all_data, directory, root):
    """
    Writes a csv file for data from a given year.

    this_year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """
    ###### Q4 CHANGE HERE #####
    print("in one: " + random_variable)
    #print("in one: " + random_variable2) << This will cause error
    ###########################

    # Select data for the year
    surveys_year = all_data[all_data.year == this_year]

    # Write the new DataFrame to a csv file
    ###### Q1 CHANGE HERE #####
    filename = directory + "/" + root + str(this_year) + '.csv'
    ###########################
    surveys_year.to_csv(filename)
    ###### Q3 CHANGE HERE #####
    print(filename + " written.")
    ###########################

def yearly_data_csv_writer(start_year, end_year, all_data, directory, root):
    """
    Writes separate CSV files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    """
    ###### Q4 CHANGE HERE #####
    print("in yearly: " + random_variable)
    random_variable2 = "hey"
    print("in yearly: " + random_variable2)
    ###########################

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        ###### Q1 CHANGE HERE #####
        one_year_csv_writer(year, all_data, directory, root)
        ###########################



"""  MAIN   """

# Load the data into a DataFrame
surveys_df = pd.read_csv('data/surveys.csv')

# Q2
yearly_data_csv_writer(1977, 1977, surveys_df, "data/yearly_files/",
        "function_surveys")  # extracted 1977 only

###### Q4 CHANGE HERE #####
random_variable = "hello"
print("in main: " + random_variable)
###########################

