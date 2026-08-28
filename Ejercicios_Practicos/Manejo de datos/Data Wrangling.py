import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"

df = pd.read_csv(file_path, header=0)
print(df.info())

print(df.head())

df[['Screen_Size_cm']] = np.round(df[['Screen_Size_cm']],2)
print(df.head())

'''
Task - 1
Evaluate the dataset for missing data
Missing data was last converted from '?' to numpy.NaN. Pandas uses NaN and Null values interchangeably. This means, you can just identify the entries having Null values. Write a code that identifies which columns have missing data.
'''

missing_data = df.isnull()
print(missing_data.head())
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

'''
Task - 2
Replace with mean
Missing values in attributes that have continuous data are best replaced using Mean value. We note that values in "Weight_kg" attribute are continuous in nature, and some values are missing. Therefore, write a code to replace the missing values of weight with the average value of the attribute.
'''

# replacing missing data with mean
avg_weight=df['Weight_kg'].astype('float').mean(axis=0)
df["Weight_kg"] = df["Weight_kg"].replace(np.nan, avg_weight)

print(df.head())

# astype() function converts the values to the desired data type
# axis=0 indicates that the mean value is to calculated across all column elements in a row.

'''
Replace with the most frequent value
Missing values in attributes that have categorical data are best replaced using the most frequent value. We note that values in "Screen_Size_cm" attribute are categorical in nature, and some values are missing. Therefore, write a code to replace the missing values of Screen Size with the most frequent value of the attribute.
'''
common_screen_size = df['Screen_Size_cm'].value_counts().idxmax()
# df["Screen_Size_cm"].replace(np.nan, common_screen_size, inplace=True)
# This line thow a warning called ChainedAssign because it is not possible to modify the original object, 
# try to avoid an inplace operation use, because the intermediate object of the chained assignment is not assigned back to the 
# original object. The correct way to do this is to assign the result of the operation back to the original object as follows:
# df["Screen_Size_cm"] = df["Screen_Size_cm"].replace(np.nan, common_screen_size)
df["Screen_Size_cm"] = df["Screen_Size_cm"].replace(np.nan, common_screen_size)
print(df.head())
'''
Task - 3
Fixing the data types
Both "Weight_kg" and "Screen_Size_cm" are seen to have the data type "Object", while both of them should be having a data type of "float". Write a code to fix the data type of these two columns.
'''
df[["Weight_kg","Screen_Size_cm"]] = df[["Weight_kg","Screen_Size_cm"]].astype("float")
print(df.head())

'''
Task - 4¶
Data Standardization
The value of Screen_size usually has a standard unit of inches. Similarly, weight of the laptop is needed to be in pounds. Use the below mentioned units of conversion and write a code to modify the columns of the dataframe accordingly. Update their names as well.

1 inch = 2.54 cm
1 kg   = 2.205 pounds
'''

# Data standardization: convert weight from kg to pounds
df["Weight_kg"] = df["Weight_kg"]*2.205
df.rename(columns={'Weight_kg':'Weight_pounds'}, inplace=True)

# Data standardization: convert screen size from cm to inch
df["Screen_Size_cm"] = df["Screen_Size_cm"]/2.54
df.rename(columns={'Screen_Size_cm':'Screen_Size_inch'}, inplace=True)

print(df.head())

'''
Data Normalization
Often it is required to normalize a continuous data attribute. Write a code to normalize the "CPU_frequency" attribute with respect to the maximum value available in the dataset.
'''
df['CPU_frequency'] = df['CPU_frequency']/df['CPU_frequency'].max()
print(df.head())

'''
Task - 5
Binning
Binning is a process of creating a categorical attribute which splits the values of a continuous data into a specified number of groups. In this case, write a code to create 3 bins for the attribute "Price". These bins would be named "Low", "Medium" and "High". The new attribute will be named "Price-binned".
'''

bins = np.linspace(min(df["Price"]), max(df["Price"]), 4)
group_names = ['Bajo', 'Medio', 'Alto']
df['Price-binned'] = pd.cut(df['Price'], bins, labels=group_names, include_lowest=True )
print(df.head())

# Also, plot the bar graph of these bins.

plt.bar(group_names, df["Price-binned"].value_counts())
plt.xlabel("Precio")
plt.ylabel("Cantidad")
plt.title("Price bins")

print(plt.show())

'''
Task - 6
Indicator variables
Convert the "Screen" attribute of the dataset into 2 indicator variables, "Screen-IPS_panel" and "Screen-Full_HD". Then drop the "Screen" attribute from the dataset.
'''

#Indicator Variable: Screen
dummy_variable_1 = pd.get_dummies(df["Screen"])
dummy_variable_1.rename(columns={'IPS Panel':'Screen-IPS_panel', 'Full HD':'Screen-Full_HD'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)

# drop original column "Screen" from "df"
df.drop("Screen", axis = 1, inplace=True)

print(df.head())


