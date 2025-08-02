import pandas as pd
import matplotlib.pyplot as plt

data_before = pd.read_csv("../NYPL-menus/MenuItem.csv", usecols=["price"])
data_after = pd.read_csv("../NYPL-menus/MenuItem_cleaned.csv", usecols=["price"])

bins = [0, 1, 5, 10, 100, float('inf')]
labels = ['0-1', '1-5', '5-10', '10-100', '100+']

# Step 3: Categorize prices into bins
data_before['bin'] = pd.cut(data_before['price'], bins=bins, labels=labels, include_lowest=True)
data_after['bin'] = pd.cut(data_after['price'], bins=bins, labels=labels, include_lowest=True)

# Step 4: Count how many values fall into each bin
before_counts = data_before['bin'].value_counts().sort_index()
after_counts = data_after['bin'].value_counts().sort_index()

# Step 5: Combine into comparison DataFrame
bin_compare = pd.DataFrame({
    'Before': before_counts,
    'After': after_counts
})
bin_compare['Removed'] = bin_compare['Before'] - bin_compare['After']

# Step 6: Plot Before vs After bin counts
plt.figure(figsize=(10, 6))
bin_compare[['Before', 'After']].plot(kind='bar', figsize=(10, 6), color=['red', 'blue'])
plt.title("Count of MenuItem Prices by Bin (Before vs After Cleaning)")
plt.xlabel("Price Range")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("workflow_price_bin_comparison.png")
plt.close()

# Step 7: Save comparison as CSV
bin_compare.to_csv("price_bin_comparison.csv")
