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

    
"""
AGRICULTURAL LAND BAR GRAPH
"""    

def readFile(a):
    '''
        This function is used to read csv file in original form and transposed 
        form and also dropping specific columns to avoid disturbance
        in final visualized result.

        Parameters
        ----------
        a : csv filename
    
        Returns
        -------
        agri_land : variable for storing csv file
        agri_land_t : variable for storing transposed csv file

    '''
    agri_land = pd.read_csv("Agricultural_Land.csv");
    agri_land = agri_land.drop(['Country Code', 'Indicator Name', \
                                'Indicator Code', '1960'], axis=1)
    agri_land_t = pd.DataFrame.transpose(agri_land)
    return agri_land, agri_land_t

# calling function above to display dataframe
agri_land, agri_land_t = readFile("Agricultural_land.csv")
print("\nAgricultural Land: \n", agri_land)
print("\nTransposed Agricultural Land: \n", agri_land_t)


# select particular rows using slicing method
new_agri_land = agri_land.iloc[[14,29,35,37,55,70,89,99,109],:] #iloc used for choosing particular rows and all columns
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


# manipulating ticks on x & y axis
plt.xticks(x, agri_sel_cols, rotation = 45, fontsize=13) # rotation refers to the angle of ticks on x-axis
plt.yticks(fontsize=13)

plt.title("Agricultural Land Area", fontsize=15)
plt.xlabel("Countries", fontsize=15)
plt.ylabel("Agricultural Land (%)", fontsize=15)
plt.legend(fontsize=13)
plt.savefig("agri.png")
plt.show()



# In[ ]:
    

"""
FOREST AREA BAR GRAPH
"""

def readFile(b):
    '''
        This function is used to read csv file in original form and transposed 
        form and also dropping specific columns to avoid disturbance
        in final visualized result.

        Parameters
        ----------
        b : csv filename
    
        Returns
        -------
        forest_area : variable for storing csv file
        forest_area_t : variable for storing transposed csv file

    '''
    forest_area = pd.read_csv("Forest_Area.csv");
    forest_area = forest_area.drop(['Country Code', 'Indicator Name', \
                                    'Indicator Code', '1960', '1961', '1962', \
                                      '1963', '1964', '1965', '1966', '1967', \
                                      '1968', '1969', '1970', '1971', '1972', \
                                      '1973', '1974', '1975', '1976', '1977', \
                                      '1978', '1979', '1980', '1981', '1982', \
                                      '1983', '1984', '1985', '1986', '1987', \
                                      '1988', '1989', '2021'], axis=1)
    forest_area_t = pd.read_csv(b).T
    return forest_area, forest_area_t

# calling function above to display dataframe
forest_area, forest_area_t = readFile("Forest_Area.csv")
print("\nForest Area: \n", forest_area)
print("\nTransposed Forest Area: ", forest_area_t)


# select particular rows using slicing method
new_forest_area = forest_area.iloc[[14,29,35,37,55,70,89,99,109],:] # iloc used for choosing particular rows and all columns
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

# manipulating ticks on x & y axis
plt.xticks(x, forest_sel_cols, rotation = 45, fontsize=13) # rotation refers to the angle of ticks on x-axis
plt.yticks(fontsize=13)

plt.title("Forest Area", fontsize=15)
plt.xlabel("Countries", fontsize=15)
plt.ylabel("Forest Area (%)", fontsize=15)
plt.legend(fontsize=13)
plt.savefig("forest.png")
plt.show()



# In[ ]:

    
"""
POPULATION LINE GRAPH
"""

def readFile(c):
    '''
        This function is used to read csv file in original form and transposed 
        form and also dropping specific columns to avoid disturbance
        in final visualized result.

        Parameters
        ----------
        c : csv filename
    
        Returns
        -------
        pop : variable for storing csv file
        pop_t : variable for storing transposed csv file

    '''
    pop = pd.read_csv("Population.csv");
    pop = pop.drop(['Country Code', 'Indicator Name', 'Indicator Code'], \
                   axis=1)
    pop_t = pd.DataFrame.transpose(pop)
    return pop, pop_t

# calling function above to display dataframe
pop, pop_t = readFile("Population.csv")
print("\nPopulation: \n", pop)
print("\nTranposed Population: \n", pop_t)


# populating header with header information
header3 = pop_t.iloc[0].values.tolist()
pop_t.columns = header3
print("\nPopulation Header: \n", pop_t)


# removing first two lines
pop_t = pop_t.iloc[2:]
print("\nRemoving first two lines from population: \n", pop_t)


# arranging length of column
print(len(pop_t))


