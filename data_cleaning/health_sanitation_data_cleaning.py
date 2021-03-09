import pandas as pd
import os

# columns in health sanitation dataset csv files
required = ['Country Name','GDP per capita (current US$) [NY.GDP.PCAP.CD]',                    
            'Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population) [SH.STA.WASH.P5]',
            'People using at least basic drinking water services (% of population) [SH.H2O.BASW.ZS]',
            'People using at least basic sanitation services (% of population) [SH.STA.BASS.ZS]']


def heath_sanitation_data_clean(file_name):
    '''
    Clean health data and return a new clean dataframe for the same
    :param file_name: dataset csv file to clean
    :return: pandas dataframe
    '''
    assert isinstance(file_name,str)
    assert os.path.exists(file_name)
    # reading health sanitation data
    data = pd.read_csv(file_name)

    # Organize dataframe with the required data
    new_data = []
    for i in range(data.shape[0]):
        flag = False
        tmp = []
        for j in required[1:]:
            try:
                t = float(data[j][i])
                if j == 'GDP per capita (current US$) [NY.GDP.PCAP.CD]':
                    tmp.append(int(t/200))
                else:
                    tmp.append(t)
            except ValueError:
                flag = True
                break
        if not flag:
            tmp.append(data[required[0]][i])
            new_data.append(tmp)
    # cleaned dataframe
    new_df = pd.DataFrame(new_data, columns = ['GDP_per_capita',
                                               'mortality_rate_unsafe_water_sanitation_hygiene','basic_water_access',
                                               'basic_sanitation_access','Country'])  

    return new_df
