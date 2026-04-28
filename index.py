python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "data/Distribution_of_Active_Members_2022_0.xlsx"
data = pd.read_excel(file_path)

# Data Cleaning and Preparation
# Assuming the dataset has columns: 'Quarter', 'Sector', 'Age Band', 'Gender', 'Years of Service', 'Count'
data['Total'] = data.groupby('Quarter')['Count'].transform('sum')
data['Percentage'] = (data['Count'] / data['Total']) * 100

# Visualization: Active Members by Quarter
plt.figure(figsize=(10, 6))
data.groupby('Quarter')['Count'].sum().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Total Active Members per Quarter in 2022")
plt.xlabel("Quarter")
plt.ylabel("Number of Active Members")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output/active_members_per_quarter.png')
plt.show()

# Visualization: Distribution by Sector
sectors_data = data.groupby(['Quarter', 'Sector'])['Count'].sum().unstack()
sectors_data.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title("Active Members Distribution by Sector")
plt.xlabel("Quarter")
plt.ylabel("Number of Active Members")
plt.legend(title="Sector")
plt.tight_layout()
plt.savefig('output/sector_distribution.png')
plt.show()

