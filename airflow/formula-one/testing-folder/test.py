# File used for testing purposes such as GET requests from openf1.org
import requests 
from datetime import date, time 

date_retrieval = '2025-08-31' #last grand prix as of 08/31/2025

# Race Session Info 
# Could use ..../v1/meetings to get the name of the Grand Prix

response = requests.get(f'https://api.openf1.org/v1/sessions?date_start>={date_retrieval}&session_name=Race&session_type=Race')
data = response.json()
print(data)
print(f'Session Key: {data[0]['session_key']}')
print(f'Meeting Key: {data[0]['meeting_key']}')

session_race_key = data[0]['session_key'] #use this as the main key for race
meeting_race_key = data[0]['meeting_key']
location = data[0]['location']

print('Current Race session key is: ', session_race_key)
print('Current Race location: ', location)

print('----------------------------------')
# Drivers
driver_response = requests.get(f'https://api.openf1.org/v1/drivers?session_key={session_race_key}')
driver_data = driver_response.json()
#print('Driver data: ', driver_data)

print('Names of Drivers in Race Day with team name: ')
for driver in driver_data:
    print(f"{driver["full_name"]} #{driver['driver_number']} - {driver['team_name']}")
print('Total number of drivers: ', len(driver_data))


print('----------------------------------')
# Race Results
race_results_response = requests.get(f'https://api.openf1.org/v1/session_result?session_key={session_race_key}')
race_results_data = race_results_response.json()
print('Race Results:')
for driver in race_results_data:
    # Data does not include driver's name, only driver number. Need to match with driver data above.
    driver_info = next((d for d in driver_data if d['driver_number'] == driver['driver_number']), None)
    if driver_info:
        if driver['dnf'] == True:
            print(f"Place: DNF - {driver_info['full_name']} - {driver_info['team_name']}")
        else:
            print(f"Place: {driver['position']} - {driver_info['full_name']} - {driver_info['team_name']}")

#overview of inital table
#       key                                                foreign key     foreign key?
#| session_key | session_name | name_acronym | full_name | driver_number | team_name |