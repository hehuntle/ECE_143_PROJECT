
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from collections import defaultdict
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def income_disparity_clean(filename):
  data = pd.read_csv(filename)
  data['GDP per capita, PPP (current international $) [NY.GDP.PCAP.PP.CD]'].replace('..', np.nan, inplace=True)
  data['Income share held by highest 10% [SI.DST.10TH.10]'].replace('..', np.nan, inplace=True)
  data.dropna(subset=['Income share held by highest 10% [SI.DST.10TH.10]'], inplace=True)
  data['Income of Top 10%'] = data['Income share held by highest 10% [SI.DST.10TH.10]'].astype(float)
  data['GDP Per Capita'] = data['GDP per capita, PPP (current international $) [NY.GDP.PCAP.PP.CD]'].astype(float)
  return data
