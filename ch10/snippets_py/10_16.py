# Section 10.16 Snippets
# Cleaned up and corrected version

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Fahrenheit to Celsius conversion
def c(f):
    return 5 / 9 * (f - 32)

# Create temperature conversion table
temps = [(f, c(f)) for f in range(0, 101, 10)]
temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
axes.set_ylabel('Celsius')
plt.show()

# Load the Average High Temperatures into a DataFrame
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
print("First 5 rows:\n", nyc.head())
print("Last 5 rows:\n", nyc.tail())

# Clean the Data
nyc.columns = ['Date', 'Temperature', 'Anomaly']
print("First 3 rows after renaming columns:\n", nyc.head(3))
print("Date dtype:", nyc.Date.dtype)
nyc.Date = nyc.Date.floordiv(100)
print("First 3 rows after cleaning Date:\n", nyc.head(3))

# Descriptive statistics
pd.set_option('display.precision', 2)
print("Temperature describe:\n", nyc.Temperature.describe())

# Linear regression
linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
print("Slope:", linear_regression.slope)
print("Intercept:", linear_regression.intercept)
print("Predicted temp for 2019:", linear_regression.slope * 2019 + linear_regression.intercept)
print("Predicted temp for 1850:", linear_regression.slope * 1850 + linear_regression.intercept)

# Plot regression
sns.set_style('whitegrid')
axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
axes.set_ylim(10, 70)
plt.show()

# Self Check Exercise: When will predicted temp >= 40F?
year = 2019
slope = linear_regression.slope
intercept = linear_regression.intercept
temperature = slope * year + intercept
while temperature < 40.0:
    year += 1
    temperature = slope * year + intercept
print("First year with predicted temp >= 40F:", year)

# Additional info
print("DataFrame shape (rows, columns):", nyc.shape)
print("Column names:", nyc.columns.tolist())
min_temp = nyc.Temperature.min()
max_temp = nyc.Temperature.max()
min_year = nyc.Date[nyc.Temperature.idxmin()]
max_year = nyc.Date[nyc.Temperature.idxmax()]
print(f"Minimum temperature: {min_temp}F in {min_year}")
print(f"Maximum temperature: {max_temp}F in {max_year}")
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
temps = [(f, c(f)) for f in range(0, 101, 10)]
temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
# End of script
