import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv('C:/Users/VISHAL/Downloads/global-meat-production.csv')

# Step 2: Group and unstack (equivalent to pivot)
grouped = df.groupby(['Entity', 'Year'])['Meat, total | 00001765 || Production | 005510 || tonnes'].sum()
table = grouped.unstack('Year')  # Rows = Entity, Columns = Year

# Step 3: Save the table to Excel
table.reset_index().to_excel('C:/Users/VISHAL/Downloads/global-meat-production.xlsx', index=False)
print("Excel file created successfully!")

# Step 4: Plot a heatmap
# plt.figure(figsize=(15, 6))
plt.imshow(table, aspect='auto', cmap='Blues')
plt.title('Meat Production by Region and Year')
plt.xlabel('Year')
plt.ylabel('Region')
plt.xticks(range(len(table.columns)), table.columns, rotation=90)
plt.yticks(range(len(table.index)), table.index)
plt.colorbar(label='Production (tonnes)')
# plt.tight_layout()
plt.show()
