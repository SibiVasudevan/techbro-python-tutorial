import pandas as pd # The only import you need to crush it

# Create data like a chad
df = pd.DataFrame( {
    'Product' : ['Macbook', 'HP', 'Dell','Chromebook', 'Asus', 'Acer', 'Macbook', 'Dell'],
    'Revenue' : [2000, 1000, 800, 900, 950, 1200, 2500, 1250],
    'Units' : [50, 100, 150, 125, 115, 85, 40, 175],
    'Region': ['North', 'South', 'North', 'South', 'North', 'North','South', 'North']
})

df.head() # First  few rows
df.describe() # Statistical summary go brr
df.info() # Dataset info, no cap fr

df['Revenue'] #Select single column
df[['Product', 'Revenue']] # Multiple columns like a chad
df.loc[0] # Row selection for kings
df.iloc[1:3] # Integer-based selection for gigachads

# Boolean filtering ftw
high_revenue = df[df['Revenue'] > 900]
multi_condition = df[ (df['Revenue'] > 900) & (df['Units']> 90) ]

# Handling missing like a pro
df.dropna() # Drop those weak missing values
df.fillna(0) # Fill nulls

# Group by operations
grouped = df.groupby('Product').agg({
    'Revenue': 'sum',
    'Units': 'mean'
})

# Pivot operations - galaxy brain stuff 
pivot_table = df.pivot_table(
    values = 'Revenue',
    index = 'Product',
    columns = 'Region',
    aggfunc = 'sum'
)

# String operatins for the culture
df['Product'] = df['Product'].str.upper() # ALL CAPS BECAUSE WE SHOUTING
df['Product'] = df['Product'].str.replace('HP', 'OMEN') # Replace like a pro

