# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv(r"C:\Users\91812\OneDrive\Desktop\cognifyz\Dataset .csv")

# View top 10 rows of the dataset
display(data.head(10))


# ----------------------------------------------------------
# Task 1: TABLE BOOKING AND ONLINE DELIVERY
# ----------------------------------------------------------

# Total number of restaurants
total_num_restaurants = len(data)

# Percentage of restaurants that offer table booking and online delivery
table_booking_percentage = (data['Has Table booking'].eq('Yes').sum() / total_num_restaurants) * 100
online_delivery_percentage = (data['Has Online delivery'].eq('Yes').sum() / total_num_restaurants) * 100

print(f"Percentage of restaurants that offer Table Booking: {table_booking_percentage:.2f}%")
print(f"Percentage of restaurants that offer Online Delivery: {online_delivery_percentage:.2f}%")


# Compare the average ratings of restaurants with table booking and those without
avg_rating_with_table = data.loc[data['Has Table booking'] == 'Yes', 'Aggregate rating'].mean()
avg_rating_without_table = data.loc[data['Has Table booking'] == 'No', 'Aggregate rating'].mean()

print(f"Average rating with Table Booking: {avg_rating_with_table:.2f}")
print(f"Average rating without Table Booking: {avg_rating_without_table:.2f}")


# Analyze the availability of online delivery among restaurants with different price ranges
def price_range(cost):
    if cost < 500:
        return 'Low'
    elif 500 <= cost <= 1000:
        return 'Medium'
    else:
        return 'High'

data['Price Range Category'] = data['Average Cost for two'].apply(price_range)

online_delivery_by_price_range = pd.crosstab(data['Price Range Category'], data['Has Online delivery'], normalize='index') * 100
print("Online Delivery Availability by Price Range:\n", online_delivery_by_price_range)

# Bar plot
plt.figure(figsize=(6,4))
sns.countplot(data=data, x='Price Range Category', hue='Has Online delivery', palette='Set2')
plt.title("Online Delivery Availability by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.show()


# ----------------------------------------------------------
# Task 2: PRICE RANGE ANALYSIS
# ----------------------------------------------------------

# Most common price range among all the restaurants
most_common_price_range = data['Price range'].mode()[0]
print("Most Common Price Range:", most_common_price_range)

# Calculate the average rating for each price range
avg_rating_by_price_range = data.groupby('Price range')['Aggregate rating'].mean().reset_index()
print("Average rating for each price range:\n", avg_rating_by_price_range.round(2))

# Identify the price range with the highest average rating
highest_avg_rating_idx = avg_rating_by_price_range['Aggregate rating'].idxmax()

# Bar plot
plt.figure(figsize=(6,4))
colors = ['red' if i == highest_avg_rating_idx else 'blue' for i in range(len(avg_rating_by_price_range))]
plt.bar(avg_rating_by_price_range['Price range'], avg_rating_by_price_range['Aggregate rating'], color=colors)
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.title("Average Rating by Price Range")
plt.show()


# ----------------------------------------------------------
# Task 3: FEATURE ENGINEERING
# ----------------------------------------------------------

# Extract additional features: length of restaurant name and address
data['Restaurant Name Length'] = data['Restaurant Name'].str.len()
data['Address Length'] = data['Address'].str.len()

display(data[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Length']].head())

# Create new binary features for table booking and online delivery
data['Has Table Booking (Encoded)'] = data['Has Table booking'].map({'Yes': 1, 'No': 0})
data['Has Online Delivery (Encoded)'] = data['Has Online delivery'].map({'Yes': 1, 'No': 0})

display(data.head())
