#used to update garmin_display on home assistant
#ran with regualr crontab
import get_data
import calc
import get_time
import credentials
from requests import post
import datetime

def ft(x):
    return str("{0:.1f}".format(x))

my_dict = get_data.my_filtered_activities() #get master dictionary
#Week
weekly_dict = calc.weekly_stats(my_dict) #use weekly_stats to calculate weekly dictionary (monday first)
this_week = sorted(weekly_dict.keys())[-1] #find key for latest week
#month
def MTD(dictionary,months_ago): #month to date
    month_total_dict = calc.monthly_daily_totals(dictionary,months_ago,'distance_miles')
    if month_total_dict.keys():
        return month_total_dict[max(month_total_dict.keys())] #finds highest date, uses that date to find value
    else:
        return 0
this_month = MTD(my_dict.copy(),0)
#Year
def yearly(master_dict):
    #adapted from build.py
    now = datetime.datetime.now()
    ytd_dict = master_dict.copy()
    for key in list(master_dict):
        if key < get_time.FOY():
            del ytd_dict[key]
    ytd_miles = []
    for run in ytd_dict:
        ytd_miles.append(float(ytd_dict[run]['distance_miles']))
    return sum(ytd_miles)
this_year = yearly(my_dict)
#All time
at_miles = []
for run in my_dict:
    at_miles.append(float(my_dict[run]['distance_miles']))
all_time = sum(at_miles)

output = ft(weekly_dict[this_week]['miles_ran'])+" - "+ft(this_month)+" - "+ft(this_year)#+" * "+ft(all_time)
print (datetime.datetime.now())
print(output)

headers = {"Authorization": "Bearer "+credentials.api_token,
           'content-type': 'application/json'}

url = credentials.api_url+"/api/states/sensor.garmin_display"
data = '{"state": "'+str(output)+'", "attributes": {"unit_of_measurement": "Miles"}}'
response = post(url, headers=headers, data=data)
