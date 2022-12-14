# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:32:03 2022

@author: prach
"""


# In[ ]:
   
    
# import libraries for performing functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# In[ ]:

    
"""
AGRICULTURAL LAND BAR GRAPH
"""    

# reading file and storing it in a variable
output_agri = open("Agricultural_land.csv", "r")
print("\nAgricultural Land Output: \n", output_agri) # printing the file
agri_land_rows=[] # creating rows array


# read CSV and store it in variable
agri_land = pd.read_csv("Agricultural_Land.csv")
print("\nAgricultural Land: \n", agri_land)


# drop particular columns
drp_agri_column = agri_land.drop(['Country Code', 'Indicator Name', 'Indicator Code', '1960'], axis=1)
print("\nAgricultural Land after dropping particular columns: \n", drp_agri_column)


# select particular rows using slicing method
new_agri_land = drp_agri_column.iloc[[14,29,35,37,55,70,89,99,109],:] #iloc used for choosing particular rows and all columns
print("\nExtracted Agricultural Land: \n", new_agri_land)


# remove NaN values from dataset
drp_agri_null = new_agri_land.dropna()
print("\nExtracted Agricultural Land after removing NaN: \n", drp_agri_null)


# calculating Normal Distribution of particular year through "scipy" module
print("\nNormal Distribution: \n", stats.skew(new_agri_land["1965"])) # "skew" is used for calculating normal distribution


# calculating average of total agricultural land through "numpy" module
print("\nAverage Agricultural Land: \n", agri_land.mean()) # "mean" is used for averaging


# removing first two lines
drp_agri_null = drp_agri_null.iloc[2:]
print("\nRemoving first two lines from Agricultural Land: \n", drp_agri_null)


# indexing the "Country Name" column
agri_index = drp_agri_null.set_index('Country Name')
print("\nAgricultural Land Country Name Index: \n", agri_index)


# select "Country Name" column for further use
agri_sel_cols = (new_agri_land["Country Name"])


# arranging length of column
x = np.arange(len(agri_sel_cols))


# extracting particular years and storing it in a variable
agri_one = (new_agri_land["1970"])
agri_two = (new_agri_land["1980"])
agri_three = (new_agri_land["1990"])
agri_four = (new_agri_land["2000"])
agri_five = (new_agri_land["2010"])
agri_six = (new_agri_land["2020"])


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# bar graph plot
plt.bar(x-0.3,agri_one, width=0.1, label="1970", edgecolor="black", color="blue")
plt.bar(x-0.2,agri_two, width=0.1, label="1980", edgecolor="black", color="yellow")
plt.bar(x-0.1,agri_three, width=0.1, label="1990", edgecolor="black", color="pink")
plt.bar(x+0.1,agri_four, width=0.1, label="2000", edgecolor="black", color="purple")
plt.bar(x+0.2,agri_five, width=0.1, label="2010", edgecolor="black", color="red")
plt.bar(x+0.3,agri_six, width=0.1, label="2020", edgecolor="black", color="magenta")


# manipulating ticks on x-axis
plt.xticks(x, agri_sel_cols, rotation = 45) # rotation refers to the angle of ticks on x-axis

plt.title("Agricultural Land Area")
plt.xlabel("Countries")
plt.ylabel("Agricultural Land (%)")
plt.legend()
plt.savefig("agri.png")
plt.show()

"""
FOREST AREA BAR GRAPH
"""

# reading file and storing it in a variable
output_forest = open("Forest_Area.csv", "r")
print("\nForest Area Output: \n", output_forest) #printing the file
rows=[]


# function for reading rows in file and populating header with header information
for rows in output_forest:
    print("\nForest Area Rows in Output: \n",rows)
    print()


# read CSV and store it in variable
forest_area = pd.read_csv("Forest_Area.csv")
print("\nForest Area: \n", forest_area)


# drop particular columns
drp_forest_column = forest_area.drop(['Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962',
                                  '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', 
                                  '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', 
                                  '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '2021'], axis=1)
print("\nForest Area after dropping particular columns: \n", drp_forest_column)


# select particular rows using slicing method
new_forest_area = drp_forest_column.iloc[[14,29,35,37,55,70,89,99,109],:] # iloc used for choosing particular rows and all columns
print("\nExtracted Forest Area: \n", new_forest_area)


# remove NaN values from dataset
drp_forest_null = new_forest_area.dropna()
print("\nExtracted Forest Area after dropping NaN: \n", drp_forest_null)


# removing first two lines
drp_forest_null = drp_forest_null.iloc[2:]
print("\nRemoving first two lines from Forest Area: \n", drp_forest_null)


# indexing the "Country Name" column
forest_index = drp_forest_null.set_index('Country Name')
print("\nForest Area Country Name Index: \n", forest_index)


# select "Country Name" column for further use
forest_sel_cols = (new_forest_area["Country Name"])


# arranging length of column
x = np.arange(len(forest_sel_cols))


# extracting particular years and storing it in a variable
forest_one = (new_forest_area["1990"])
forest_two = (new_forest_area["1995"])
forest_three = (new_forest_area["2000"])
forest_four = (new_forest_area["2005"])
forest_five = (new_forest_area["2010"])
forest_six = (new_forest_area["2015"])


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# bar graph plot
plt.bar(x-0.3,forest_one, width=0.1, label="1990", edgecolor="black", color="red")
plt.bar(x-0.2,forest_two, width=0.1, label="1995", edgecolor="black", color="blue")
plt.bar(x-0.1,forest_three, width=0.1, label="2000", edgecolor="black", color="orange")
plt.bar(x+0.1,forest_four, width=0.1, label="2005", edgecolor="black", color="brown")
plt.bar(x+0.2,forest_five, width=0.1, label="2010", edgecolor="black", color="violet")
plt.bar(x+0.3,forest_six, width=0.1, label="2015", edgecolor="black", color="green")

# manipulating ticks on x-axis
plt.xticks(x, forest_sel_cols, rotation = 45) # rotation refers to the angle of ticks on x-axis

plt.title("Forest Area")
plt.xlabel("Countries")
plt.ylabel("Forest Area (%)")
plt.legend()
plt.savefig("forest.png")
plt.show()



# In[ ]:

    
"""
POPULATION LINE GRAPH
"""

# reading file and storing it in a variable
output_pop = open("Population.csv", "r")
print("\nPopulation Output: \n", output_pop) # printing the file
rows=[]
    

# read csv file and storing it in a variable
pop = pd.read_csv("Population.csv")
print("\nPopulation: \n", pop)


# drop particular columns
pop = pop.drop(['Indicator Code', 'Indicator Name'], axis=1)
print("\nPopulation after dropping particular columns: \n",pop)


# transpose the dataframe
pop = pd.DataFrame.transpose(pop)
print("\nPopulation Transpose: \n", pop)


# populating header with header information
header3 = pop.iloc[0].values.tolist()
pop.columns = header3
print("\nPopulation Header: \n",pop)


# removing first two lines
pop = pop.iloc[2:]
print("\nRemoving first two lines from Population: ", pop)


# arranging length of column
print(len(pop))


# extracting particular countries and storing it in a variable
pop = pop[pop["Austria"].notna()]
pop = pop[pop["Brazil"].notna()]
pop = pop[pop["Canada"].notna()]
pop = pop[pop["Switzerland"].notna()]
pop = pop[pop["Germany"].notna()]
pop = pop[pop["Spain"].notna()]
pop = pop[pop["Greece"].notna()]
pop = pop[pop["Croatia"].notna()]
pop = pop[pop["India"].notna()]


# indexing change as integer type
pop.index = pop.index.astype(int)


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# line graph plot
plt.plot(pop.index, pop["Austria"], label="Austria", linestyle='dashed')
plt.plot(pop.index, pop["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(pop.index, pop["Canada"], label="Canada", linestyle='dashed')
plt.plot(pop.index, pop["Switzerland"], label="Switzerland", linestyle='dashed')
plt.plot(pop.index, pop["Germany"], label="Germany", linestyle='dashed')
plt.plot(pop.index, pop["Spain"], label="Spain", linestyle='dashed')
plt.plot(pop.index, pop["Greece"], label="Greece", linestyle='dashed')
plt.plot(pop.index, pop["Croatia"], label="Croatia", linestyle='dashed')
plt.plot(pop.index, pop["India"], label="India", linestyle='dashed')

plt.title("Population Total")
plt.xlabel("Year")
plt.ylabel("Population (%)")
plt.legend(bbox_to_anchor=(1,0.5), loc="center left")
plt.savefig("pop.png")
plt.show()


# In[ ]:
    
    
"""
ACCESS ELECTRICITY LINE GRAPH
"""

# reading file and storing it in a variable
output_elec = open("Access_Electricity.csv", "r")
print("\nAccess_Electricity Output: \n", output_elec) #printing the file
rows=[]


# read csv file and storing it in a variable
elec = pd.read_csv("Access_Electricity.csv")
print("\nElectricity: \n", elec)


# drop particular columns
elec = elec.drop(['Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962',
                  '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', 
                  '1972', '1973', '1974', '1975', '1976', '1978', '1979', '1980', '1981', 
                  '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '2021'], axis=1)
print("\nAccess Electricity after dropping particular columns: \n", elec)


# transpose the dataframe
elec = pd.DataFrame.transpose(elec)
print("\nAccess Electricity Transpose: \n", elec)


# populating header with header information
header4 = elec.iloc[0].values.tolist()
elec.columns = header4
print("\nAccess Electricity Header: \n", elec)


# removing first two lines
elec = elec.iloc[2:]
print("\nRemoving first two lines from Access Electricity: \n", elec)


# arranging length of column
print(len(elec))


# extracting particular countries and storing it in a variable
elec = elec[elec["Austria"].notna()]
elec = elec[elec["Brazil"].notna()]
elec = elec[elec["Canada"].notna()]
elec = elec[elec["Switzerland"].notna()]
elec = elec[elec["Germany"].notna()]
elec = elec[elec["Spain"].notna()]
elec = elec[elec["Greece"].notna()]
elec = elec[elec["Croatia"].notna()]
elec = elec[elec["India"].notna()]


# indexing change as integer type
elec.index = elec.index.astype(int)


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# line graph plot
plt.plot(elec.index, elec["Austria"], label="Austria", linestyle='dashed')
plt.plot(elec.index, elec["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(elec.index, elec["Canada"], label="Canada", linestyle='dashed')
plt.plot(elec.index, elec["Switzerland"], label="Switzerland", linestyle='dashed')
plt.plot(elec.index, elec["Germany"], label="Germany", linestyle='dashed')
plt.plot(elec.index, elec["Spain"], label="Spain", linestyle='dashed')
plt.plot(elec.index, elec["Greece"], label="Greece", linestyle='dashed')
plt.plot(elec.index, elec["Croatia"], label="Croatia", linestyle='dashed')
plt.plot(elec.index, elec["India"], label="India", linestyle='dashed')

plt.title("Access Electricity")
plt.xlabel("Year")
plt.ylabel("Access Electricity (%)")
plt.legend(bbox_to_anchor=(1.0,0.5), loc="center left")
plt.savefig("elec.png")
plt.show()



# In[ ]:
    
# read csv file adn storing it in a variable
table = pd.read_csv("Energy_Consumption.csv")
df_table = pd.DataFrame(table)
print("\nEnergy Consumption Dataframe: \n", df_table)

# accessing particular rows
new_table = df_table.iloc[[14, 29, 35, 37, 55, 70, 99, 109],:]
print("\nExtracted Energy Dataframe: \n", new_table)
    
    
    
