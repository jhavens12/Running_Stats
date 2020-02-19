import get_data
import calc
import credentials
from requests import post


my_dict = get_data.my_filtered_activities() #get master dictionary
weekly_dict = calc.weekly_stats(my_dict) #use weekly_stats to calculate weekly dictionary (monday first)

this_week = sorted(weekly_dict.keys())[-1] #find key for latest week



output = str(weekly_dict[this_week]['run_count'])+"R "+str(weekly_dict[this_week]['miles_ran'])+"M"


headers = {"Authorization": "Bearer "+credentials.api_token,
           'content-type': 'application/json'}

url = credentials.api_url+"/api/states/sensor.garmin_display"
data = '{"state": "'+str(output)+'", "attributes": {"unit_of_measurement": "Miles"}}'
response = post(url, headers=headers, data=data)
