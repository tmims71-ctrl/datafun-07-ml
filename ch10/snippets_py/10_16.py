print("DataFrame shape (rows, columns):", nyc.shape)
print("Column names:", nyc.columns.tolist())
min_temp = nyc.Temperature.min()
max_temp = nyc.Temperature.max()
min_year = nyc.Date[nyc.Temperature.idxmin()]
max_year = nyc.Date[nyc.Temperature.idxmax()]
print(f"Minimum temperature: {min_temp}F in {min_year}")
print(f"Maximum temperature: {max_temp}F in {max_year}")
# Section 10.16 Snippets
# This file includes the Self Check snippets which continue from the section body.

# Time Series
# Simple Linear Regression
# Linear Relationships

c = lambda f: 5 / 9 * (f - 32)

temps = [(f, c(f)) for f in range(0, 101, 10)]

import pandas as pd


temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_label = axes.set_ylabel('Celsius')
import matplotlib.pyplot as plt
plt.show()

# Components of the Simple Linear Regression Equation
# SciPy’s stats Module
# Pandas
# Seaborn Visualization
# Getting Weather Data from NOAA

# Loading the Average High Temperatures into a DataFrame

nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
print("First 5 rows:\n", nyc.head())
print("Last 5 rows:\n", nyc.tail())
# Cleaning the Data
nyc.columns = ['Date', 'Temperature', 'Anomaly']
print("First 3 rows after renaming columns:\n", nyc.head(3))
print("Date dtype:", nyc.Date.dtype)
nyc.Date = nyc.Date.floordiv(100)
print("First 3 rows after cleaning Date:\n", nyc.head(3))

# Calculating Basic Descriptive Statistics for the Dataset

pd.set_option('display.precision', 2)
print("Temperature describe:\n", nyc.Temperature.describe())

# Forecasting Future January Average High Temperatures
from scipy import stats


linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
print("Slope:", linear_regression.slope)
print("Intercept:", linear_regression.intercept)
print("Predicted temp for 2019:", linear_regression.slope * 2019 + linear_regression.intercept)
print("Predicted temp for 1850:", linear_regression.slope * 1850 + linear_regression.intercept)

# Plotting the Average High Temperatures and a Regression Line
import seaborn as sns

sns.set_style('whitegrid')


axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
axes.set_ylim(10, 70)
plt.show()

# Getting Time Series Datasets

# Self Check Exercises 
# Exercise 3
year = 2019

slope = linear_regression.slope

intercept = linear_regression.intercept

temperature = slope * year + intercept

while temperature < 40.0:

##########################################################################
# development, research, and testing of the theories and programs        #

# to determine their effectiveness. The authors and publisher make       #
    slope = linear_regression.slope
    intercept = linear_regression.intercept
    temperature = slope * year + intercept
    while temperature < 40.0:
        year += 1
        temperature = slope * year + intercept
    print("First year with predicted temp >= 40F:", year)
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
