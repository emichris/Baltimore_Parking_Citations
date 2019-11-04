# Parking Citation Analysis

import pandas as pd
import datetime as dt

print("Christian Emiyah's Project - TheDataIncubator")
data = pd.read_csv("../dataset/Parking_Citations.csv", low_memory = False)
pd.set_option('display.max_columns', None)
data.head(5);
data['Arrest Date'] = data['Arrest Date'].astype('datetime64[ns]')


# Check for missing and n/a values
data.isna().sum()
data.isnull().sum()

import matplotlib.pyplot as plt
count_Desc_groups = data.groupby(data['Description]').count()
print(count_Desc_groups.head(5))
count_Desc_groups.plot.bar(x='ViolCode', y='Citation')
plt.show()
