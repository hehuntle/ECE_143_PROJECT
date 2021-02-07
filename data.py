import numpy as np
import pandas as pd


#happs have results of World Happiness report from 2015-2018
hap_2015 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2015.csv")
hap_2015=hap_2015[['Country',  'Family', 'Health (Life Expectancy)', 'Freedom','Trust (Government Corruption)']]
hap_2016 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2016.csv")
hap_2016=hap_2016[['Country',  'Family', 'Health (Life Expectancy)', 'Freedom','Trust (Government Corruption)']]
hap_2017 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2017.csv")
hap_2017=hap_2017[['Country',  'Family', 'Health..Life.Expectancy.', 'Freedom','Trust..Government.Corruption.']]
hap_2018 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2018.csv")
hap_2018=hap_2018[['Country or region',  'Social support', 'Healthy life expectancy', 'Freedom to make life choices','Perceptions of corruption']]

#current_gdp has GDP from 2015-2018 for 199 countries
current_gdp=pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/gdp/nom.csv")
current_gdp=current_gdp[['Country', '2015', '2016', '2017', '2018']]

#socioeconomic data from countries 2015-2019 for 277 countries
gen_count=pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/general_world/world.csv")
gen_count=gen_count[['Country', 'Pop. Density (per sq. mi.)', 'Net migration', 'Infant mortality (per 1000 births)', 'Crops (%)', 'Climate', 'Birthrate', 'Deathrate']]


x_2015=pd.merge(gen_count,hap_2015, on='Country')
#x_2016=pd.merge(hap_2016, gen_count)
#x_2017=pd.merge(hap_2017, gen_count)
#x_2018=pd.merge(hap_2018, gen_count)



print(x_2015.shape)