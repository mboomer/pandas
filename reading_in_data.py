# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:10:34 2020

@author: Marie Hillock
"""

import pandas as pd

# read data from excel spreadsheet tracks
tracks = pd.read_excel('tracks.xlsx', sheet_name='Tracks')

print(tracks)

# print the columns
print(tracks.columns)
# print a single columns
print(tracks['Name'])

# print the columns
print(tracks.columns)
print(tracks['Milliseconds'])


# read data from CSV file
flights = pd.read_csv('flights.csv')
print(flights)

# note that columns are offset
# panda tries to use the first column as an index 
# we dont want that 

flights = pd.read_csv('flights.csv', index_col=False)
print(flights)

