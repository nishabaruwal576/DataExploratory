Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Create a histogram for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close()
SyntaxError: multiple statements found while compiling a single statement
# Save the proportions to genre_props
genre_props= movies.genre.value_counts()/len(movies.genre)
print(genre_props)
# Save the counts to genre_counts
genre_counts=movies.genre.value_counts()
print(genre_counts)
SyntaxError: multiple statements found while compiling a single statement
# Create a bar chart for movie genre 
sns.countplot(x='genre',data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()