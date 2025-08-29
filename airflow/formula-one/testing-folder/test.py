# File used for testing purposes such as GET requests from openf1.org
import requests 
from datetime import date, time 

date_retrieval = '2025-08-03' #last grand prix as of 08/07/2025
response = requests.get(f'https://api.openf1.org/v1/sessions?date_start>={date_retrieval}')
data = response.json()
print(data)
print(f'Session Key: {data[0]["session_key"]}')
print(f'Meeting Key: {data[0]["meeting_key"]}')

session_race_key = data[0]["session_key"] #use this as the main key for race
meeting_race_key = data[0]["meeting_key"]
print('current race session key is: ', session_race_key)


# Drivers
driver_response = requests.get(f'https://api.openf1.org/v1/drivers?session_key={session_race_key}')
driver_data = driver_response.json()
print('Driver data: ', driver_data)

print('Names of Drivers in Race Day with team name: ')
for driver in driver_data:
    print(f"{driver["full_name"]} #{driver['driver_number']} - {driver['team_name']}")
print('Total number of drivers: ', len(driver_data))

#overview of inital table
#       key                                                foreign key     foreign key?
#| session_key | session_name | name_acronym | full_name | driver_number | team_name |