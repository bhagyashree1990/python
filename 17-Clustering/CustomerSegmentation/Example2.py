# Create an Offer-Transaction pivot table
from Example1 import df
# Code starts here
# create pivot table
matrix = df.pivot_table(index='Customer Last Name',columns='Offer #',values='n')

# replace missing values with 0
matrix.fillna(0,inplace=True)

# reindex pivot table
matrix.reset_index(inplace=True)

# display first 5 rows
print(matrix.head())
# Code ends here