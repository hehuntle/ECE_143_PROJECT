# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:28:40 2021

@author: s
"""
###################################
# Energy
# import numpy as np
import pandas as pd
import missingno as msno

energy = pd.read_csv('h/energy.csv')
gdp_2016 = pd.read_csv('h/2016.csv')
# gender = pd.read_csv('h/gender_data.csv')
# %matplotlib inlines
msno.matrix(energy.sample(250))
msno.matrix(gdp_2016.sample(150))


energy = energy.drop(columns=['Code'])
energy = energy.set_index('Year')
line = energy.plot.line()

hydro = energy[['Entity','Hydropower (terawatt-hours)']]
top_10_countries = hydro.groupby('Entity').sum().sort_values('Hydropower (terawatt-hours)', ascending=False)[1:10].index.values
hydro = hydro[hydro['Entity'].isin(top_10_countries)]
h = hydro.plot.line()

solar = energy[['Entity','Solar (terawatt-hours)']]
top_10_countries = solar.groupby('Entity').sum().sort_values('Solar (terawatt-hours)', ascending=False)[1:10].index.values
solar = solar[solar['Entity'].isin(top_10_countries)]
s = solar.plot.line()

wind = energy[['Entity','Wind (terawatt-hours)']]
top_10_countries = wind.groupby('Entity').sum().sort_values('Wind (terawatt-hours)', ascending=False)[1:10].index.values
wind = wind[wind['Entity'].isin(top_10_countries)]
w = wind.plot.line()

other = energy[['Entity','Other renewables (terawatt-hours)']]
top_10_countries = other.groupby('Entity').sum().sort_values('Other renewables (terawatt-hours)', ascending=False)[1:10].index.values
other = other[other['Entity'].isin(top_10_countries)]
o = other.plot.line()
# ax = energy.plot.bar(x='Entity', y=['Solar (terawatt-hours)'], rot=0)


###################################
# Womens Rights
















