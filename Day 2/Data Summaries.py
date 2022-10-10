Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import codecademylib3
import pandas as pd

movies = pd.read_csv('movies.csv')

# Print the first 5 rows 
print(movies.head())

# Print the summary statistics for all columns
print(movies.info())
print(movies.describe(include='all'))

SyntaxError: multiple statements found while compiling a single statement
Save the mean to mean_budget
mean_budget= movies.production_budget.mean()
print(mean_budget)
# Save the median to med_budget
med_budget=movies.production_budget.median()
print(med_budget)
# Save the mode to mode_budget
mode_budget= movies.production_budget.mode()
print(mode_budget)
# Save the trimmed mean to trmean_budget
from scipy.stats import trim_mean
trmean_budget=trim_mean(movies.production_budget, proportiontocut=0.2)
print(trmean_budget)

# Save the range to range_budget
range_budget= movies.production_budget.max()-movies.production_budget.min()
print(range_budget)

# Save the interquartile range to iqr_budget
from scipy.stats import iqr
#iqr_budget= iqr(movies.production_budget)
iqr_budget=movies.production_budget.quantile(0.75)-movies.production_budget.quantile(0.25)
print(iqr_budget)

# Save the variance to var_budget
var_budget=movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget=movies.production_budget.std()
print(std_budget)

# Save the mean absolute deviation to mad_budget
mad_budget=movies.production_budget.mad()
print(mad_budget)
