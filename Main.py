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
    vis['ptitle_h'] = 20
    vis['ptitle_w'] = vis['psub_w']
    vis['ptitle_x'] = 0
    vis['ptitle_y'] = 40

    #subtitles 10 percent
    vis['psubtitle_title_h'] = 20
    vis['psubtitle_title_w'] = vis['psub_w']/2
    vis['psubtitle_title_x'] = 0
    vis['psubtitle_title_y'] = 60

    vis['psubtitle_value_h'] = 20
    vis['psubtitle_value_w'] = vis['psub_w']/2
    vis['psubtitle_value_x'] = vis['psub_w']/2
    vis['psubtitle_value_y'] = 60

    #box titles
    vis['box_titles_h'] = 32
    vis['box_titles_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_titles_x'] = 1 #this is later changed dynamically
    vis['box_titles_y'] = 80

    vis['box_values_h'] = 80
    vis['box_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_values_x'] = 1 #this is later changed dynamically
    vis['box_values_y'] = 110

    #Bottom Labels
    vis['ptotal_title_h'] = 32
    vis['ptotal_title_w'] = vis['psub_w']/5
    vis['ptotal_title_x'] = 0
    vis['ptotal_title_y'] = 190

    vis['ptotal_values_h'] = 32
    vis['ptotal_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['ptotal_values_x'] = 1 #this is later changed dynamically
    vis['ptotal_values_y'] = 190

    ########################################################CSUB########################################################

    return vis

vis = vis(w,h)


box_titles = ['Date','Distance','Pace','Duration','Elevation']
box_values = ['Sun Apr 29','3.34','9:14','0:34:14','155.55']

#SUBVIEWS
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'blue')
fsubview = ui.View(frame=(vis['fsub_x'], vis['fsub_y'], vis['fsub_w'], vis['fsub_h']), background_color = 'red')
view.add_subview(psubview)
view.add_subview(csubview)
view.add_subview(fsubview)

#seg control
pseg_control = ui.SegmentedControl(name= 'pseg_control', frame = (vis['pseg_control_x'], vis['pseg_control_y'],vis['pseg_control_w'],vis['pseg_control_h']))
pseg_control.segments = ("Week 1","Week 2","Week 3")
#SegmentedControl.action
#SegmentedControl.selected_index
psubview.add_subview(pseg_control)

#title
ptitle = ui.Label(name = 'ptitle', bg_color ='yellow', frame = (vis['ptitle_x'], vis['ptitle_y'], vis['ptitle_w'], vis['ptitle_h']))
ptitle.text = "ptitle"
ptitle.alignment = 1 #1 is center
psubview.add_subview(ptitle)

#subtitles
psubtitle_title = ui.Label(name = 'psubtitle_title', bg_color ='gray', frame = (vis['psubtitle_title_x'], vis['psubtitle_title_y'], vis['psubtitle_title_w'], vis['psubtitle_title_h']))
psubtitle_title.text = "subtitle title"
psubtitle_title.alignment = 1 #1 is center
psubview.add_subview(psubtitle_title)

psubtitle_value = ui.Label(name = 'psubtitle_value', bg_color ='pink', frame = (vis['psubtitle_value_x'], vis['psubtitle_value_y'], vis['psubtitle_value_w'], vis['psubtitle_value_h']))
psubtitle_value.text = "subtitle value"
psubtitle_value.alignment = 1 #1 is center
psubview.add_subview(psubtitle_value)

#box titles
for n,label in enumerate(box_titles):
    count = len(box_titles)
    vis['box_titles_w'] = vis['psub_w']/count #divide width by number of labels
    vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
    label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',14)
    label_title.border_color = 'black'
    label_title.border_width = 1
    psubview.add_subview(label_title)

for n,label in enumerate(box_values):
    count = len(box_values)
    vis['box_values_w'] = vis['psub_w']/count #divide width by number of labels
    vis['box_values_x'] = vis['box_values_w'] * n #first label at 0, second label at width*1
    label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',10)
    label_title.border_color = 'black'
    label_title.border_width = 1
    psubview.add_subview(label_title)

#total title/labels
ptotal_title = ui.Label(name = 'ptotal_title', bg_color ='pink', frame = (vis['ptotal_title_x'], vis['ptotal_title_y'], vis['ptotal_title_w'], vis['ptotal_title_h']))
ptotal_title.text = "ptotals"
ptotal_title.alignment = 1 #1 is center
psubview.add_subview(ptotal_title)

######
view.present(style='sheet', hide_title_bar=True)
