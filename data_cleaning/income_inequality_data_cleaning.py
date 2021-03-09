
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from collections import defaultdict
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os

def income_inequality_data_clean(file_name):
    '''
    Clean health data and return a new clean dataframe for the same
    :param file_name: dataset csv file to clean
    :return: pandas dataframe
    '''
    assert isinstance(file_name,str)
    assert os.path.exists(file_name)
    # reading income inequality data
    income_df = pd.read_csv(file_name)
    # cleaning nan values
    income_df['GDP per capita, PPP (current international $) [NY.GDP.PCAP.PP.CD]'].replace('..', np.nan, inplace=True)
    income_df['Income share held by highest 10% [SI.DST.10TH.10]'].replace('..', np.nan, inplace=True)
    income_df.dropna(subset=['Income share held by highest 10% [SI.DST.10TH.10]'], inplace=True)
    income_df['Income of Top 10%'] = income_df['Income share held by highest 10% [SI.DST.10TH.10]'].astype(float)
    income_df['GDP Per Capita'] = income_df['GDP per capita, PPP (current international $) [NY.GDP.PCAP.PP.CD]'].astype(float)
    # normalizing gdp values
    income_df['GDP Per Capita'] = income_df['GDP Per Capita']/200

    return income_df