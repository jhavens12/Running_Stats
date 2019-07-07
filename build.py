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
import numpy as np #new


runs_per_week = 4
goal_mileage = 650

master_dict = get_data.my_filtered_activities()

def format_text(x):
    return str("{0:.2f}".format(x))

def top_period(runs_per_week,current_info):

    weekly_dict = calc.weekly_stats(master_dict.copy())

    max_weekly_miles = 0
    for week in weekly_dict:
        if weekly_dict[week]['miles_ran'] > max_weekly_miles:
            max_weekly_miles = float(weekly_dict[week]['miles_ran'])
            most_miles_week = week

    dict_1 = weekly_dict[most_miles_week]['run_dict'] #grab dictionary of runs from top week to display

    #below is taken from the period function
    ########################################

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
    current_elevation_total = "{0:.2f}".format(sum(current_elevation_list))

    main_dict = {} #main dictionary to add values to and then return
    main_dict['title'] = str(most_miles_week)#(get_time.convert_weekday_full(get_time.LM(Monday)) + " - " + get_time.convert_weekday_full(get_time.LS(Sunday)))

    main_dict['subtitle_title'] = 'Ten Percent:'
    main_dict['subtitle_value'] = str(past_ten_percent)

    main_dict['subtitle2_title'] = ''
    main_dict['subtitle2_value'] = ''

    main_dict['box_titles'] = ['Date','Distance','Duration','Pace','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(past_run_title_label))
    main_dict['box_values'].append("\n".join(past_run_mile_label))
    main_dict['box_values'].append("\n".join(past_run_elapsed_label))
    main_dict['box_values'].append("\n".join(past_run_pace_label))
    main_dict['box_values'].append("\n".join(past_run_treadmill_label))

    #BOTTOM VALUES
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []
    main_dict['total_values'].append(str(past_miles))
    main_dict['total_values'].append(str(current_duration_total))
    main_dict['total_values'].append(str(current_pace_average))
    main_dict['total_values'].append(current_elevation_total)

    #calculate remaining
    current_miles = current_info['current_miles']
    current_week_count = current_info['current_week_count']

    remaining_miles = str("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles)))
    main_dict['remaining_miles'] = remaining_miles
    main_dict['remaining_miles_match'] = str("{0:.2f}".format(float(past_miles) - float(current_miles)))
    if float(runs_per_week)-float(current_week_count) != 0:
        miles_per_run_remaining = float(remaining_miles)/(runs_per_week-float(current_week_count))
        main_dict['remaining_per_run'] = format_text(miles_per_run_remaining)
    else:
        main_dict['remaining_per_run'] = "0"

    remaining_miles_down = str("{0:.2f}".format(float(past_miles) - float(current_miles) - float(past_ten_percent))) #this uses past rolling 4 weeks
    main_dict['remaining_miles_down'] = remaining_miles_down

    return main_dict

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


    #calculate rolling 10 percent over the past 4 weeks
    def rolling_ten_percent(Sunday,Monday):
        def period_ten_percent(sun,mon):
            dict_1 = master_dict.copy()
            for key in master_dict:
                if key > get_time.LS(sun):
                    del dict_1[key]
            for key in master_dict:
                if key < get_time.LM(mon):
                    del dict_1[key]
            past_dict_rev = {k: dict_1[k] for k in list(reversed(sorted(dict_1.keys())))}
            past_dict = {k: past_dict_rev[k] for k in list(sorted(past_dict_rev.keys()))}
            past_run_count = calc.activity_count(past_dict)
            past_mile_list = []
            for i in past_dict:
                past_mile_list.append(float(past_dict[i]['distance_miles']))
            past_miles = ("{0:.2f}".format(sum(past_mile_list)))
            past_ten_percent = float(("{0:.2f}".format(float(past_miles) * .1)))

            return past_ten_percent
        past_list = []
        past_list.append(period_ten_percent(Sunday,Monday))
        past_list.append(period_ten_percent(Sunday+1,Monday+1))
        past_list.append(period_ten_percent(Sunday+2,Monday+2))
        past_list.append(period_ten_percent(Sunday+3,Monday+3))

        past_four = sum(past_list)
        past_avg = past_four/4
        return past_avg

    past_avg = rolling_ten_percent(Sunday,Monday)

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
    current_elevation_total = "{0:.2f}".format(sum(current_elevation_list))


    #####
    main_dict['title'] = (get_time.convert_weekday_full(get_time.LM(Monday)) + " - " + get_time.convert_weekday_full(get_time.LS(Sunday)))

    main_dict['subtitle_title'] = 'Ten Percent:'
    main_dict['subtitle_value'] = str(past_ten_percent)

    main_dict['subtitle2_title'] = '4 Weeks Roll:'
    main_dict['subtitle2_value'] = format_text(past_avg)

    main_dict['box_titles'] = ['Date','Distance','Duration','Pace','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(past_run_title_label))
    main_dict['box_values'].append("\n".join(past_run_mile_label))
    main_dict['box_values'].append("\n".join(past_run_elapsed_label))
    main_dict['box_values'].append("\n".join(past_run_pace_label))
    main_dict['box_values'].append("\n".join(past_run_treadmill_label))

    #BOTTOM VALUES
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []
    main_dict['total_values'].append(str(past_miles))
    main_dict['total_values'].append(str(current_duration_total))
    main_dict['total_values'].append(str(current_pace_average))
    main_dict['total_values'].append(current_elevation_total)

    #calculate remaining
    current_miles = current_info['current_miles']
    current_week_count = current_info['current_week_count']


    #THIS IS WHERE CSUBVIEW SUBTITLES HAPPEN
    #remaining_miles = str("{0:.2f}".format((float(past_ten_percent) + float(past_miles)) - float(current_miles))) #this uses just 1 week
    remaining_miles = str("{0:.2f}".format((float(past_avg) + float(past_miles)) - float(current_miles))) #this uses past rolling 4 weeks
    main_dict['remaining_miles'] = remaining_miles
    main_dict['remaining_miles_match'] = str("{0:.2f}".format(float(past_miles) - float(current_miles)))
    if float(runs_per_week)-float(current_week_count) != 0:
        miles_per_run_remaining = float(remaining_miles)/(runs_per_week-float(current_week_count))
        main_dict['remaining_per_run'] = format_text(miles_per_run_remaining)
    else:
        main_dict['remaining_per_run'] = "0"
    remaining_miles_down = str("{0:.2f}".format(float(past_miles) - float(current_miles) - float(past_avg))) #this uses past rolling 4 weeks
    main_dict['remaining_miles_down'] = remaining_miles_down

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
    current_elevation_total = "{0:.2f}".format(sum(current_elevation_list))

    #main_dict['title'] = (get_time.weekday(get_time.LM(0)) + " " + str(get_time.LM(0).day) + " - " + get_time.weekday(get_time.now()) + " " + str(get_time.now().day))
    main_dict['title'] = (get_time.convert_weekday_full(get_time.LM(0)) + " - " + get_time.convert_weekday_full(datetime.datetime.now()))
    #main_dict['subtitle1_title'] = "Remaining:"
    main_dict['subtitle1_title'] = "UP:"
    main_dict['subtitle2_title'] = "Match:"
    main_dict['subtitle3_title'] = "DOWN:"
    #main_dict['subtitle2_title'] = "Per Run:"
    main_dict['subtitle1_value'] = "0"
    main_dict['subtitle2_value'] = "0"
    main_dict['subtitle3_value'] = "0"


    main_dict['box_titles'] = ['Date','Distance','Duration','Pace','Elevation']
    main_dict['box_values'] = []
    main_dict['box_values'].append("\n".join(current_run_title_label))
    main_dict['box_values'].append("\n".join(current_run_mile_label))
    main_dict['box_values'].append("\n".join(current_run_elapsed_label))
    main_dict['box_values'].append("\n".join(current_run_pace_label))
    main_dict['box_values'].append("\n".join(current_run_treadmill_label))

    #totals at bottom
    main_dict['total_title'] = 'Total/AVG'
    main_dict['total_values'] = []
    main_dict['total_values'].append(str(current_miles))
    main_dict['total_values'].append(str(current_duration_total))
    main_dict['total_values'].append(str(current_pace_average))
    main_dict['total_values'].append(current_elevation_total)

    return main_dict

def weekly(current_info):

    def how_most_running_period(days): #Used for "Days" as running consecutive days
        output_dict = {}
        input_day = days
        result_dict = calc.full_running_totals(master_dict.copy(),input_day,'distance_miles')
        current_total_date = sorted(result_dict.keys())[-1]
        current_total = result_dict[current_total_date]
        highest_total = 0
        for run in result_dict:
            if result_dict[run] > highest_total:
                highest_total = result_dict[run]
                highest_total_date = run
        #result_dict has date as key, 7 day total as value
        output_dict['highest_total'] = highest_total
        output_dict['highest_total_date'] = highest_total_date
        output_dict['current_total'] = current_total
        output_dict['current_total_date'] = current_total_date
        output_dict['difference_distance'] = output_dict['current_total'] - output_dict['highest_total']
        output_dict['difference_time'] =  output_dict['current_total_date'] - output_dict['highest_total_date']

        return output_dict

    run_period_7 = how_most_running_period(7)
    run_period_30 = how_most_running_period(30)

    current_miles = current_info['current_miles']
    current_week_count = current_info['current_week_count']

    #taken from top peroid
    weekly_dict = calc.weekly_stats(master_dict.copy())

    max_weekly_miles = 0
    for week in weekly_dict:
        if weekly_dict[week]['miles_ran'] > max_weekly_miles:
            max_weekly_miles = float(weekly_dict[week]['miles_ran'])
            most_miles_week = week

    print(weekly_dict[most_miles_week]['datetime'])
    dict_1 = weekly_dict[most_miles_week]['run_dict'] #grab dictionary of runs from top week to display

    main_dict = {}
    main_dict['flbox_titles'] = []
    main_dict['flbox_values'] = []
    main_dict['frbox_titles'] = []
    main_dict['frbox_values'] = []

    main_dict['title'] = "WEEKLY"
    #LABELS
    main_dict['flbox_titles'].append("This Week")
    main_dict['flbox_titles'].append("Best Week")
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("---------------") #15
    main_dict['flbox_titles'].append("7 Day")
    main_dict['flbox_titles'].append("Best 7 Day")
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("Days Since")

    #DATA
    main_dict['flbox_values'].append(str(current_miles))
    main_dict['flbox_values'].append(format_text(max_weekly_miles))
    main_dict['flbox_values'].append(format_text(float(max_weekly_miles)-float(current_miles)))
    main_dict['flbox_values'].append("------") #6
    main_dict['flbox_values'].append(format_text(run_period_7['current_total']))
    main_dict['flbox_values'].append(format_text(run_period_7['highest_total']))
    main_dict['flbox_values'].append(format_text(run_period_7['difference_distance']))
    main_dict['flbox_values'].append(str(run_period_7['difference_time'].days))

    # #
    main_dict['frbox_titles'].append("30 Day")
    main_dict['frbox_titles'].append("Best 30 Day")
    main_dict['frbox_titles'].append("Difference")
    main_dict['frbox_titles'].append("Days Since")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")

    #
    main_dict['frbox_values'].append(format_text(run_period_30['current_total']))
    main_dict['frbox_values'].append(format_text(run_period_30['highest_total']))
    main_dict['frbox_values'].append(format_text(run_period_30['difference_distance']))
    main_dict['frbox_values'].append(str(run_period_30['difference_time'].days))
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append("")
    main_dict['frbox_values'].append("")
    # main_dict['frbox_values'].append(format_text(run_period_90['current_total']))
    # main_dict['frbox_values'].append(format_text(run_period_90['highest_total']))
    # main_dict['frbox_values'].append(format_text(run_period_90['difference_distance']))
    # main_dict['frbox_values'].append(str(run_period_90['difference_time'].days))

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
    if now.month == 12:
      past = datetime.datetime(now.year,12,31)
    else:
      past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
    LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)
    days_remaining = LOM.day - now.day
    #runs_per_week = 3
    runs_remain = math.ceil(days_remaining*(runs_per_week/7))
    if runs_remain == 0:
      runs_remain = 1
    monthly_dict = calc.monthly_stats(master_dict.copy())
    max_miles = 0
    for month in monthly_dict:
        if monthly_dict[month]['miles_ran'] > max_miles:
            max_miles = int(monthly_dict[month]['miles_ran'])
            most_miles_month = month


    main_dict['title'] = get_time.convert_month_name(datetime.datetime.now()) #get name of this month
    #LABELS
    #14 values per side
    main_dict['flbox_titles'].append("This Month")
    main_dict['flbox_titles'].append("Run Count")
    main_dict['flbox_titles'].append("---------------") #15
    main_dict['flbox_titles'].append("Last Month")
    main_dict['flbox_titles'].append("Run Count")
    main_dict['flbox_titles'].append("---------------") #15
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("Runs Remain")
    main_dict['flbox_titles'].append("MPR Last Month")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")
    main_dict['flbox_titles'].append("")


    #DATA
    main_dict['flbox_values'].append(format_text(this_month))
    main_dict['flbox_values'].append(format_text(len(this_month_full)))
    main_dict['flbox_values'].append("------") #6
    main_dict['flbox_values'].append(format_text(last_month))
    main_dict['flbox_values'].append(format_text(len(last_month_full)))
    main_dict['flbox_values'].append("------") #6
    main_dict['flbox_values'].append(format_text(month_difference))
    main_dict['flbox_values'].append(format_text(runs_remain))
    main_dict['flbox_values'].append(format_text(abs(month_difference/runs_remain)))
    #fix above line - divison by 0
    main_dict['flbox_values'].append("")

    # #
    main_dict['frbox_titles'].append("50 Miles Goal")
    main_dict['frbox_titles'].append("MPR to 50M")
    main_dict['frbox_titles'].append("---------------") #15
    main_dict['frbox_titles'].append("Month Record")
    main_dict['frbox_titles'].append("MPR to Record")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")
    main_dict['frbox_titles'].append("")

    #
    main_dict['frbox_values'].append(format_text(this_month-50))
    main_dict['frbox_values'].append(format_text((50-this_month)/runs_remain))
    main_dict['frbox_values'].append("------") #6
    main_dict['frbox_values'].append(str(max_miles))
    main_dict['frbox_values'].append(format_text((max_miles-this_month)/runs_remain))
    main_dict['frbox_values'].append("")
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
    if now.month == 12:
      past = datetime.datetime(now.year,12,31)
    else:
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

    MPD = goal_mileage/365 #miels per day starting 1/1
    day_of_year = now.timetuple().tm_yday #numerical value of day in the year
    #day_of_year = LOM.timetuple().tm_yday #found the day of the last of month for some reason, changed to above
    target_miles = MPD*day_of_year #what my current target_miles should be - NOT year long goal
    remaining_ytd_miles = miles_this_year - target_miles #why is this named like this?
    days_remaining_in_year = (end_of_year - now).days


    #new 3.6.18
    goal_miles_left_in_year = goal_mileage - miles_this_year #reverse of remaining_ytd_miles for some reason
    goal_miles_per_day_now = goal_miles_left_in_year/days_remaining_in_year
    goal_miles_per_week_now = goal_miles_per_day_now*7
    goal_miles_per_run_now = goal_miles_per_week_now/runs_per_week

    #new 5.16.18 - Goal predictions
    def goal_hit_date(filter_day):
        yearly_dict = calc.yearly_totals(master_dict.copy(),0) #current year
        x_list = []
        y_list = []
        for event in yearly_dict:
            if event > filter_day:
                x_list.append(event)
                y_list.append(yearly_dict[event])

        def extended_prediction(x_list,y_list,end_day):
            if not y_list:
                y_list = [0]
            if not x_list:
                x_list = [0]
            extended_range = list(range(x_list[0],end_day))
            model = np.polyfit(x_list, y_list, 1)
            predicted = np.polyval(model, extended_range)
            return extended_range, predicted

        extended_range_30, predicted_30 = extended_prediction(x_list, y_list, 720)
        the_list = []
        for x,y in zip(extended_range_30,predicted_30):
            if y > goal_mileage:
                the_list.append(x)
        if not the_list:
            goal_day = 365 #changed from 0 as it showed last year when it could not predict
        else:
            goal_day = the_list[0]
        timestamp = datetime.datetime.now()
        goal_day_nice = datetime.datetime(timestamp.year, 1, 1) + datetime.timedelta(goal_day - 1)
        return str(goal_day_nice.month)+"."+str(goal_day_nice.day)+"."+str(goal_day_nice.year)[-2:]

    todays_number = datetime.datetime.now().timetuple().tm_yday #finds number of year
    days_ago_30 = todays_number - 30 #number to filter entires out from since not datetime objects
    days_ago_90 = todays_number - 90

    goal_30 = goal_hit_date(days_ago_30) #30 days ago
    goal_90 = goal_hit_date(days_ago_90)
    goal_year = goal_hit_date(0) #0 is beginning of year

    ###

    main_dict['title'] = get_time.convert_year_name(datetime.datetime.now())

    main_dict['flbox_titles'].append("YTD Miles")
    main_dict['flbox_titles'].append("Last YTD by now")
    main_dict['flbox_titles'].append("Difference")
    main_dict['flbox_titles'].append("---------------") #15
    main_dict['flbox_titles'].append("Days Remain")
    main_dict['flbox_titles'].append("Goal (30)")
    main_dict['flbox_titles'].append("Goal (90)")
    main_dict['flbox_titles'].append("Goal (Year)")

    main_dict['flbox_values'].append(format_text(miles_this_year))
    main_dict['flbox_values'].append(format_text(miles_last_year_this_time))
    main_dict['flbox_values'].append(format_text(miles_this_year-miles_last_year_this_time))
    main_dict['flbox_values'].append("------") #6
    main_dict['flbox_values'].append(str(days_remaining_in_year))
    main_dict['flbox_values'].append(goal_30)
    main_dict['flbox_values'].append(goal_90)
    main_dict['flbox_values'].append(goal_year)

    main_dict['frbox_titles'].append("Yearly Goal")
    main_dict['frbox_titles'].append("Difference")
    main_dict['frbox_titles'].append("---------------") #15
    main_dict['frbox_titles'].append("Miles Per Day")
    main_dict['frbox_titles'].append("Miles Per Week")
    main_dict['frbox_titles'].append("Miles Per Run")



    main_dict['frbox_values'].append(format_text(target_miles))
    main_dict['frbox_values'].append(format_text(remaining_ytd_miles))
    main_dict['frbox_values'].append("------") #6
    main_dict['frbox_values'].append(format_text(goal_miles_per_day_now))
    main_dict['frbox_values'].append(format_text(goal_miles_per_week_now))
    main_dict['frbox_values'].append(format_text(goal_miles_per_run_now))



    return main_dict

def yearly_graph():
    #modified from running_graphs to show YTD mileage
    yearly_dict = calc.yearly_totals(master_dict.copy(),0) #current year
    #print(yearly_dict)
    yearly_dict2 = calc.yearly_totals(master_dict.copy(),1) #last year
    yearly_dict3 = calc.yearly_totals(master_dict.copy(),2) #last year

    def graph(formula):
        x = np.array(range(0,366))
        y = eval(formula)
        plt.plot(x, y, 'w', linestyle=':', linewidth=4,label=goal_mileage)

    label1=int(datetime.datetime.now().year)
    label2=label1-1
    label3=label1-2

    graph('x*('+str(goal_mileage)+'/365)')
    plt.plot(list(yearly_dict3.keys()),list(yearly_dict3.values()), 'green', linewidth=4,label=label3)
    plt.plot(list(yearly_dict2.keys()),list(yearly_dict2.values()), 'blue', linewidth=4,label=label2)
    plt.plot(list(yearly_dict.keys()),list(yearly_dict.values()), 'red', linewidth=4, label=label1)

    plt.style.use('dark_background')
    plt.axis('off')
    plt.legend(loc=0,fontsize=20)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1,
                wspace=None, hspace=None)

    b = BytesIO()
    plt.savefig(b, transparent='True')
    plt.close('all')
    return b

def yearly_prediction_graph(): #This is currently used
    #modified from running_graphs to show YTD mileage

    def graph(formula):
        x = np.array(range(0,366))
        y = eval(formula)
        plt.plot(x, y, 'w', linestyle=':', linewidth=4)

    yearly_dict = calc.yearly_totals(master_dict.copy(),0) #current year
    yearly_dict2 = calc.yearly_totals(master_dict.copy(),1) #last year

    x_list = []
    y_list = []
    x2_list = []
    y2_list = []

    todays_number = datetime.datetime.now().timetuple().tm_yday #finds number of year
    month_ago_number = todays_number - 30 #number to filter entires out from since not datetime objects

    for event in yearly_dict:
        x_list.append(event)
        y_list.append(yearly_dict[event])
        if event > month_ago_number:
            x2_list.append(event)
            y2_list.append(yearly_dict[event])

    def extended_prediction(x_list,y_list,end_day):
        if not y_list:
            y_list = [0]
        if not x_list:
            x_list = [0]
        extended_range = list(range(x_list[0],end_day))
        model = np.polyfit(x_list, y_list, 1)
        predicted = np.polyval(model, extended_range)
        return extended_range, predicted

    extended_range, predicted = extended_prediction(x_list, y_list, 365)
    extended_range_30, predicted_30 = extended_prediction(x2_list, y2_list, 365)

    graph('x*('+str(goal_mileage)+'/365)')
    plt.plot(extended_range, predicted, linestyle='--',color='orange',linewidth=4,label='All Year')
    plt.plot(extended_range_30, predicted_30, linestyle='--',color='red',linewidth=4,label='30 Days')
    plt.plot(list(yearly_dict.keys()),list(yearly_dict.values()),label=('This Year'),color='blue',lw='4')

    plt.style.use('dark_background')
    plt.axis('off')
    plt.legend(loc=0,fontsize=30)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1,
                wspace=None, hspace=None)
    b = BytesIO()
    plt.savefig(b, transparent='True')
    plt.close('all')
    return b

