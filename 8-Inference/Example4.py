#determine whether these Land.Contour of the property is dependent on the Sale.Price of the property
import pandas as pd
import scipy.stats as stats
# code starts here
path='Test.csv'
df = pd.read_csv(path)

# categorize the SalePrice into three buckets
price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])

# make a frequency table with Land.Conotur
observed = pd.crosstab(df['Land.Contour'],price)

print(observed)

# conduct the chi-square test with the above frequency table
chi2, p, dof, ex = stats.chi2_contingency(observed)

print("Chi-square statistic = ",chi2)
print("p-value = ",p)
# the p-value is less than 5% significance level hence there is enough evidence against the null hypothesis and hence we can state that the variable of Land.Contour and Sale.Price are not independent of each other.