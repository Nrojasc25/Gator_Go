import pandas as pd
from graph import Graph

# this doesn't work.
def displayMenu(username):
    print("---------------------")
    print("\nHello " + username)
    print("\nMenu: \n")
    print("1. View Account \n2. Search Friends \n3. Log Out\n")
    print("---------------------")
    choice = input("\nPlease select a choice from the menu: ")

    if choice == 1:
        # Display User ID, User Name, Destination, Travel Date
        # display main menu
        print("Profile:\n")
        print("User ID: ")
        print("User Name: ")
        print("Destination: ")
        print("Travel Date: \n")
        displayMenu(username)

    elif choice == 2:
        # display search results 
        print("Search results:")

    elif choice == 3:
        username = login()

    else:
        print("\nPlease select a valid option.")
        choice = displayMenu(username)

def login():
    print("Welcome to GatorGo!")
    username = input("\nPlease enter your username: ")
    while g.searchUserName(username) == False:
        print("\nCould not find user, please try again.\n")
        g.tempInsert(username) 
        username = input("Please enter your username: ")
    return username

'''
Instructions to run on terminal: 

pip install pandas
pip install openpyxl
python build.py 
'''

# dataset format: 
# User ID (int)    User Name (str)    Destination (int)     Friends (list of str)     Date of Travel (int)

'''
Instructions for reading the file

Display the first few rows of the dataframe
print(df.head())

Access a specific column
column_data = df['column header']

Access a specific row (by index)
row_data = df.iloc[index]         
'''


# SETUP FOR READING THE FILE

# Set the file path and read into DataFrame (df)
file_path = 'dataset_group.xlsx'
df = pd.read_excel(file_path)

print(df.head()) # for TESTING

# Get number of user (number of userIDS)
userIDS = df['User ID']  
print("Number of users: " + str(userIDS.size)) # for TESTING

# FOR TESTING
print("first 5 users:")
for i in range (5):
    userId = df.iloc[i, 0]
    userName = df.iloc[i, 1]
    print("USER ID: " + str(userId) + " USER NAME: " + userName)

# CREATING THE GRAPH FROM FILE DATA
g = Graph()
# for each user in file, insert
#                        set userID, userName, destination, friends, travelDate

# when setting userID, append 0s at the beginning so they're all the same size (6 digits) 
print()

# PROGRAM RUN

username = login()
displayMenu(username)

# if choice == 1:
#     # Display User ID, User Name, Destination, Travel Date
#     # display main menu
#     print("Profile:\n")
#     print("User ID: ")
#     print("User Name: ")
#     print("Destination: ")
#     print("Travel Date: \n")
#     choice = displayMenu()

# elif choice == 2:
#     # display search results 
#     print("Search results:")
# elif choice == 3:
#     username = login()
# else:
#     print("\nPlease select a valid option.")
#     choice = displayMenu()