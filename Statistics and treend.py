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
plt.xlabel('Country')
plt.ylabel('Carbon dioxide emission')
plt.title('Carbon Dioxide Emission (Kiloton)')
plt.rcParams["figure.dpi"] = 500
plt.savefig('Co2 emission.png')
plt.show()




#THE SECOND PLOT
#With the use of the previously defined function to read into a panda dataframe
#the data name changes so the python doesn't confuse it as a single data
file = 'Data.csv'
indicator = 'Agricultural land (% of land area)'
df_countrie, df_yea, df_dat = data_frame(file, indicator)



#The years in column are an object, using a function to convert to float
#since it is in a decimal format
print(df_countrie.dtypes)
year = ['1990','1994','1996','1998','2000','2012','2014','2016','2018']

def convert_to_float(data):
    """
    

    Parameters
    ----------
    The use of astype to convert the
    values in the year column to a float 
    with the use as astype.

    Returns: The converted object to float
    -------

    """
    for y in year:
        data[y] = data[y].astype(float)
convert_to_float(df_countrie)
print(df_countrie.dtypes)



plt.figure()
df_countrie.plot('Country Name',['1990','1994','1996','1998','2000', '2012'\
                                 ,'2014','2016','2018'], kind='bar')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xticks(rotation= 45)
plt.xlabel('Country')
plt.ylabel('Agricultural land')
plt.title('Agriculatural land covered(%)')
plt.rcParams["figure.dpi"] = 500
plt.savefig('Land covered by Agriculture.png',bbox_inches='tight')
plt.show()




#The third effect of climate change plotting
file = 'Data.csv'
indicator = 'Electricity production from oil sources (% of total)'
df_countri, df_ye, df_da = data_frame(file, indicator)


#deleting the columns without a value
df_countri = df_countri.drop(['2014','2016','2018'], axis=1)
year = ['1994','1996','1998','2000','2012']


#converting the type<object> to a float type
def convert_to_float(data):
    for y in year:
        data[y] = data[y].astype(float)
convert_to_float(df_countri)



plt.figure()
df_countri.plot('Country Name',['1994','1996','1998','2000', '2012']\
                , kind='bar')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xlabel('Country')
plt.ylabel('Electricity production from oil sources')
plt.title('Electricity from oil sources')
plt.xticks(rotation= 'vertical')
plt.rcParams["figure.dpi"] = 500
plt.savefig('Electricity.png',bbox_inches='tight')
plt.show()




#THE FOURTH PLOT
file = 'Data.csv'
indicator = 'Urban population (% of total population)'
df_countr, df_y, df_d = data_frame(file, indicator)


count = ['Sri Lanka','United Kingdom','Ireland','Iceland','Australia'\
         , 'New Zealand','Niger','Chad','Bangladesh','Haiti']

#convertimg of the countries in column to float types
def convert_to_float(data):
    for c in count:
        data[c] = data[c].astype(float)
convert_to_float(df_y)


plt.figure()
df_y.plot('Year',['Sri Lanka','United Kingdom','Ireland','Iceland'\
                     ,'Australia', 'New Zealand','Chad','Bangladesh','Haiti'])
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.xticks(rotation= 45)
plt.xlabel('Country')
plt.ylabel('Urban Population')
plt.title('Population growth')
plt.rcParams["figure.dpi"] = 500
plt.savefig('Population growth.png', bbox_inches='tight')
plt.show()




#THE USE OF HEATMAP TO SHOW THE CORRELATION BETWEEN SOME INDICATORS
#TO VERIFY ITS IMPACT ON CLIMATE CHANGE
data3  = pd.read_csv('Data.csv')
print(data3)
# data3 = data3.fillna(0, inplace=True)

#extracting the indicators needed to the country of interest
chad_a = data3.loc[data3['Country Name'] == 'Chad']
Chad1 = chad_a[chad_a['Series Name'] ==\
               'Urban population (% of total population)']
Chad2 = chad_a[chad_a['Series Name'] == \
               'Total greenhouse gas emissions (% change from 1990)']
