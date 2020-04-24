#import packages
import pandas as pd
# Create DataFrames : From series
#construct the dataframe
df = pd.DataFrame({'Name':pd.Series(['Rob','Bobby','John','Danny','Manny'],index=['R','B','J','D','M']),
                    'Age':pd.Series([25,30,21,32,23],index=['R','B','J','D','M'])})
#display
print(df)