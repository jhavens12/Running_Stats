#import get_data
import ui
from pprint import pprint
import datetime

#fix bottom line of pview - doesn't like up with end of labels


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

def vis(w,h):
    vis = {}
    vis['x_margin'] = 15
    vis['y_margin'] = 20

    #SUBVIEWS
    vis['psub_h'] = (h*.33) - 20
    vis['psub_w'] = w - (vis['x_margin']*2) #sets width for all subviews
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin'] + 30

    vis['csub_h'] = h*.33
    vis['csub_w'] = vis['psub_w']
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['psub_y'] + vis['psub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    vis['fsub_h'] = h*.26
    vis['fsub_w'] = vis['psub_w']
    vis['fsub_x'] = vis['x_margin']
    vis['fsub_y'] = vis['csub_y'] + vis['csub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    ########################################################PSUB########################################################
    #SEGMENTED CONTROL
    vis['pseg_control_h'] = 30
    vis['pseg_control_w'] = vis['psub_w']
    vis['pseg_control_x'] = vis['x_margin']
    vis['pseg_control_y'] = vis['y_margin']

    #LABELS
    vis['ptitle_h'] = 20
    vis['ptitle_w'] = vis['psub_w']
    vis['ptitle_x'] = 0
    vis['ptitle_y'] = 0

    #subtitles 10 percent
    vis['psubtitle_title_h'] = 20
    vis['psubtitle_title_w'] = vis['psub_w']/2
    vis['psubtitle_title_x'] = 0
    vis['psubtitle_title_y'] = 20

    vis['psubtitle_value_h'] = 20
    vis['psubtitle_value_w'] = vis['psub_w']/2
    vis['psubtitle_value_x'] = vis['psub_w']/2
    vis['psubtitle_value_y'] = 20

    #box titles
    vis['box_titles_h'] = 32
    vis['box_titles_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_titles_x'] = 1 #this is later changed dynamically
    vis['box_titles_y'] = 40

    vis['box_values_h'] = 80
    vis['box_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_values_x'] = 1 #this is later changed dynamically
    vis['box_values_y'] = 70

    #Bottom Labels
    vis['ptotal_title_h'] = 32
    vis['ptotal_title_w'] = vis['psub_w']/5
    vis['ptotal_title_x'] = 0
    vis['ptotal_title_y'] = 150

    vis['ptotal_values_h'] = 32
    vis['ptotal_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['ptotal_values_x'] = 1 #this is later changed dynamically
    vis['ptotal_values_y'] = 150

    ########################################################cSUB########################################################

    #LABELS
    vis['ctitle_h'] = 20
    vis['ctitle_w'] = vis['psub_w']
    vis['ctitle_x'] = 0
    vis['ctitle_y'] = 0

    #subtitles 10 percent
    vis['csubtitle1_title_h'] = 20
    vis['csubtitle1_title_w'] = vis['psub_w']/4
    vis['csubtitle1_title_x'] = 0 #first
    vis['csubtitle1_title_y'] = 20

    vis['csubtitle1_value_h'] = 20
    vis['csubtitle1_value_w'] = vis['psub_w']/4
    vis['csubtitle1_value_x'] = vis['psub_w']/4 #second
    vis['csubtitle1_value_y'] = 20

    vis['csubtitle2_title_h'] = 20
    vis['csubtitle2_title_w'] = vis['psub_w']/4
    vis['csubtitle2_title_x'] = (vis['psub_w']/4) * 2 #third
    vis['csubtitle2_title_y'] = 20

    vis['csubtitle2_value_h'] = 20
    vis['csubtitle2_value_w'] = vis['psub_w']/4
    vis['csubtitle2_value_x'] = (vis['psub_w']/4) * 3 #fourth
    vis['csubtitle2_value_y'] = 20


    return vis

vis = vis(w,h)


box_titles = ['Date','Distance','Pace','Duration','Elevation']
box_values = ['Sun Apr 29','3.34','9:14','0:34:14','155.55']
total_values = ['13.02','8:49','0:21:00','1000.89']

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
view.add_subview(pseg_control)

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

for n,label in enumerate(total_values):
    n = n+1 #account for first box being the static label
    count = len(total_values)
    vis['ptotal_values_w'] = vis['psub_w']/(count+1) #divide width by number of labels
    vis['ptotal_values_x'] = vis['ptotal_values_w'] * n #first label at 0, second label at width*1
    label_title = ui.Label(name = label, bg_color = 'lightblue', frame = (vis['ptotal_values_x'], vis['ptotal_values_y'], vis['ptotal_values_w'], vis['ptotal_values_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',10)
    label_title.border_color = 'black'
    label_title.border_width = 1
    psubview.add_subview(label_title)

########################################################CSUB########################################################
########################################################CSUB########################################################
########################################################CSUB########################################################
########################################################CSUB########################################################
########################################################CSUB########################################################

#Title
ctitle = ui.Label(name = 'ctitle', bg_color ='yellow', frame = (vis['ctitle_x'], vis['ctitle_y'], vis['ctitle_w'], vis['ctitle_h']))
ctitle.text = "ctitle"
ctitle.alignment = 1 #1 is center
csubview.add_subview(ctitle)

#subtitles
csubtitle1_title = ui.Label(name = 'csubtitle1_title', bg_color ='gray', frame = (vis['csubtitle1_title_x'], vis['csubtitle1_title_y'], vis['csubtitle1_title_w'], vis['csubtitle1_title_h']))
csubtitle1_title.text = "sub1 t"
csubtitle1_title.alignment = 1 #1 is center
csubview.add_subview(csubtitle1_title)

csubtitle1_value = ui.Label(name = 'csubtitle1_value', bg_color ='pink', frame = (vis['csubtitle1_value_x'], vis['csubtitle1_value_y'], vis['csubtitle1_value_w'], vis['csubtitle1_value_h']))
csubtitle1_value.text = "sub1 v"
csubtitle1_value.alignment = 1 #1 is center
csubview.add_subview(csubtitle1_value)

csubtitle2_title = ui.Label(name = 'csubtitle2_title', bg_color ='gray', frame = (vis['csubtitle2_title_x'], vis['csubtitle2_title_y'], vis['csubtitle2_title_w'], vis['csubtitle2_title_h']))
csubtitle2_title.text = "sub2 t"
csubtitle2_title.alignment = 1 #1 is center
csubview.add_subview(csubtitle2_title)

csubtitle2_value = ui.Label(name = 'csubtitle2_value', bg_color ='pink', frame = (vis['csubtitle2_value_x'], vis['csubtitle2_value_y'], vis['csubtitle2_value_w'], vis['csubtitle2_value_h']))
csubtitle2_value.text = "sub2 v"
csubtitle2_value.alignment = 1 #1 is center
csubview.add_subview(csubtitle2_value)

#box titles
for n,label in enumerate(box_titles):
    count = len(box_titles)
    vis['box_titles_w'] = vis['csub_w']/count #divide width by number of labels
    vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
    label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',14)
    label_title.border_color = 'black'
    label_title.border_width = 1
    csubview.add_subview(label_title)

for n,label in enumerate(box_values):
    count = len(box_values)
    vis['box_values_w'] = vis['csub_w']/count #divide width by number of labels
    vis['box_values_x'] = vis['box_values_w'] * n #first label at 0, second label at width*1
    label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
    label_title.text = label
    label_title.alignment = 1
    label_title.font =  ('<system>',10)
    label_title.border_color = 'black'
    label_title.border_width = 1
    csubview.add_subview(label_title)

view.present(style='sheet', hide_title_bar=True)
