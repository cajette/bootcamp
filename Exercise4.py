"""
Exercise 4
making finch data tidy
"""

import pandas as pd
import numpy as np
import os

#Import files into their own DataFrame

df_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
df_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
df_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
df_1991 = pd.read_csv('data/grant_1991.csv', comment='#')
df_2012 = pd.read_csv('data/grant_2012.csv', comment='#')

# Change column name of yearband to year on 1973 data
# Original columns: band   species  yearband  beak length  beak depth
df_1973 = df_1973.rename(columns={'yearband': 'year'})

# Change the 1973 date from 73 to 1973
df_1973['year'] = 1973

# Add date column to all the other dataframes
df_1975['year'] = 1975
df_1987['year'] = 1987
df_1991['year'] = 1991
df_2012['year'] = 2012

# Rename other columns files
df_1973 = df_1973.rename(columns={'beak length': 'beak length (mm)',
                                  'beak depth': 'beak depth (mm)'})

df_1975 = df_1975.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})

df_1987 = df_1987.rename(columns={'Beak length, mm': 'beak length (mm)',
                                  'Beak depth, mm': 'beak depth (mm)'})

df_1991 = df_1991.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})

df_2012 = df_2012.rename(columns={'blength': 'beak length (mm)',
                                  'bdepth': 'beak depth (mm)'})


# Reorder 73, 75, 87, 91, 2012 df's
df_1973 = df_1973[['band', 'species', 'beak length (mm)', 'beak depth (mm)',
                   'year']]

df_1975 = df_1975[['band', 'species', 'beak length (mm)', 'beak depth (mm)',
                   'year']]

df_1987 = df_1987[['band', 'species', 'beak length (mm)', 'beak depth (mm)',
                   'year']]

df_1991 = df_1991[['band', 'species', 'beak length (mm)', 'beak depth (mm)',
                   'year']]

df_2012 = df_2012[['band', 'species', 'beak length (mm)', 'beak depth (mm)',
                   'year']]


# Concatenate the dataframes into a single dataframes
df_grant = pd.concat((df_1973, df_1975, df_1987, df_1991, df_2012), ignore_index=True)
# axis is row vs column
#kwarg axis=0 is rows, axis=1 is column
#for pd.concat function, tells it where the data will be added
#goal is for index to be meaningful across the row (aka all the stuff applies to same trial/sample)

# Save concatenated data as csv file
os.path.isfile(df_grant.csv)
df_grant.to_csv('df_grant.csv')
