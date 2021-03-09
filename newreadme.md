# ECE-143-Project Team 20
This github is a repository for team 20's group presentation "Modernization and GDP". Winter 2021, ECE 143. 

In order to complete this project, we used following data
# Datasets: 

### * World Bank Dataset [LINK](https://data.worldbank.org/)
       We used this database to gather 
         1. Income Disparity
         2. Health
         3. Sanitation and Water
         4. Renewable Energy
         5. Secondary Education statistics

### * World-Happiness Kaggle Dataset [LINK](https://www.kaggle.com/unsdsn/world-happiness)
       We used this dataset to collect GDP data. 


## All the datafiles are stored in /datasets

# Github File/Folder Organization:
      .
      ├── data_cleaning                                            
      │    ├── education_data_cleaning.py                                  
      │    ├── energy_data_cleaning.py                               
      |    └── health_data_cleaning.py      
      |    └── health_sanitation_data_cleaning.py   
      |    └── income_inequality_data_cleaning.py   
      |
      ├── datasets                                      # Python code to acquire/clean the data 
      │     ├── GDP_2016.csv
      │     ├── education.csv
      │     ├── energy.csv
      │     ├── health.csv
      │     ├── income_inequality.csv
      ├── ProjectVisualization.ipynb                          # Jupiter notebook file for all the plots in the presentation
      ├── Presentation Slides       
      └── Group_20_Assignment6.ipynb
      └── README.md                                           # Readme files

#### 
# Modules/Packages used in the codes:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict, defaultdict
from scipy.stats import pearsonr
from matplotlib.pyplot import figure
import csv
      

