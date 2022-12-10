# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:37:53 2022

@author: Adeolu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:15:08 2022

@author: Adeolu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import pearsonr



def data_frame(file, indicator):
    """
    

    Parameters
    ----------
    file : A csv format
        The use of a csv document gotten from World bank.
    indicator : The Series name
        DESCRIPTION: The name of the series for use, the 
        imported data has various indicators.

    Returns
    -------
    country_data : The country name
        as a column and the year in rows.
    year_data : The year 
        as a column and returns the country as a row.

    """
    data = pd.read_csv(file)
    data1 = data[data['Series Name'] == indicator]
    
    country_data = data1
    
    data1 = data1.drop(['Series Name', 'Country Code'], axis=1)
    
    year_data = data1.T
    year_data = year_data.rename(columns=year_data.iloc[0])
    year_data = year_data.drop(index=year_data.index[0], axis=0)
    year_data = year_data.reset_index()
    year_data = year_data.rename(columns={"index":"Year"})
    
    return country_data, year_data, data



#With the use of the defined function to read into a panda dataframe
file = 'co2emission.csv'
indicator = 'CO2 emissions (kt)'
df_countries, df_year, df_data = data_frame(file, indicator)



#plotting of the co2 emission as a bar chart to see its trend
plt.figure()
df_countries.plot('Country Name',['1990','1994','1996','1998','2000', '2012'\
                                  ,'2014','2016','2018'], kind='bar')
plt.xticks(rotation= 45)
plt.title('Carbon Dioxide Emission (Kiloton)')
plt.savefig('Co2 emission.png')
plt.show()
