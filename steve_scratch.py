# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:28:40 2021

@author: s
"""
###################################
### top countries by GDP
### or choose 2016 and plot everything
import numpy as np
import pandas as pd
# import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt

energy = pd.read_csv('h/energy.csv')
gdp_2016 = pd.read_csv('h/2016.csv')
gender = pd.read_csv('h/genderdata.csv')
gender.replace("nan",np.nan)

energy.replace("nan", np.nan)
gdp_2016.replace("nan", np.nan)
energy.replace("nan", np.nan)


gdp_2016 = gdp_2016[['Country','Economy (GDP per Capita)']]
# %matplotlib inline
# msno.matrix(energy.sample(250))
# msno.bar(energy.sample(250))
# msno.heatmap(energy)
# msno.matrix(gender.sample(250))
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
cont = ['Asia Pacific','South & Central America','North America']
hydro = hydro[~hydro['Entity'].isin(cont)]
hydro['year'] = hydro.index
hydro = hydro.set_index('Entity').join(gdp_2016.set_index('Country'))
hydro['Entity'] = hydro.index
top_10_countries = hydro.groupby('Entity').sum().sort_values('Hydropower (terawatt-hours)', ascending=False)[1:10].index.values
hydro = hydro[hydro['Entity'].isin(top_10_countries)]
hydro = hydro.set_index('year')
plt.figure()
sns.lineplot(data=hydro, x=hydro.index, y='Hydropower (terawatt-hours)', hue='Economy (GDP per Capita)').set_title('Top 10 Countries by Hydropower')

# solar = energy[['Entity','Solar (terawatt-hours)']]
# cont = ['Asia Pacific','South & Central America','North America']
# solar = solar[~solar['Entity'].isin(cont)]
# top_10_countries = solar.groupby('Entity').sum().sort_values('Solar (terawatt-hours)', ascending=False)[1:10].index.values
# solar = solar[solar['Entity'].isin(top_10_countries)]
# plt.figure()
# sns.lineplot(data=solar, x=solar.index, y='Solar (terawatt-hours)', hue='Entity').set_title('Top 10 Countries by Solar')

solar = energy[['Entity','Solar (terawatt-hours)']]
cont = ['Asia Pacific','South & Central America','North America']
solar = solar[~solar['Entity'].isin(cont)]
solar['year'] = solar.index
solar = solar.set_index('Entity').join(gdp_2016.set_index('Country'))
solar['Entity'] = solar.index
top_10_countries = solar.groupby('Entity').sum().sort_values('Solar (terawatt-hours)', ascending=False)[1:10].index.values
solar = solar[solar['Entity'].isin(top_10_countries)]
solar = solar.set_index('year')
plt.figure()
sns.lineplot(data=solar, x=solar.index, y='Solar (terawatt-hours)', hue='Economy (GDP per Capita)').set_title('Top 10 Countries by Solar')
###

# wind = energy[['Entity','Wind (terawatt-hours)']]
# cont = ['Asia Pacific','South & Central America','North America']
# wind = wind[~wind['Entity'].isin(cont)]
# top_10_countries = wind.groupby('Entity').sum().sort_values('Wind (terawatt-hours)', ascending=False)[1:10].index.values
# wind = wind[wind['Entity'].isin(top_10_countries)]
# plt.figure()
# sns.lineplot(data=wind, x=wind.index, y='Wind (terawatt-hours)', hue='Entity').set_title('Top 10 Countries by Wind')

wind = energy[['Entity','Wind (terawatt-hours)']]
cont = ['Asia Pacific','South & Central America','North America']
wind = wind[~wind['Entity'].isin(cont)]
wind['year'] = wind.index
wind = wind.set_index('Entity').join(gdp_2016.set_index('Country'))
wind['Entity'] = wind.index
top_10_countries = wind.groupby('Entity').sum().sort_values('Wind (terawatt-hours)', ascending=False)[1:10].index.values
wind = wind[wind['Entity'].isin(top_10_countries)]
wind = wind.set_index('year')
plt.figure()
sns.lineplot(data=wind, x=wind.index, y='Wind (terawatt-hours)', hue='Economy (GDP per Capita)').set_title('Top 10 Countries by Wind')

# other = energy[['Entity','Other renewables (terawatt-hours)']]
# cont = ['Asia Pacific','South & Central America','North America']
# other = other[~other['Entity'].isin(cont)]
# top_10_countries = other.groupby('Entity').sum().sort_values('Other renewables (terawatt-hours)', ascending=False)[1:10].index.values
# other = other[other['Entity'].isin(top_10_countries)]
# plt.figure()
# sns.lineplot(data=other, x=other.index, y='Other renewables (terawatt-hours)', hue='Entity').set_title('Top 10 Countries by Other Renewables')

other = energy[['Entity','Other renewables (terawatt-hours)']]
cont = ['Asia Pacific','South & Central America','North America']
other = other[~other['Entity'].isin(cont)]
other['year'] = other.index
other = other.set_index('Entity').join(gdp_2016.set_index('Country'))
other['Entity'] = other.index
top_10_countries = other.groupby('Entity').sum().sort_values('Other renewables (terawatt-hours)', ascending=False)[1:10].index.values
other = other[other['Entity'].isin(top_10_countries)]
other = other.set_index('year')
plt.figure()
sns.lineplot(data=other, x=other.index, y='Other renewables (terawatt-hours)', hue='Economy (GDP per Capita)').set_title('Top 10 Countries by Other Renewables')


#                     )
# hydro['Year'] = hydro.index
# # Initialize the FacetGrid object
# sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
# pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
# g = sns.FacetGrid(hydro, row="Entity", hue="Entity", aspect=15, height=.5, palette=pal)
# # Draw the densities in a few steps
# g.map(sns.kdeplot, "Year",
#       bw_adjust=.5, clip_on=False,
#       fill=True, alpha=1, linewidth=1.5)
# g.map(sns.kdeplot, "Year", clip_on=False, color="w", lw=2, bw_adjust=.5)
# g.map(plt.axhline, y=0, lw=2, clip_on=False)

# # Define and use a simple function to label the plot in axes coordinates
# def label(x, color, label):
#     ax = plt.gca()
#     ax.text(0, .2, label, fontweight="bold", color=color,
#             ha="left", va="center", transform=ax.transAxes)
# g.map(label, "Year")
# # Set the subplots to overlap
# g.fig.subplots_adjust(hspace=.25)

# # Remove axes details that don't play well with overlap
# g.set_titles("")
# g.set(yticks=[])
# g.despine(bottom=True, left=True)

# sns.relplot(data=hydro, )
# # sns.lineplot(data=hydro)


###################################
# Womens rights
gen_cols = ['A woman can apply for a passport in the same way as a man (1=yes; 0=no) [SG.APL.PSPT.EQ]',
'A woman can be head of household in the same way as a man (1=yes; 0=no) [SG.HLD.HEAD.EQ]',
'A woman can choose where to live in the same way as a man (1=yes; 0=no) [SG.LOC.LIVE.EQ]',
'A woman can get a job in the same way as a man (1=yes; 0=no) [SG.GET.JOBS.EQ]',
'A woman can obtain a judgment of divorce in the same way as a man (1=yes; 0=no) [SG.OBT.DVRC.EQ]',
'A woman can open a bank account in the same way as a man (1=yes; 0=no) [SG.OPN.BANK.EQ]',
'A woman can register a business in the same way as a man (1=yes; 0=no) [SG.BUS.REGT.EQ]',
'A woman can sign a contract in the same way as a man (1=yes; 0=no) [SG.CNT.SIGN.EQ]',
'A woman can travel outside her home in the same way as a man (1=yes; 0=no) [SG.HME.TRVL.EQ]',
'A woman can travel outside the country in the same way as a man (1=yes; 0=no) [SG.CTR.TRVL.EQ]',
'A woman has the same rights to remarry as a man (1=yes; 0=no) [SG.REM.RIGT.EQ]'
]
gender = gender.dropna()
year = ['2020']
gender = gender[~gender['Time'].isin(year)]
gender[gen_cols[0]] = gender[gen_cols[0]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[1]] = gender[gen_cols[1]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[2]] = gender[gen_cols[2]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[3]] = gender[gen_cols[3]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[4]] = gender[gen_cols[4]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[5]] = gender[gen_cols[5]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[6]] = gender[gen_cols[6]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[7]] = gender[gen_cols[7]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[8]] = gender[gen_cols[8]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[9]] = gender[gen_cols[9]].apply(lambda x: int(x) if x.isdigit() else 0)
gender[gen_cols[10]] = gender[gen_cols[10]].apply(lambda x: int(x) if x.isdigit() else 0)

gender['count of womens rights'] = (gender[gen_cols[0]])+(gender[gen_cols[1]])+(gender[gen_cols[2]])+(gender[gen_cols[3]])+(gender[gen_cols[4]])+(gender[gen_cols[5]])+(gender[gen_cols[6]])+(gender[gen_cols[7]])+(gender[gen_cols[8]])+(gender[gen_cols[9]])+(gender[gen_cols[10]])
top_10_countries = gender.groupby('Country Name').sum().sort_values('count of womens rights', ascending=False)[1:30].index.values
gender = gender[gender['Country Name'].isin(top_10_countries)]
##swtich to top 30 in gdp, not womens rights
gender = gender.set_index('Country Name').join(gdp_2016.set_index('Country'))
gender['Country Name'] = gender.index
gender = gender[['Time','count of womens rights','Economy (GDP per Capita)']]
plt.figure()
sns.lineplot(data=gender, x='Time', y='count of womens rights', hue='Economy (GDP per Capita)').set_title('Womens Rights Top 30 Countries')

gender_more = pd.read_csv('h/gender_more.csv')
gender_more.replace("nan",np.nan)

columns = list(gender_more.columns)
year = ['2020']
gender_more = gender_more[~gender_more['Time'].isin(year)]
temp_series = pd.Series(dtype=int)

# for i in range(len(columns)):
#   gender_more = gender_more[~gender_more[columns[i]].isnull()]

gender_more['count of womens rights'] = pd.Series(np.zeros(len(gender_more)))

for i in range(4,len(columns)):
  gender_more['count of womens rights'] += gender_more[columns[i]].apply(lambda x: 1 if x  else 0)

# gender_more['count of womens rights'] = temp_series






