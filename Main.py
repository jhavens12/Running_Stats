#import get_data
import ui
from pprint import pprint
import datetime


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

def vis(w,h):
    vis = {}
    vis['x_margin'] = 15
    vis['y_margin'] = 20

    #SUBVIEWS
    vis['psub_h'] = h*.33
    vis['psub_w'] = w - (vis['x_margin']*2) #sets width for all subviews
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin']

    vis['csub_h'] = h*.33
    vis['csub_w'] = vis['psub_w']
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['y_margin'] + vis['psub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    vis['fsub_h'] = h*.26
    vis['fsub_w'] = vis['psub_w']
    vis['fsub_x'] = vis['x_margin']
    vis['fsub_y'] = vis['csub_y'] + vis['csub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    ########################################################PSUB########################################################
    #SEGMENTED CONTROL
    vis['pseg_control_h'] = 30
    vis['pseg_control_w'] = vis['psub_w'] - 10
    vis['pseg_control_x'] = 5
    vis['pseg_control_y'] = 5

    #LABELS
    vis['psub_title_h'] = 20
    vis['psub_title_w'] = vis['psub_w']
    vis['psub_title_x'] = 0
    vis['psub_title_y'] = 40

    vis['box_titles_h'] = 32
    vis['box_titles_w'] = vis['psub_w']
    vis['box_titles_x'] = 1 #filler
    vis['box_titles_y'] = 60

    # BOX TITLES
    vis['psub_date_h'] = 20
    vis['psub_date_w'] = vis['psub_w']
    vis['psub_date_x'] = 0
    vis['psub_date_y'] = 40

    vis['psub_distance_h'] = 20
    vis['psub_distance_w'] = vis['psub_w']
    vis['psub_distance_x'] = 0
    vis['psub_distance_y'] = 40

    vis['psub_pace_h'] = 20
    vis['psub_pace_w'] = vis['psub_w']
    vis['psub_pace_x'] = 0
    vis['psub_pace_y'] = 40

    vis['psub_duration_h'] = 20
    vis['psub_duration_w'] = vis['psub_w']
    vis['psub_duration_x'] = 0
    vis['psub_duration_y'] = 40

    vis['psub_elevation_h'] = 20
    vis['psub_elevation_w'] = vis['psub_w']
    vis['psub_elevation_x'] = 0
    vis['psub_elevation_y'] = 40

    vis['psub_total_h'] = 20
    vis['psub_total_w'] = vis['psub_w']
    vis['psub_total_x'] = 0
    vis['psub_total_y'] = 40



    ########################################################CSUB########################################################
#date
#distance
#pace
#duration
#elevation
#total/avg
#10percent


    return vis

vis = vis(w,h)


box_titles = ['Date','Distance','Pace','Duration','Elevation']

#SUBVIEWS
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'blue')
fsubview = ui.View(frame=(vis['fsub_x'], vis['fsub_y'], vis['fsub_w'], vis['fsub_h']), background_color = 'red')
view.add_subview(psubview)
view.add_subview(csubview)
view.add_subview(fsubview)

#PSUB FILLER
pseg_control = ui.SegmentedControl(name= 'pseg_control', frame = (vis['pseg_control_x'], vis['pseg_control_y'],vis['pseg_control_w'],vis['pseg_control_h']))
pseg_control.segments = ("Week 1","Week 2","Week 3")
#SegmentedControl.action
#SegmentedControl.selected_index

ptitle = ui.Label(name = 'ptitle', bg_color ='yellow', frame = (vis['psub_title_x'], vis['psub_title_y'], vis['psub_title_w'], vis['psub_title_h']))
ptitle.text = "ptitle"
ptitle.alignment = 1 #1 is center

for n,label in enumerate(box_titles):

    count = len(box_titles)
    vis['box_titles_w'] = vis['psub_w']/count #divide width by number of labels
    vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
    n = n+1
    label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',10)
    label_title.border_color = 'black'
    label_title.border_width = 1
    psubview.add_subview(label_title)

psubview.add_subview(ptitle)
psubview.add_subview(pseg_control)


######
view.present(style='sheet', hide_title_bar=True)
