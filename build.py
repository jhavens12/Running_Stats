import get_time
import get_data
import calc
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import pylab
from io import BytesIO
from pprint import pprint
import datetime #recently added
import math #recently added


runs_per_week = 3

master_dict = get_data.my_filtered_activities()

def period(Sunday,Monday): #given master dict copy, and then 0 and 1 for last week

    main_dict = {} #main dictionary to add values to and then return

    dict_1 = master_dict.copy() #create dictionary to manipulate

    #Filter out entries
    for key in master_dict:
        if key > get_time.LS(Sunday):
            del dict_1[key]
    for key in master_dict:
        if key < get_time.LM(Monday):
            del dict_1[key]

    past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))}
    past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))}
    past_run_count = calc.activity_count(past_dict)
    past_mile_list = []
    for i in past_dict:
        past_mile_list.append(float(past_dict[i]['distance_miles']))
    past_miles = ("{0:.2f}".format(sum(past_mile_list)))
    past_ten_percent = ("{0:.2f}".format(float(past_miles) * .1))

    #create lists of items to display
    past_run_title_label = []
    for i in list(sorted(past_dict)):
        past_run_title_label.append(past_dict[i]['weekday_short_date'])
    past_run_mile_label = []
    for i in list(sorted(past_dict)):
        past_run_mile_label.append(past_dict[i]['distance_miles'])
    past_run_pace_label = []
    for i in list(sorted(past_dict)):
        past_run_pace_label.append(past_dict[i]['pace'])
    past_run_elapsed_label = []
    for i in list(sorted(past_dict)):
        past_run_elapsed_label.append(str(past_dict[i]['elapsed']))
    past_run_treadmill_label = []
    for i in list(sorted(past_dict)):
        past_run_treadmill_label.append(str(past_dict[i]['total_elevation_feet']))

    #remaining(past_ten_percent,past_miles,runs_per_week)

    #label1= v['label1']
    main_dict['title'] = (get_time.convert_weekday_full(get_time.LM(Monday)) + " - " + get_time.convert_weekday_full(get_time.LS(Sunday)))

    #label4= v['label4']
    main_dict['subtitle_title'] = 'Past Ten Percent'
    main_dict['subtitle_value'] = str(past_ten_percent)

    #label5= v['label5']
    main_dict['box_titles'] = ['Date','Distance','Pace','Duration','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(past_run_title_label))

    #label6= v['label6']
    main_dict['box_values'].append("\n".join(past_run_mile_label))

    #abel7= v['label7']
    main_dict['box_values'].append("\n".join(past_run_pace_label))

    #label8= v['label8']
    main_dict['box_values'].append("\n".join(past_run_elapsed_label))

    #label9= v['label9']
    main_dict['box_values'].append("\n".join(past_run_treadmill_label))


    #BOTTOM VALUES
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []


    main_dict['total_values'].append(str(past_miles))

    dec_pace_list = []
    for i in list(sorted(past_dict)):
        dec_pace_list.append(past_dict[i]['pace_dec'])
    current_pace_average = get_data.convert_dec_time(sum(dec_pace_list)/len(dec_pace_list))
    #label504= v['label504']
    main_dict['total_values'].append(str(current_pace_average))

    seconds_elapsed_list = []
    for i in list(sorted(past_dict)):
        seconds_elapsed_list.append(past_dict[i]['elapsed_time'])
    total_elapsed_seconds = sum(seconds_elapsed_list)
    current_duration_total = get_data.convert_seconds_to_minutes(total_elapsed_seconds)
    #label505= v['label505']
    main_dict['total_values'].append(str(current_duration_total))

    current_elevation_list = []
    for i in list(sorted(past_dict)):
        current_elevation_list.append(float(past_dict[i]['total_elevation_feet']))
    current_elevation_total = sum(current_elevation_list)
    #label506= v['label506']
    main_dict['total_values'].append(str(current_elevation_total))

    return main_dict

def remaining(past_ten_percent,past_miles,runs_per_week):
    remaining_miles = ("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles)))

    label40= v['label40']
    label40.text = str(remaining_miles)

    label41= v['label41']
    if float(runs_per_week)-float(current_week_count) != 0:
        miles_per_run_remaining = float(remaining_miles)/(runs_per_week-float(current_week_count))
        label41.text = format_text(miles_per_run_remaining)
    else:
        label41.text = "0"
