import pandas as pd
from graph import Graph
import ast


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
    #print(g.users[username].__dict__)
    user_obj = g.users[username]
    friend_ids = user_obj.getFriends()
    friend_usernames = [g.id_to_user_object[fid].username for fid in friend_ids if fid in g.id_to_user_object]

    print("\n-----------------------------------------------------------")
    print("Profile (Raw Data View):")
    print(f"User ID: {user_obj.getID()}")
    print(f"Username: {user_obj.username}")
    print(f"Destination: {user_obj.getDestination()}")
    print(f"Travel Date: {user_obj.getDate()}")
    print(f"Friends (Usernames): {friend_usernames}")
    print("-----------------------------------------------------------\n")

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
file_path = 'dataset_final.xlsx'
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
    #friends = df.iloc[i, 3]
    friends_raw = df.iloc[i, 3]
    if isinstance(friends_raw, str):
        try:
            friends = ast.literal_eval(friends_raw)
        except:
            friends = []
    else:
        friends = friends_raw

    date = df.iloc[i, 4]
    #edit so that date is read and then written in date form instead of int format its in

    # insert into the graph
    if username == "william79":
        print(username, friends, destination, date, id)
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
        print("-----------------------------------------------------------")
        n = int(input("Max date range: "))
        max_users = int(int(input("Max number of users: ")))
        print("\nSearch results:")

        destination = g.getDestination(username)
        int_date = g.getDate(username)

        from datetime import datetime
        #date_obj = datetime.strptime(str(int_date), "%Y%m%d").date()

        bfs_results, bfs_time = g.getBFSTime(destination, int_date, username, n, max_users)
        dfs_results, dfs_time = g.getDFSTime(destination, int_date, username, n, max_users)

        print("\nBFS Results:")
        if len(bfs_results) == 0:
            print("No rides found!")
        else:
            for friend in bfs_results:
                travel_date = datetime.strptime(str(g.getDate(friend)), "%Y-%m-%d").date()
                print(f"{friend} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        print(f"BFS Search Time: {bfs_time:.6f} seconds")

        print("\nDFS Results:")
        if len(dfs_results) == 0:
            print("No rides found!")
        else:
            for friend in dfs_results:
                travel_date = datetime.strptime(str(g.getDate(friend)), "%Y-%m-%d").date()
                print(f"{friend} (Travel Date: {travel_date.strftime('%Y-%m-%d')})")
        print(f"DFS Search Time: {dfs_time:.6f} seconds\n")


    elif choice == '3':
        print("-----------------------------------------------------------")
        username = login()
    elif choice == '4':
        break
    else:
        print("\nPlease select a valid option.")
    choice = displayMenu(username)

