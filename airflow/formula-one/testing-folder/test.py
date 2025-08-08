# File used for testing purposes such as GET requests from openf1.org
import requests 
from datetime import date, time 

date_retrieval = '2025-08-03' #last grand prix as of 08/07/2025
response = requests.get(f'https://api.openf1.org/v1/sessions?date_start>={date_retrieval}')
data = response.json()
print(data)
print(f'Session Key: {data[0]["session_key"]}')
print(f'Meeting Key: {data[0]["meeting_key"]}')

# Next time: start extracting data, do not worry about formatting just yet, just extract with session_key, meeting_key. 
# Make sure you have a function that ensures you are extracting data from race day, not any other race format. 