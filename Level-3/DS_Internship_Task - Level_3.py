# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv(r"C:\Users\91812\OneDrive\Desktop\cognifyz\Dataset .csv")
# Step 3: Show the first 5 rows of the dataset
print("First 5 rows of dataset:")
display(data.head())

# Step 4: Get basic information about the dataset
print("\nDataset Info:")
display(data.info())

# Step 5: Check for missing values
print("\nMissing Values:")
display(data.isnull().sum())

# Step 6: Basic statistics
print("\nDescriptive Statistics:")
display(data.describe())

# Step 7: Visualization examples
## Histogram of first numeric column
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_columns) > 0:
    plt.figure(figsize=(6,4))
    plt.hist(data[numeric_columns[0]], bins=20, edgecolor="black")
    plt.title(f"Histogram of {numeric_columns[0]}")
    plt.xlabel(numeric_columns[0])
    plt.ylabel("Frequency")
    plt.show()
else:
    print("\nNo numeric columns to plot.")

# Step 8: Correlation heatmap (if numeric columns exist)
if len(numeric_columns) > 1:
    corr = data[numeric_columns].corr()
    plt.figure(figsize=(6,4))
    plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
    plt.colorbar()
    plt.title("Correlation Heatmap")
    plt.xticks(range(len(corr)), corr.columns, rotation=45)
    plt.yticks(range(len(corr)), corr.columns)
    plt.show()
else:
    print("\nNot enough numeric columns for correlation heatmap.")
