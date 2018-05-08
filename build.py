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


runs_per_week = 4

master_dict = get_data.my_filtered_activities()

def format_text(x):
    return str("{0:.2f}".format(x))

def period(Sunday,Monday,current_info): #given master dict copy, and then 0 and 1 for last week

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

    #bottom values
    dec_pace_list = []
    for i in list(sorted(past_dict)):
        dec_pace_list.append(past_dict[i]['pace_dec'])
    current_pace_average = get_data.convert_dec_time(sum(dec_pace_list)/len(dec_pace_list))

    seconds_elapsed_list = []
    for i in list(sorted(past_dict)):
        seconds_elapsed_list.append(past_dict[i]['elapsed_time'])
    total_elapsed_seconds = sum(seconds_elapsed_list)
    current_duration_total = get_data.convert_seconds_to_minutes(total_elapsed_seconds)

    current_elevation_list = []
    for i in list(sorted(past_dict)):
        current_elevation_list.append(float(past_dict[i]['total_elevation_feet']))
    current_elevation_total = sum(current_elevation_list)

    main_dict['title'] = (get_time.convert_weekday_full(get_time.LM(Monday)) + " - " + get_time.convert_weekday_full(get_time.LS(Sunday)))

    main_dict['subtitle_title'] = 'Past Ten Percent'
    main_dict['subtitle_value'] = str(past_ten_percent)

    main_dict['box_titles'] = ['Date','Distance','Pace','Duration','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(past_run_title_label))
    main_dict['box_values'].append("\n".join(past_run_mile_label))
    main_dict['box_values'].append("\n".join(past_run_pace_label))
    main_dict['box_values'].append("\n".join(past_run_elapsed_label))
    main_dict['box_values'].append("\n".join(past_run_treadmill_label))

    #BOTTOM VALUES
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []
    main_dict['total_values'].append(str(past_miles))
    main_dict['total_values'].append(str(current_pace_average))
    main_dict['total_values'].append(str(current_duration_total))
    main_dict['total_values'].append(str(current_elevation_total))

    #calculate remaining
    current_miles = current_info['current_miles']
    current_week_count = current_info['current_week_count']

    remaining_miles = str("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles)))
    main_dict['remaining_miles'] = remaining_miles
    if float(runs_per_week)-float(current_week_count) != 0:
        miles_per_run_remaining = float(remaining_miles)/(runs_per_week-float(current_week_count))
        main_dict['remaining_per_run'] = format_text(miles_per_run_remaining)
    else:
        main_dict['remaining_per_run'] = "0"
    #

    return main_dict

def current_period():
    main_dict = {}
    dict_2 = master_dict.copy()

    #filter out old runs (older than monday)
    for key in master_dict:
        if key < get_time.LM(0):
            del dict_2[key]

    current_week_count = calc.activity_count(dict_2)
    main_dict['current_week_count'] = current_week_count #USED FOR CALCULATIONS

    mile_list = []
    for i in dict_2:
        mile_list.append(float(dict_2[i]['distance_miles']))
    current_miles = "{0:.2f}".format(sum(mile_list))
    main_dict['current_miles'] = current_miles #USED FOR CALCULATIONS
    current_run_title_label = []
    for i in list(sorted(dict_2)):
        current_run_title_label.append(dict_2[i]['weekday_short_date'])
    current_run_mile_label = []
    for i in list(sorted(dict_2)):
        current_run_mile_label.append(dict_2[i]['distance_miles'])
    current_run_pace_label = []
    for i in list(sorted(dict_2)):
        current_run_pace_label.append(dict_2[i]['pace'])
    current_run_elapsed_label = []
    for i in list(sorted(dict_2)):
        current_run_elapsed_label.append(str(dict_2[i]['elapsed']))
    current_run_treadmill_label = []
    for i in list(sorted(dict_2)):
        current_run_treadmill_label.append(str("{0:.2f}".format(dict_2[i]['total_elevation_feet'])))

    #bottom values
    dec_pace_list = []
    for i in list(sorted(dict_2)):
        dec_pace_list.append(dict_2[i]['pace_dec'])
    if len(dec_pace_list) != 0:
        current_pace_average = get_data.convert_dec_time(sum(dec_pace_list)/len(dec_pace_list))
    else:
        current_pace_average = 0

    seconds_elapsed_list = []
    for i in list(sorted(dict_2)):
        seconds_elapsed_list.append(dict_2[i]['elapsed_time'])
    total_elapsed_seconds = sum(seconds_elapsed_list)
    current_duration_total = get_data.convert_seconds_to_minutes(total_elapsed_seconds)

    current_elevation_list = []
    for i in list(sorted(dict_2)):
        current_elevation_list.append(float(dict_2[i]['total_elevation_feet']))
    current_elevation_total = sum(current_elevation_list)

    main_dict['title'] = (get_time.weekday(get_time.LM(0)) + " " + str(get_time.LM(0).day) + " - " + get_time.weekday(get_time.now()) + " " + str(get_time.now().day))
    main_dict['subtitle1_title'] = "Remaining:"
    main_dict['subtitle2_title'] = "Per Run:"
    main_dict['subtitle1_value'] = "0"
    main_dict['subtitle2_value'] = "0"

    main_dict['box_titles'] = ['Date','Distance','Pace','Duration','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(current_run_title_label))
    main_dict['box_values'].append("\n".join(current_run_mile_label))
    main_dict['box_values'].append("\n".join(current_run_pace_label))
    main_dict['box_values'].append("\n".join(current_run_elapsed_label))
    main_dict['box_values'].append("\n".join(current_run_treadmill_label))

    #totals at bottom
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []
    main_dict['total_values'].append(str(current_miles))
    main_dict['total_values'].append(str(current_pace_average))
    main_dict['total_values'].append(str(current_duration_total))
    main_dict['total_values'].append(str("{0:.2f}".format(current_elevation_total)))

    return main_dict

def monthly(runs_per_week):

    def MTD(dictionary,months_ago): #month to date
        month_total_dict = calc.monthly_daily_totals(dictionary,months_ago,'distance_miles')
        if month_total_dict.keys():
            return month_total_dict[max(month_total_dict.keys())] #finds highest date, uses that date to find value
        else:
            return 0

    main_dict = {}
    main_dict['flbox_titles'] = []
    main_dict['flbox_values'] = []
    main_dict['frbox_titles'] = []
    main_dict['frbox_values'] = []

    this_month_full = calc.monthly_daily_totals(master_dict.copy(),0,'distance_miles')
    last_month_full = calc.monthly_daily_totals(master_dict.copy(),1,'distance_miles')
    this_month = MTD(master_dict.copy(),0)
    last_month = MTD(master_dict.copy(),1)
    month_difference = this_month - last_month
    now = datetime.datetime.now()
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    days_remaining = LOM.day - now.day
    #runs_per_week = 3
    runs_remain = math.ceil(days_remaining*(runs_per_week/7))
    monthly_dict = calc.monthly_stats(master_dict.copy())
    max_miles = 0
    for month in monthly_dict:
        if monthly_dict[month]['miles_ran'] > max_miles:
            max_miles = int(monthly_dict[month]['miles_ran'])
            most_miles_month = month


    main_dict['title'] = "MONTH"
    #LABELS
    main_dict['flbox_titles'].append("This Month")
    main_dict['flbox_titles'].append("Run Count")
    main_dict['flbox_titles'].append("Last Month")
    main_dict['flbox_titles'].append("Run Count")
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("Runs Remain")
    main_dict['flbox_titles'].append("MPR Last Month")

    #DATA
    main_dict['flbox_values'].append(format_text(this_month))
    main_dict['flbox_values'].append(format_text(len(this_month_full)))
    main_dict['flbox_values'].append(format_text(last_month))
    main_dict['flbox_values'].append(format_text(len(last_month_full)))
    main_dict['flbox_values'].append(format_text(month_difference))
    main_dict['flbox_values'].append(format_text(runs_remain))
    main_dict['flbox_values'].append(format_text(abs(month_difference/runs_remain)))

    # #
    main_dict['frbox_titles'].append("50 Miles Goal")
    main_dict['frbox_titles'].append("MPR to 50M")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("Month Record")
    main_dict['frbox_titles'].append("MPR to Record")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")

    #
    main_dict['frbox_values'].append(format_text(this_month-50))
    main_dict['frbox_values'].append(format_text((50-this_month)/runs_remain))
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append(str(max_miles))
    main_dict['frbox_values'].append(format_text((max_miles-this_month)/runs_remain))
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append("")

    return main_dict

def yearly(runs_per_week):
    main_dict = {}
    main_dict['flbox_titles'] = []
    main_dict['flbox_values'] = []
    main_dict['frbox_titles'] = []
    main_dict['frbox_values'] = []
    #this year
    now = datetime.datetime.now()
    past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    end_of_year = datetime.datetime(now.year, 12, 31)
    days_remaining = LOM.day - now.day
    #runs_per_week = 3

    ytd_dict = master_dict.copy()
    for key in list(ytd_dict):
        if key < get_time.FOY():
            del ytd_dict[key]
    ytd_miles = []
    for run in ytd_dict:
        ytd_miles.append(float(ytd_dict[run]['distance_miles']))
    miles_this_year = sum(ytd_miles)

    #last year
    timestamp = datetime.datetime.now()
    past_ytd_dict = master_dict.copy()
    for key in list(past_ytd_dict):
        if key < get_time.PFOY():
            del past_ytd_dict[key]
        if key > datetime.datetime(timestamp.year - 1, timestamp.month, timestamp.day): #get date this time last year
            del past_ytd_dict[key]
    pytd_miles = []
    for run in past_ytd_dict:
        pytd_miles.append(float(past_ytd_dict[run]['distance_miles']))
    miles_last_year_this_time = sum(pytd_miles)

    goal_2018 = 600
    MPD = goal_2018/365 #miels per day starting 1/1
    day_of_year = now.timetuple().tm_yday #numerical value of day in the year
    #day_of_year = LOM.timetuple().tm_yday #found the day of the last of month for some reason, changed to above
    target_miles = MPD*day_of_year #what my current target_miles should be - NOT year long goal
    remaining_ytd_miles = miles_this_year - target_miles #why is this named like this?
    days_remaining_in_year = (end_of_year - now).days
    print("Days remaining in year: "+str(days_remaining_in_year))

    #new 3.6.18
    goal_miles_left_in_year = goal_2018 - miles_this_year #reverse of remaining_ytd_miles for some reason
    goal_miles_per_day_now = goal_miles_left_in_year/days_remaining_in_year
    goal_miles_per_week_now = goal_miles_per_day_now*7
    goal_miles_per_run_now = goal_miles_per_week_now/runs_per_week

    main_dict['title'] = "YEAR"

    main_dict['flbox_titles'].append("YTD Miles")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("Last YTD by now")
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")

    main_dict['flbox_values'].append(format_text(miles_this_year))
    main_dict['flbox_values'].append("")
    main_dict['flbox_values'].append(format_text(miles_last_year_this_time))
    main_dict['flbox_values'].append(format_text(miles_this_year-miles_last_year_this_time))
    main_dict['flbox_values'].append("")
    main_dict['flbox_values'].append("")
    main_dict['flbox_values'].append("")

    main_dict['frbox_titles'].append("18 Goal by today")
    main_dict['frbox_titles'].append("Difference")
    main_dict['frbox_titles'].append("Miles Per Day")
    main_dict['frbox_titles'].append("Miles Per Week")
    main_dict['frbox_titles'].append("Miles Per Run")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")

    main_dict['frbox_values'].append(format_text(target_miles))
    main_dict['frbox_values'].append(format_text(remaining_ytd_miles))
    main_dict['frbox_values'].append(format_text(goal_miles_per_day_now))
    main_dict['frbox_values'].append(format_text(goal_miles_per_week_now))
    main_dict['frbox_values'].append(format_text(goal_miles_per_run_now))
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append("")

    return main_dict
