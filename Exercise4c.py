import pandas as pdb
import numpy as np

#import complete data set
df_complete = pd.read_csv('data/grant_complete.csv', comment='#')

# Drop duplicates
df_complete = df_complete.drop_duplicates(subset={'band', 'year'})

pd.drop_na