def weekly_graph():

    now = datetime.datetime.now()
    diff = now - datetime.datetime(now.year, 1, 1)
    weeks_back = int(diff.days/7)
    weeks_to_calculate = list(range(0,weeks_back)) #calculate 0 to 17

    week_dict = {}
    for week in weeks_to_calculate:
        week_dict[week] = master_dict.copy() #make a master dict for each week to calculate

    for week in week_dict:
        for key in list(week_dict[week]): #for each key in each master dictionary
            if key < get_time.LM(week): #if older than last monday (0 is 1, 1 is 2,2 mondays ago)
                del week_dict[week][key]
        for key in list(week_dict[week]):
           if key > get_time.LS(week-1): #if newer than last sunday (0 is 1)
               del week_dict[week][key]

    miles_dict = {}
    for week in week_dict:
        if week_dict[week]: #check to see if any activites exist in the given week
            mile_list = []
            for activity in week_dict[week]:
                mile_list.append(float(week_dict[week][activity]['distance_miles']))
            miles_dict[get_time.LM(week)] = sum(mile_list)
        else:
            miles_dict[get_time.LM(week)] = 0

    x_list = []
    y_list = []
    for month in miles_dict:
        x_list.append(month)
        y_list.append(miles_dict[month])

    #######
    myFmt = mdates.DateFormatter('%m/%d')
    plt.bar(x_list, y_list, align='center', width=6)

    plt.style.use('dark_background')
    #plt.axis('off')
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1,
                wspace=None, hspace=None)

    b = BytesIO()
    plt.savefig(b, transparent='True')
    plt.close('all')
    return b
