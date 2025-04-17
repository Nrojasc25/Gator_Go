import pandas as pd
from graph import Graph
# To run on terminal: 
# pip install pandas 
# pip install openpyxl
# python main.py 



# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'dataset_group.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
# To run: type python main.py on terminal.
print(df.head())

# Access a specific column
column_data = df['User ID']  # Replace 'ColumnName' with the actual column name
print(column_data)

# Access a specific row by index
row_data = df.iloc[0]  # Access the first row
print(row_data)

'''
create the graph here with dataset info
'''

users = Graph()
output = users.display()

expectedOutput = [
    "A -> ['B', 'C']",
    "B -> ['D']",
    "C -> []",
    "D -> []",
    "E -> []]"
]

if(output == expectedOutput):
    print("true")
else:
    print("false")