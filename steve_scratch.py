# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:28:40 2021

@author: s
"""
###################################
# Energy
# import numpy as np
import pandas as pd

gdp_2016 = pd.read_csv('h/2016.csv')
energy = pd.read_csv('h/energy.csv')
gender = pd.read_csv('h/gender_data.csv')


energy = energy.drop(columns=['Code'])
energy = energy.set_index('Year')
line = energy.plot.line()

hydro = energy[['Entity','Hydropower (terawatt-hours)']]
top_20_countries = hydro.groupby('Entity').sum().sort_values('Hydropower (terawatt-hours)', ascending=False)[1:20].index.values
h = hydro.plot.line()

solar = energy[['Entity','Solar (terawatt-hours)']]
top_20_countries = solar.groupby('Entity').sum().sort_values('Solar (terawatt-hours)', ascending=False)[1:20].index.values
s = solar.plot.line()

wind = energy[['Entity','Wind (terawatt-hours)']]
top_20_countries = wind.groupby('Entity').sum().sort_values('Wind (terawatt-hours)', ascending=False)[1:20].index.values
w = wind.plot.line()

other = energy[['Entity','Other renewables (terawatt-hours)']]
top_20_countries = other.groupby('Entity').sum().sort_values('Other renewables (terawatt-hours)', ascending=False)[1:20].index.values
o = other.plot.line()
# ax = energy.plot.bar(x='Entity', y=['Solar (terawatt-hours)'], rot=0)


###################################
# Womens Rights

rights = pd.read_csv('gender_data.csv')
















