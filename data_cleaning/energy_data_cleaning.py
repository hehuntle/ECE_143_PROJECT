# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:56:11 2021

@author: s
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from collections import defaultdict
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

energy = pd.read_csv('https://raw.githubusercontent.com/stekim/ECE_143_PROJECT/main/h/energy.csv')
gdp_2016 = pd.read_csv('https://raw.githubusercontent.com/stekim/ECE_143_PROJECT/main/h/2016.csv')
energy = energy.set_index('Entity').join(gdp_2016.set_index('Country'))
continents = ['Asia Pacific','South & Central America','North America','Europe','World','Europe (Other)']
data = energy[~energy.index.isin(continents)]
data = data.reset_index()
data.rename(columns={"index": "Country"}, inplace=True)

data = data[['Year','Hydropower (terawatt-hours)',
       'Solar (terawatt-hours)', 'Wind (terawatt-hours)',
       'Other renewables (terawatt-hours)',
       'Economy (GDP per Capita)', 'Country']]

data = data[data['Year']==2016]

leg = ['75% percentile in GDP',
     '50% percentile in GDP',
     '75% percentile in GDP',
     'Top 25% percentile in GDP',
     'No Data Available']

m = ['Year',
           'Hydropower (terawatt-hours)',
           'Solar (terawatt-hours)',
           'Wind (terawatt-hours)',
           'Other renewables (terawatt-hours)',
           'Economy (GDP per Capita)']
def label_country(row):
  if row['Economy (GDP per Capita)'] <= 1.417 and row['Economy (GDP per Capita)'] > 1.23:
     return 'royalblue'
  if row['Economy (GDP per Capita)'] <= 1.23 and row['Economy (GDP per Capita)'] > 1.05:
     return 'cornflowerblue'
  if row['Economy (GDP per Capita)'] < 1.05:
     return 'lightsteelblue'
  if row['Economy (GDP per Capita)'] > 1.417:
    return 'darkblue'
  else:
    return 'silver'

data['color_code'] = data.apply (lambda row: label_country(row), axis=1)
#####GDP ####
GDP_categories = []

# split countries into their groups
for item in data['Economy (GDP per Capita)']:
    category = ''
    if item < 1.08:
        category = 'Lower 25% percentile in GDP'
    elif item < 1.25:
        category = '50% percentile in GDP'
    elif item < 1.42:
        category = '75% percentile in GDP'
    elif item > 1.42:
        category = 'Top 25% percentile in GDP'
    else:
        category = 'No Data Available'
    GDP_categories.append(category)
data['gdp_perc'] = GDP_categories

figure(num=None, figsize=(18, 12), dpi=180, facecolor='w', edgecolor='w')