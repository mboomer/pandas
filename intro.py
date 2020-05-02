# -*- coding: utf-8 -*-
"""
Created on Sat May  2 08:42:18 2020

@author: Mark Boomer
"""

import pandas as pd
import numpy as np

# create a python dictionary with each key having a arrray of 5 random values
df_data = {
    'col1': np.random.rand(5),
    'col2': np.random.rand(5),
    'col3': np.random.rand(5),
    'col4': np.random.rand(5)
}
print(df_data)

# DataFrame: create a 2D table with rows and colums from the python dictionary
df = pd.DataFrame(df_data)

print(df)

# indices start at 0 and go up to but don’t include the final stated index
# print first 2 rows
print(df[:2])
# print 3rd and 4th rows
print(df[2:4])
# print first row
print(df[:1])

# print column 1 - specify column name in string literal
print(df['col1'])
# print column 2 & 3 - note the list of columns are in an array so
# we need the double brackets
print(df[
    ['col2','col3']
    ]
)
# print columns in different order
print(df[
    ['col3','col1','col4']
    ]
)

