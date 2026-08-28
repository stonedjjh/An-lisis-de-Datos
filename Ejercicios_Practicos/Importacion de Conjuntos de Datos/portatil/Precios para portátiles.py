import pandas as pd
import numpy as np

file_name="laptops.csv"

'''
Task #1: 
Load the dataset to a pandas dataframe named 'df'
Print the first 5 entries of the dataset to confirm loading.
'''
df = pd.read_csv(file_name,header=None)
print(df.head(5))

'''
Task #2: 
Assign the following columns to the dataframe.
Manufacturer, Category, Screen, GPU, OS, CPU_core, Screen_Size_inch, CPU_frequency, RAM_GB, Storage_GB_SSD, Weight_kg, Price
Print the first 10 entries of the dataframe to confirm loading.
'''
header = [ "Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = header
print(df.head(10))

'''
Task #3: 
Replace '?' with 'NaN'
Replace the '?' entries in the dataset with NaN value, recevied from the Numpy package.
'''
df.replace('?',np.nan, inplace = True)

'''
Task #4: 
Print the data types of the dataframe columns
'''
print(df.dtypes)

'''
Task #5: 
Print the statistical description of the dataset, including that of 'object' data types.
'''
print(df.describe(include='all'))

'''
Task #6: 
Print the summary information of the dataset.
'''
print(df.info())