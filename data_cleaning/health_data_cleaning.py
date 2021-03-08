import pandas as pd
import os

# columns in health dataset csv files
required = ['Country Name', 'Life expectancy at birth, total (years) [SP.DYN.LE00.IN]',
            'Physicians (per 1,000 people) [SH.MED.PHYS.ZS]', 'GDP per capita (current US$) [NY.GDP.PCAP.CD]',
            'Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70 (%) [SH.DYN.NCOM.ZS]',
            'Current health expenditure per capita (current US$) [SH.XPD.CHEX.PC.CD]']


def heath_data_clean(file_name):
    '''
    Clean health data and return a new clean dataframe for the same
    :param file_name: dataset csv file to clean
    :return: pandas dataframe
    '''
    assert isinstance(file_name,str)
    assert os.path.exists(file_name)
    # reading health data
    data = pd.read_csv(file_name)
    new_data = []
    for i in range(data.shape[0]):
        flag = False
        tmp = []
        for j in required[1:]:
            try:
                # removing all Nan or no data rows
                t = float(data[j][i])
                if j == 'GDP per capita (current US$) [NY.GDP.PCAP.CD]':
                    # Normalizing the GDP value
                    tmp.append(int(t / 200))
                else:
                    tmp.append(t)
            except ValueError:
                flag = True
                break
        if not flag:
            tmp.append(data[required[0]][i])
            new_data.append(tmp)

    # creating new dataframe with clean data
    new_df = pd.DataFrame(new_data, columns=['life_expectancy', 'Physicians_per_1000', 'GDP_per_capita', 'mortality',
                                             'health_gdp', 'Country'])

    return new_df
