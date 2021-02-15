# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:28:40 2021

@author: s
"""

# import numpy as np
import pandas as pd

gdp_2016 = pd.read_csv('data/2016.csv')
energy = pd.read_csv('data/energy.csv')
gender = pd.read_csv('data/gender_data.csv')


energy = energy.drop(columns=['Code'])
energy = energy.set_index('Year')
line = energy.plot.line()

hydro = energy['Entity','Hydropower (terawatt-hours)']
h = hydro.plot.line()
# ax = energy.plot.bar(x='Entity', y=['Solar (terawatt-hours)'], rot=0)

