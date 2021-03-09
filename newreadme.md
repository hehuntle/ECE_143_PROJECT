# ECE-143-Project Team 20 Winter 2021, ECE 143. 
This github is a repository for team 20's group presentation "Modernization and GDP". 

In order to complete this project, we used following data
# Datasets: 

###  World Bank Dataset [LINK](https://data.worldbank.org/)
       We used this database to gather 
         1. Income Disparity
         2. Health
         3. Sanitation and Water
         4. Renewable Energy
         5. Secondary Education statistics

###  World-Happiness Kaggle Dataset [LINK](https://www.kaggle.com/unsdsn/world-happiness)
       We used this dataset to collect GDP data. 


## All the datafiles are stored in /datasets

# Github File/Folder Organization:
      ├── data_cleaning                                            
      │    ├── education_data_cleaning.py                                  
      │    ├── energy_data_cleaning.py                               
      |    └── health_data_cleaning.py      
      |    └── health_sanitation_data_cleaning.py   
      |    └── income_inequality_data_cleaning.py   
      |
      ├── datasets                                     
      │     ├── GDP_2016.csv
      │     ├── education.csv
      │     ├── energy.csv
      │     ├── health.csv
      │     ├── income_inequality.csv
      ├── ProjectVisualization.ipynb                        
      ├── Presentation Slides       
      └── Group_20_Assignment6.ipynb
      └── README.md                                          

#### 
# Modules/Packages used:
import pandas as pd <br>
import numpy as np  <br>
import matplotlib.pyplot as plt  <br>
from collections import OrderedDict, defaultdict  <br>
from scipy.stats import pearsonr  <br>
from matplotlib.pyplot import figure  <br>
import csv  <br>
      

