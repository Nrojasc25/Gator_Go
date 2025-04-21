import pandas as pd
from graph import Graph

'''
Instructions to run on terminal: 
pip install pandas
pip install openpyxl
python build.py 
'''

# HELPER FUNCTIONS

def displayMenu(username):
    print("-----------------------------------------------------------")
    print("\nHello " + username+"!")
    print("\nMenu:")
    print("1. View Account   2. Search Friends   3. Log Out   (4. Exits Program)")
    return input("\nPlease select a choice from the main menu: ")

def login():
    print("\n\nWelcome to GatorGo!")
    username = input("\nPlease enter your username: ")
    while g.searchUsername(username) == False:
        print("\nIncorrect username, please try again.\n\n")
        username = input("Please enter your username: ")
    return username

# SETUP FOR READING THE FILE
'''
Instructions for reading the file:
Access a specific column
column_data = df['column header']

Access a specific row (by index)
row_data = df.iloc[index]         
'''
# Set the file path and read into DataFrame (df)
file_path = 'dataset_draft2.xlsx'
print("\nREADING PROGRAM DATA...")
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe (for testing program functionality)
print("\nDISPLAYING FIRST FEW ROWS OF DATASET FOR TESTING PROGRAM FUNCTIONALITY\n")
print(df.head())

# CREATING THE GRAPH FROM FILE DATA
g = Graph()

# Get number of user (number of userIDS)
print("\nBUILDING GRAPH...")
numUsers = len(df['User ID'])
for i in range(0, numUsers):

    # get User's data

    # dataset format: User ID (int)  User Name (str)  Destination (int)   Friends (list of str)   Date of Travel (int)
    id = df.iloc[i, 0] # what if i change the index for 'name'??
    username = df.iloc[i, 1]
    destination = df.iloc[i, 2]
    friends = df.iloc[i, 3]
    date = df.iloc[i, 4]

    # insert into the graph
    g.insert(username, friends, destination, date, id)

# PROGRAM RUN
print("\nPROGRAM START")
username = login()
choice = displayMenu(username)

while True:
    if choice == '1':
        # Display User ID, User Name, Destination, Travel Date
        # display main menu
        print("-----------------------------------------------------------")
        print("\nProfile:\n")
        print("User ID: " + str(g.getID(username)))
        print("User Name: " + username)
        print("Destination: " + g.getDestination(username))
        print("Travel Date: " + str(g.getDate(username)) +"\n") # change to getFormattedDate
    elif choice == '2':
        # display search results 
        print("-----------------------------------------------------------")
        print("\nSearch results:")
    elif choice == '3':
        print("-----------------------------------------------------------")
        username = login()
    elif choice == '4':
        break
    else:
        print("\nPlease select a valid option.")
    choice = displayMenu(username)

