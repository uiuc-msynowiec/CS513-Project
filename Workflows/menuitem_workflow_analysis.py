import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_before = pd.read_csv("../NYPL-menus/MenuItem.csv", usecols=["price"])
data_after = pd.read_csv("../NYPL-menus/MenuItem_cleaned.csv", usecols=["price"])

rows_before = len(data_before)
rows_after = len(data_after)
rows_removed = rows_before - rows_after
print(f"Rows removed during cleaning: {rows_removed} ({(rows_removed / rows_before):.2%})")

plt.figure(figsize=(10, 5))
sns.histplot(data_before['price'].dropna(), bins=100, color='red', label = 'Before')
sns.histplot(data_after['price'].dropna(), bins=100, color='blue', label = 'After')

plt.title("Price Distribution Before vs After Cleaning")
plt.xlabel("Price")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.savefig("workflow_menuitem_cleaning.png")
plt.close()


#@begin FilterPrice
#@in MenuItem.csv
#@out MenuItem_cleaned.csv
#@param threshold=0
#@desc Remove menu items where price <= 0
#@note Removed approx 33% of rows due to zero or missing prices
#@end FilterPrice