# extracting particular countries and storing it in a variable
pop_t = pop_t[pop_t["Austria"].notna()]
pop_t = pop_t[pop_t["Brazil"].notna()]
pop_t = pop_t[pop_t["Canada"].notna()]
pop_t = pop_t[pop_t["Switzerland"].notna()]
pop_t = pop_t[pop_t["Germany"].notna()]
pop_t = pop_t[pop_t["Spain"].notna()]
pop_t = pop_t[pop_t["Greece"].notna()]
pop_t = pop_t[pop_t["Croatia"].notna()]
pop_t = pop_t[pop_t["India"].notna()]


# indexing change as integer type
pop_t.index = pop_t.index.astype(int)


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# line graph plot
plt.plot(pop_t.index, pop_t["Austria"], label="Austria", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Canada"], label="Canada", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Switzerland"], label="Switzerland", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Germany"], label="Germany", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Spain"], label="Spain", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Greece"], label="Greece", linestyle='dashed')
plt.plot(pop_t.index, pop_t["Croatia"], label="Croatia", linestyle='dashed')
plt.plot(pop_t.index, pop_t["India"], label="India", linestyle='dashed')


# manipulating ticks on x & y axis
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)


plt.title("Population Total", fontsize=15)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Population (%)", fontsize=15)
plt.legend(bbox_to_anchor=(1,0.5), loc="center left", fontsize=13)
plt.savefig("pop.png")
plt.show()


# In[ ]:
    
    
"""
ACCESS ELECTRICITY LINE GRAPH
"""

def readFile(d):
    '''
        This function is used to read csv file in original form and transposed 
        form and also dropping specific columns to avoid disturbance
        in final visualized result.

        Parameters
        ----------
        d : csv filename
    
        Returns
        -------
        elec : variable for storing csv file
        elec_t : variable for storing transposed csv file

    '''
    elec = pd.read_csv("Access_Electricity.csv");
    elec = pd.read_csv(d)
    elec = elec.drop(['Country Code', 'Indicator Name', 'Indicator Code', \
                      '1960', '1961', '1962', '1963', '1964', '1965', '1966', \
                      '1967', '1968', '1969', '1970', '1971', '1972', '1973', \
                      '1974', '1975', '1976', '1978', '1979', '1980', '1981', \
                      '1982', '1983', '1984', '1985', '1986', '1987', '1988', \
                      '1989', '2021'], axis=1)
    elec_t = pd.DataFrame.transpose(elec)
    return elec, elec_t

# calling function above to display dataframe
elec, elec_t = readFile("Access_Electricity.csv")
print("\nAccess Electricity: \n", elec)
print("\nTransposed Access Electricity: \n", elec_t)


# populating header with header information
header4 = elec_t.iloc[0].values.tolist()
elec_t.columns = header4
print("\nAccess Electricity Header: \n", elec_t)


# removing first two lines
elec_t = elec_t.iloc[2:]
print("\nRemoving first two lines from Access Electricity: \n", elec_t)


# arranging length of column
print(len(elec_t))


# extracting particular countries and storing it in a variable
elec_t = elec_t[elec_t["Austria"].notna()]
elec_t = elec_t[elec_t["Brazil"].notna()]
elec_t = elec_t[elec_t["Canada"].notna()]
elec_t = elec_t[elec_t["Switzerland"].notna()]
elec_t = elec_t[elec_t["Germany"].notna()]
elec_t = elec_t[elec_t["Spain"].notna()]
elec_t = elec_t[elec_t["Greece"].notna()]
elec_t = elec_t[elec_t["Croatia"].notna()]
elec_t = elec_t[elec_t["India"].notna()]


# indexing change as integer type
elec_t.index = elec_t.index.astype(int)


# plotting figure and adjusting figure size in plot
plt.figure(figsize=(10,8))


# line graph plot
plt.plot(elec_t.index, elec_t["Austria"], label="Austria", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Brazil"], label="Brazil", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Canada"], label="Canada", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Switzerland"], label="Switzerland", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Germany"], label="Germany", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Spain"], label="Spain", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Greece"], label="Greece", linestyle='dashed')
plt.plot(elec_t.index, elec_t["Croatia"], label="Croatia", linestyle='dashed')
plt.plot(elec_t.index, elec_t["India"], label="India", linestyle='dashed')


# manipulating ticks on x & y axis
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)


plt.title("Access Electricity", fontsize=15)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Access Electricity (%)", fontsize=15)
plt.legend(bbox_to_anchor=(1.0,0.5), loc="center left", fontsize=13)
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
    
    
    