Chad3 = chad_a[chad_a['Series Name'] == 'Agricultural land (% of land area)']
Chad4 = chad_a[chad_a['Series Name'] == 'CO2 emissions (kt)']
Chad5 = chad_a[chad_a['Series Name'] == 'Forest area (% of land area)']


#Mergeing all the indicators in a single dataframe
frame = [Chad1, Chad2, Chad3, Chad4, Chad5]
Chad_2 = pd.concat(frame)
print(Chad_2)





#Transposing the data to get the indicators as a column
Chad_3 = Chad_2.T

Chad_3.columns = ['Population', 'Total Greenhouse Gas emission'\
          ,'Agricultural area','Co2 emission','Forest area']

    
#Renaming the column containing the years to year
Chad_3 = Chad_3.reset_index()
Chad_3 = Chad_3.rename(columns={"index":"Year"})


#Deleting the rows that are not needed
Chad_3.drop([0,1,2],axis=0,inplace=True)
# print(Chad_3)



#Converting from object to float
#Since correlation analysis makes use of numbers
nam = ['Population', 'Total Greenhouse Gas emission','Agricultural area'\
   , 'Co2 emission', 'Forest area']
def convert_to_float(dat):
    for m in nam:
        dat[m] = dat[m].astype(float)
convert_to_float(Chad_3)
print()




#Tofurther understand the data the use of the statistical tool was used
#to visualize it
print(Chad_3.describe())
co = Chad_3.corr().round(2)
# print(co)

plt.figure(figsize=(10,8))
plot = sns.heatmap(co, annot = True)
plt.title('Chad Heatmap')
plt.savefig('Chad Heatmap.png',bbox_inches='tight')








#FROM THE CO2 EMISSION USING A COUNTRY WITH AN INCREASE IN CO2 EMISSION
#TO ASSESS THE FACTORS IT INFLUENCES
Aus = data3.loc[data3['Country Name'] == 'Australia']
Aus1 = Aus[Aus['Series Name'] == 'Urban population (% of total population)']
Aus2 = Aus[Aus['Series Name'] ==\
           'Total greenhouse gas emissions (% change from 1990)']
Aus3 = Aus[Aus['Series Name'] == 'Agricultural land (% of land area)']
Aus4 = Aus[Aus['Series Name'] == 'CO2 emissions (kt)']
Aus5 = Aus[Aus['Series Name'] == 'Forest area (% of land area)']
Aus6 = Aus[Aus['Series Name'] == \
           'Electricity production from oil sources (% of total)']

#Mergeing all the indicators in a single dataframe
frames = [Aus1, Aus2, Aus3, Aus4, Aus5, Aus6]
Aus_2 = pd.concat(frames)
print(Aus_2)





#Transposing the data to get the indicators as a column
Aus_3 = Aus_2.T

Aus_3.columns = ['Population', 'Total Greenhouse Gas emission'\
                 , 'Agricultural area','Co2 emission', 'Forest area'\
                     , 'Electricity production from oil']

    
#Renaming the column containing the years to year
Aus_3 = Aus_3.reset_index()
Aus_3 = Aus_3.rename(columns={"index":"Year"})


#Deleting the rows that are not needed
Aus_3.drop([0,1,2],axis=0,inplace=True)
# print(Chad_3)



#Converting from object to float
#Since correlation analysis makes use of numbers
name = ['Population', 'Total Greenhouse Gas emission','Agricultural area', 'Co2 emission', 'Forest area','Electricity production from oil']
def convert_to_float(dat):
    for n in name:
        dat[n] = dat[n].astype(float)
convert_to_float(Aus_3)

print(Aus_3.info())



#The use of a statistical function to understand the
#mean, standard deviation and other statistical function
print(Aus_3.describe())
Australia = Aus_3.corr().round(2)


plt.figure(figsize=(10,8))
plot = sns.heatmap(Australia, annot = True)
plt.title('Australia heat Map')
plt.savefig('Australia Heatmap.png',bbox_inches='tight')



