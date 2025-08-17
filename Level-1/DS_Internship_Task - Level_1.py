# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\91812\OneDrive\Desktop\cognifyz\Dataset .csv")

# View top 10 rows of the dataset
print(data.head(10))

# Number of rows and columns
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

# Duplicate Value Count
dup = data.duplicated().sum()
print("Number of duplicate rows:", dup)

# Missing values
missing_values = data.isna().sum().sum()
print("Missing values count:", missing_values)

# Empty values
empty_values = (data == "").sum().sum()
print("Empty values count:", empty_values)

# Which columns have empty values?
empty_values_count = (data == "").sum()
print("Empty Values Count:\n", empty_values_count)

# Remove rows where 'Cuisines' is empty
if "Cuisines" in data.columns:
    data = data[data["Cuisines"].str.strip() != ""]

# Verify again
print("Empty values count after cleaning:", (data == "").sum().sum())

# Dataset info
print(data.info())

# Distribution of target variable ("Aggregate rating")
if "Aggregate rating" in data.columns:
    target_counts = data["Aggregate rating"].value_counts().sort_index()
    print("Distribution of target variable:\n", target_counts)

    plt.figure(figsize=(8,5))
    sns.countplot(x="Aggregate rating", data=data, palette="Blues")
    plt.title("Distribution of Aggregate Rating")
    plt.show()

    if all(target_counts >= target_counts.mean()):
        print("The distribution of the target variable is balanced.")
    else:
        print("The distribution of the target variable is imbalanced.")

# Descriptive Analysis
numeric_columns = data.select_dtypes(include=[np.number])
print(numeric_columns.describe())

print("Standard deviation for numerical columns:")
print(numeric_columns.std())

# Distribution of Country Codes
plt.figure(figsize=(8,5))
sns.countplot(x="Country Code", data=data, palette="Blues")
plt.title("Distribution of Restaurants by Country Codes")
plt.xticks(rotation=90)
plt.show()

# Top 10 Cities
top_10_cities = data["City"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_10_cities.index, x=top_10_cities.values, color="steelblue")
plt.title("Top 10 Cities with Highest Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.show()

# Top 10 Cuisines
top_10_cuisines = data["Cuisines"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_10_cuisines.index, x=top_10_cuisines.values, color="steelblue")
plt.title("Top 10 Cuisines with Highest Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisines")
plt.show()

print("Top 10 Cuisines:\n", top_10_cuisines)
print("Top 10 Cities:\n", top_10_cities)

# Geospatial Analysis
if {"Longitude","Latitude"}.issubset(data.columns):
    plt.figure(figsize=(12,6))
    plt.scatter(data["Longitude"], data["Latitude"], alpha=0.5, c="red", s=10, label="Restaurants")
    plt.title("Restaurant Locations")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.show()

# Correlation between location and rating
if {"Latitude","Longitude","Aggregate rating"}.issubset(data.columns):
    corr = data[["Latitude","Longitude","Aggregate rating"]].corr()
    plt.figure(figsize=(6,5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    plt.title("Correlation Between Restaurant Location and Rating")
    plt.show()
