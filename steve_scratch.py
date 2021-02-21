# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:28:40 2021

@author: s
"""
###################################
import numpy as np
import pandas as pd
# import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt

energy = pd.read_csv('h/energy.csv')
gdp_2016 = pd.read_csv('h/2016.csv')
gender = pd.read_csv('h/genderdata.csv')

energy.replace("nan", np.nan)
gdp_2016.replace("nan", np.nan)
energy.replace("nan", np.nan)
# %matplotlib inline
# msno.matrix(energy.sample(250))
# msno.bar(energy.sample(250))
# msno.heatmap(energy)
# msno.matrix(gender.sample(250))
# msno.bar(gender.sample(250))
# msno.heatmap(gender)
# msno.matrix(gdp_2016.sample(150))
# msno.bar(gdp_2016.sample(150))
# msno.heatmap(gdp_2016)


# energy = energy.drop(columns=['Code'])
energy = energy.set_index('Year')
# line = energy.plot.line(subplots=True,
#                         figsize = (9,9),
#                         layout =(2,2),
#                         legend  = True,
#                         )

hydro = energy[['Entity','Hydropower (terawatt-hours)']]
top_10_countries = hydro.groupby('Entity').sum().sort_values('Hydropower (terawatt-hours)', ascending=False)[1:10].index.values
hydro = hydro[hydro['Entity'].isin(top_10_countries)]
h = hydro.plot.line(title ='Top 10 Countries by Hydropower',
                    colormap  = 'PiYG',
                    legend=True,
                    )
hydro['Year'] = hydro.index
# Initialize the FacetGrid object
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(hydro, row="Entity", hue="Entity", aspect=15, height=.5, palette=pal)
# Draw the densities in a few steps
g.map(sns.kdeplot, "Year",
      bw_adjust=.5, clip_on=False,
      fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "Year", clip_on=False, color="w", lw=2, bw_adjust=.5)
g.map(plt.axhline, y=0, lw=2, clip_on=False)

# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)


g.map(label, "Year")

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=.25)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)

sns.relplot(data=hydro)
sns.lineplot(data=hydro)

solar = energy[['Entity','Solar (terawatt-hours)']]
top_10_countries = solar.groupby('Entity').sum().sort_values('Solar (terawatt-hours)', ascending=False)[1:10].index.values
solar = solar[solar['Entity'].isin(top_10_countries)]
s = solar.plot.line(title ='Top 10 Countries by Solarpower')

wind = energy[['Entity','Wind (terawatt-hours)']]
top_10_countries = wind.groupby('Entity').sum().sort_values('Wind (terawatt-hours)', ascending=False)[1:10].index.values
wind = wind[wind['Entity'].isin(top_10_countries)]
w = wind.plot.line(title ='Top 10 Countries by Windpower')

other = energy[['Entity','Other renewables (terawatt-hours)']]
top_10_countries = other.groupby('Entity').sum().sort_values('Other renewables (terawatt-hours)', ascending=False)[1:10].index.values
other = other[other['Entity'].isin(top_10_countries)]
o = other.plot.line(title ='Top 10 Countries by Other Renewables')
# ax = energy.plot.bar(x='Entity', y=['Solar (terawatt-hours)'], rot=0)


###################################
# Other stats

















