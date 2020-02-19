import get_data
import calc


my_dict = get_data.my_filtered_activities() #get master dictionary
weekly_dict = calc.weekly_stats(my_dict) #use weekly_stats to calculate weekly dictionary (monday first)

this_week = sorted(weekly_dict.keys())[-1] #find key for latest week



output= str(weekly_dict[this_week]['run_count'])+": "+str(weekly_dict[this_week]['miles_ran'])

print(output,  file=open('/var/www/html/test/result.txt', 'w'))
