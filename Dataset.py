from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

florida_cities = [
    'Miami', 'Orlando', 'Tampa', 'Jacksonville', 'St. Petersburg',
    'Hialeah', 'Fort Lauderdale', 'Port St. Lucie', 'Tallahassee', 'Cape Coral',
    'Pembroke Pines', 'Hollywood', 'Gainesville', 'Miramar', 'Coral Springs',
    'Clearwater', 'Palm Bay', 'Miami Gardens', 'West Palm Beach', 'Lakeland',
    'Boca Raton', 'Naples', 'Sarasota', 'Fort Myers', 'Delray Beach',
    'Melbourne', 'Bradenton', 'Vero Beach', 'Palm Coast', 'Coconut Creek',
    'Boynton Beach', 'Sunrise', 'Winter Haven', 'Pensacola', 'St. Augustine',
    'Doral', 'Kissimmee', 'Weston', 'Aventura', 'Titusville',
    'Lake Worth', 'Altamonte Springs', 'Sanford', 'Winter Park', 'Wellington',
    'North Port', 'Punta Gorda', 'Ocala', 'Largo', 'Plantation',
    'Tarpon Springs', 'Fort Pierce', 'Suwannee', 'Gulfport', 'Indian Harbour Beach',
    'Key West', 'New Smyrna Beach', 'Port Orange', 'Greenacres',
    'Miami Beach', 'Dania Beach', 'Sun City Center', 'St. Petersburg Beach',
    'Seffner', 'Zephyrhills', 'Bonita Springs', 'Mount Dora', 'Sarasota Springs'
]


start_date = datetime(2025, 5, 1)
end_date = datetime(2025, 12, 31)

user_ids = [str(i).zfill(6) for i in range(1, 100001)]

user_id_to_name = {}
for user_id in user_ids:
    name = fake.user_name()[:20]  
    user_id_to_name[user_id] = name


travel_data = []

for user_id in user_ids:
    destination = random.choice(florida_cities)
    num_friends = random.randint(1, 10)
    friends = [str(random.randint(1, 100000)).zfill(6) for _ in range(num_friends)]

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    date_of_travel = start_date + timedelta(days=random_days)
    date_int = int(date_of_travel.strftime('%Y%m%d'))

    user_name = user_id_to_name[user_id]
    travel_data.append((user_id, user_name, destination, friends, date_int))

df = pd.DataFrame(travel_data, columns=['User ID', 'User Name', 'Destination', 'Friends', 'Date of Travel'])

df.to_excel('dataset.xlsx', index=False)

print(len(df))  
print(df.columns)
print(df.head())
