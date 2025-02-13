# Author: Bini Chandra
# Date: 02/12/2025
# This python file contains the code written for HW4 PART1 where I have normalized and standardized the Iris dataset.

# Importing necessary libraries
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Data/Iris.csv")
print("Original Iris Dataset:")
print(df.head())

################################################## Normalization #########################################################

# Exclude categorical column "Species" from the dataset
normalized_df = df.drop(columns=["Species"])

for col in normalized_df.columns:

    # Finding the minimum and maximum value of each column and the range
    min = normalized_df[col].min()
    max = normalized_df[col].max()
    range = max - min
    
    # Appying the normalization formula
    normalized_df[col] = (normalized_df[col] - min) / range

# Adding "Species" column back to the normalized dataset
normalized_df["Species"] = df["Species"]
print("\nNormalized Iris Dataset:")
print(normalized_df.head())

# Saving the generated normalized dataset to a csv file
normalized_df.to_csv("GeneratedData/Normalized_Iris.csv", index=False)

################################################## Standardization #########################################################

# Exclude categorical column "Species" from the dataset
standardized_df = df.drop(columns=["Species"])

for col in standardized_df.columns:

    # Finding the mean and standard deviation of each column
    mean = standardized_df[col].mean()
    std = standardized_df[col].std()
    
    # Appying the standardization formula
    standardized_df[col] = (standardized_df[col] - mean) / std

# Adding "Species" column back to the standardized dataset
standardized_df["Species"] = df["Species"]
print("\nStandardized Iris Dataset:")
print(standardized_df.head())

# Saving the generated standardized dataset to a csv file
standardized_df.to_csv("GeneratedData/Standardized_Iris.csv", index=False)