import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
<<<<<<< HEAD

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # print(df)

    # Create scatter plot
    year = df['Year']
    # print(year)
    sea_level = df['CSIRO Adjusted Sea Level']
    # print(sea_level)

    fig = plt.scatter(x = year, y = sea_level)#, hue = df_bar['month'], color = 'rainbow')#, label = "Bar")#, = months)


    #plt.show()


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

    sea_level_pred = slope * year + intercept

    plt.plot(year, sea_level_pred, color = "red", label = "Regression Line")


    # Create second line of best fit
    sea_level_2000 = pd.concat([year , sea_level], axis = 1)    # sea_level_2000.set_index('Year', inplace = True)

    # year_2000 = sea_level_2000['Year']
    # year_2000 = year_2000[120:]
    # print(year_2000)
    # sealevel_2000 = sea_level_2000['CSIRO Adjusted Sea Level']

    sealevel_2000 = sea_level_2000[120:]
    year_2000 = sealevel_2000['Year']
    sealevel2000_ = sealevel_2000['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(year_2000, sealevel2000_)

    sealevelpred_2000 = slope * year_2000 + intercept

    plt.plot(year_2000, sealevelpred_2000, color = 'orange', label = 'Predictive Regression Line')



    # Add labels and title
=======
import numpy as np 

def draw_plot():
    ## Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # print(df)

    ## Create scatter plot
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    fig = plt.scatter(x = year, y = sea_level)   #, hue = df_bar['month'], color = 'rainbow')#, label = "Bar")#, = months)

    ## Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)
    sea_level_pred = slope * year + intercept
    plt.plot(year, sea_level_pred, color = "red", label = "Regression Line")

    ## Create second line of best fit


    ## Add labels and title
>>>>>>> d4e29d6 (updates made, new py file made)
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Sea Level (Inches)")
    plt.title("Rise in Sea Levels")
    plt.show()

    
    # # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    # return plt.gca()

    # Lets see if making a git pull works tomorrow!
<<<<<<< HEAD
=======
    # Made some updated and opened a new py file!
>>>>>>> d4e29d6 (updates made, new py file made)

draw_plot()