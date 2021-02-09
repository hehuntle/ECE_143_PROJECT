import numpy as np
import pandas as pd


#happs have results of World Happiness report from 2015-2018
#shape is 158 x 5
hap_2015 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2015.csv")
hap_2015=hap_2015[['Country',  'Family', 'Health (Life Expectancy)', 'Freedom','Trust (Government Corruption)']]
hap_2015=hap_2015.rename(columns={"Family": "Family_2015", "Health (Life Expectancy)": "Health (Life Expectancy)_2015", "Freedom":  "Freedom_2015", "Trust (Government Corruption)": "Trust (Government Corruption)_2015"})

hap_2016 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2016.csv")
hap_2016=hap_2016[['Country',  'Family', 'Health (Life Expectancy)', 'Freedom','Trust (Government Corruption)']]
hap_2016=hap_2016.rename(columns={"Family": "Family_2016", "Health (Life Expectancy)": "Health (Life Expectancy)_2016", "Freedom":  "Freedom_2016", "Trust (Government Corruption)": "Trust (Government Corruption)_2016"})

hap_2017 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2017.csv")
hap_2017=hap_2017[['Country',  'Family', 'Health..Life.Expectancy.', 'Freedom','Trust..Government.Corruption.']]
hap_2017=hap_2017.rename(columns={"Family": "Family_2017", "Health..Life.Expectancy": "Health (Life Expectancy)_2017", "Freedom":  "Freedom_2017", "Trust..Government.Corruption)": "Trust (Government Corruption)_2017"})

hap_2018 = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/h/2018.csv")
hap_2018=hap_2018[['Country or region',  'Social support', 'Healthy life expectancy', 'Freedom to make life choices','Perceptions of corruption']]
hap_2018=hap_2018.rename(columns={"Social support": "Family_2018", "Healthy life expectancy": "Health (Life Expectancy)_2018", "Freedom to make life choices":  "Freedom_2018", "Perceptions of corruption": "Trust (Government Corruption)_2018"})

#current_gdp has GDP from 2015-2018 for 199 countries
#shape is 199 x 5
current_gdp=pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/gdp/nom.csv")
current_gdp=current_gdp[['Country', '2015', '2016', '2017', '2018']]

#socioeconomic data from countries 2015-2019 for 277 countries
#shape is 277 x 8 
gen_count=pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/project/general_world/world.csv")
gen_count=gen_count[['Country', 'Pop. Density (per sq. mi.)', 'Net migration', 'Infant mortality (per 1000 births)', 'Crops (%)', 'Climate', 'Birthrate', 'Deathrate']]




#result1 = pd.concat([hap_2015, gen_count], axis=1)
#result = pd.concat([hap_2016, result1], axis=1)
#result = pd.concat([hap_2017, result], axis=1)
#result = pd.concat([hap_2018, result], axis=1)
#result=pd.concat([result,current_gdp], axis=1)

x_2015=pd.merge(gen_count,hap_2015, on='Country')
print(x_2015.shape)