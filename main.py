import pandas as pd
import matplotlib.pyplot as plt

# import numpy as np


sample_df = pd.read_csv("train.csv")
summary = sample_df.describe()


sample_df.head()

# sample_df.boxplot(column=["MedInc", "HouseAge"], grid=False)
# print(sample_df.describe())

# plt.figure()
# plt.boxplot(sample_df[1:])
# plt.plot()
# # plt.show()
# plt.savefig('fig/sample.png')


# Drop the 'ID' column before plotting
df_without_id = sample_df.drop(columns=["id", "Population"])

# Create a box plot for all columns in the dataframe excluding 'ID'
plt.figure(figsize=(8, 6))
df_without_id.boxplot()
plt.title("Box and Whisker Plot (Excluding ID)")
plt.ylabel("Value")
# plt.show()
plt.savefig("fig/sample2.png")


def add(a, b):
    return a + b
