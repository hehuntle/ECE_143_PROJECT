import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data = pd.read_csv("/Users/heatherhuntley/Desktop/ece_143/new_project/education.csv")
data=pd.read_csv("https://raw.githubusercontent.com/hehuntle/ECE_143_PROJECT/main/datasets/education.csv")

#GDP
GDP = data[data["Series"]=='GDP at market prices (current US$)']
GDP_capita = data[data["Series"]=='GDP per capita (current US$)']

#Graph 1
female_prime_ger = data[data["Series"]=='Gross enrolment ratio, primary, female (%)']
prim_ger = data[data["Series"]=='Gross enrolment ratio, primary, both sexes (%)']

#Graph2
stem_grad_rate = data[data["Series"]=='Percentage of graduates from Science, Technology, Engineering and Mathematics programmes in tertiary education, both sexes (%)']
hum_grad_rate = data[data["Series"]=='Percentage of graduates from tertiary education graduating from Arts and Humanities programmes, both sexes (%)']
not_stem_grad_rate = data[data["Series"]=='Percentage of graduates from programmes other than Science, Technology, Engineering and Mathematics in tertiary education, both sexes (%)']

#Graph3
college_ger = data[data["Series"]=='Gross enrolment ratio, primary to tertiary, both sexes (%)']
college_ger_female = data[data["Series"]=='Gross enrolment ratio, primary to tertiary, female (%)']
college_ger_male = data[data["Series"]=='Gross enrolment ratio, primary to tertiary, male (%)']

GDP_capita=GDP_capita.rename(columns={'2010 [YR2010]':'GDP_2010', '2011 [YR2011]':'GDP_2011', '2012 [YR2012]':'GDP_2012', '2013 [YR2013]':'GDP_2013', '2014 [YR2014]':'GDP_2014', '2015 [YR2015]':'GDP_2015', '2016 [YR2016]':'GDP_2016', '2017 [YR2017]':'GDP_2017' ,
       '2018 [YR2018]':'GDP_2018', '2019 [YR2019]':'GDP_2019'})


#data Graph1 (primary GER v.s GDP in 2017. Includes general and female data)

prim_ger=prim_ger.rename(columns={'2017 [YR2017]':'Prime_GER_2017' })
female_prime_ger=female_prime_ger.rename(columns={'2017 [YR2017]':'Female_Prime_GER_2017' })
result = pd.merge(GDP_capita, prim_ger, on=['Country Code', 'Country Name' ])
result = pd.merge(result, female_prime_ger, on=['Country Code', 'Country Name' ])
result = pd.DataFrame(result, columns = ['Country Name','Prime_GER_2017', 'Female_Prime_GER_2017','GDP_2017'])

#data Graph2 (STEM grad rate)
stem_grad_rate=stem_grad_rate.rename(columns={'2017 [YR2017]':'STEM_2017' })
hum_grad_rate=hum_grad_rate.rename(columns={'2017 [YR2017]':'HUM_2017' })
not_stem_grad_rate=not_stem_grad_rate.rename(columns={'2017 [YR2017]':'NOT_STEM_2017' })

stem_grad_rate=stem_grad_rate.rename(columns={'2018 [YR2018]':'STEM_2018' })
hum_grad_rate=hum_grad_rate.rename(columns={'2018 [YR2018]':'HUM_2018' })
not_stem_grad_rate=not_stem_grad_rate.rename(columns={'2018 [YR2018]':'NOT_STEM_2018' })

stem_grad_rate=stem_grad_rate.rename(columns={'2016 [YR2016]':'STEM_2016' })
hum_grad_rate=hum_grad_rate.rename(columns={'2016 [YR2016]':'HUM_2016' })
not_stem_grad_rate=not_stem_grad_rate.rename(columns={'2016 [YR2016]':'NOT_STEM_2016' })




program_gdp = pd.merge(GDP_capita, stem_grad_rate, on=['Country Code', 'Country Name' ])
program_gdp = pd.merge(program_gdp, hum_grad_rate, on=['Country Code', 'Country Name' ])
program_gdp = pd.merge(program_gdp, not_stem_grad_rate, on=['Country Code', 'Country Name' ])


program_gdp = pd.merge(GDP_capita, stem_grad_rate, on=['Country Code', 'Country Name' ])
program_gdp = pd.merge(program_gdp, hum_grad_rate, on=['Country Code', 'Country Name' ])
program_gdp = pd.merge(program_gdp, not_stem_grad_rate, on=['Country Code', 'Country Name' ])



program_gdp_2018= program_gdp[['Country Name','STEM_2018', 'HUM_2018','NOT_STEM_2018', 'GDP_2018']]

program_gdp_2016= program_gdp[['Country Name','STEM_2016', 'HUM_2016','NOT_STEM_2016', 'GDP_2016']]

program_gdp= program_gdp[['Country Name','STEM_2017', 'HUM_2017','NOT_STEM_2017', 'GDP_2017']]


#data Graph3 (college GER v.s GDP in 2017. Includes general and female data))

college_ger=college_ger.rename(columns={'2017 [YR2017]':'GER_2017' })
college_ger_female=college_ger_female.rename(columns={'2017 [YR2017]':'GER_female_2017' })
college_ger_male=college_ger_male.rename(columns={'2017 [YR2017]':'GER_male_2017' })

ger_gdp = pd.merge(GDP_capita, college_ger, on=['Country Code', 'Country Name' ])
ger_gdp = pd.merge(ger_gdp, college_ger_female, on=['Country Code', 'Country Name' ])
ger_gdp = pd.merge(ger_gdp, college_ger_male, on=['Country Code', 'Country Name' ])
ger_gdp= ger_gdp[['Country Name','GER_2017', 'GER_female_2017','GER_male_2017', 'GDP_2017']]


result=result.replace({".." : np.nan})
result=result.dropna()

program_gdp=program_gdp.replace({".." : np.nan})
program_gdp=program_gdp.dropna()

program_gdp_2018=program_gdp_2018.replace({".." : np.nan})
program_gdp_2018=program_gdp_2018.dropna()

program_gdp_2016=program_gdp_2016.replace({".." : np.nan})
program_gdp_2016=program_gdp_2016.dropna()

ger_gdp=ger_gdp.replace({".." : np.nan})
ger_gdp=ger_gdp.dropna()


program_gdp_2016['GDP_2016']=program_gdp_2016['GDP_2016'].astype(float)/200
program_gdp['GDP_2017']=program_gdp['GDP_2017'].astype(float)/200
program_gdp_2018['GDP_2018']=program_gdp_2018['GDP_2018'].astype(float)/200


result['Prime_GER_2017']= result['Prime_GER_2017'].astype(float)
result['Female_Prime_GER_2017']= result['Female_Prime_GER_2017'].astype(float)
result['GDP_2017']= result['GDP_2017'].astype(float)

program_gdp['STEM_2017']= program_gdp['STEM_2017'].astype(float)
program_gdp['HUM_2017']= program_gdp['HUM_2017'].astype(float)
program_gdp['NOT_STEM_2017']= program_gdp['NOT_STEM_2017'].astype(float)
program_gdp['GDP_2017']= program_gdp['GDP_2017'].astype(float)


program_gdp_2018['STEM_2018']= program_gdp_2018['STEM_2018'].astype(float)
program_gdp_2018['HUM_2018']= program_gdp_2018['HUM_2018'].astype(float)
program_gdp_2018['NOT_STEM_2018']= program_gdp_2018['NOT_STEM_2018'].astype(float)
program_gdp_2018['GDP_2018']= program_gdp_2018['GDP_2018'].astype(float)

program_gdp_2016['STEM_2016']= program_gdp_2016['STEM_2016'].astype(float)
program_gdp_2016['HUM_2016']= program_gdp_2016['HUM_2016'].astype(float)
program_gdp_2016['NOT_STEM_2016']= program_gdp_2016['NOT_STEM_2016'].astype(float)
program_gdp_2016['GDP_2016']= program_gdp_2016['GDP_2016'].astype(float)

