#import get_data
import ui
from pprint import pprint
import datetime
import build

w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

def vis(w,h):
    vis = {}
    vis['x_margin'] = 15
    vis['y_margin'] = 20

    #SUBVIEWS
    vis['psub_h'] = 182 #(h*.33) - 20
    vis['psub_w'] = w - (vis['x_margin']*2) #sets width for all subviews
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin'] + 30

    vis['csub_h'] = 182 #h*.33
    vis['csub_w'] = vis['psub_w']
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['psub_y'] + vis['psub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    vis['fsub_h'] = h*.29
    vis['fsub_w'] = vis['psub_w']
    vis['fsub_x'] = vis['x_margin']
    vis['fsub_y'] = vis['csub_y'] + vis['csub_h'] + (vis['y_margin']/2) +30 #y margin, height of psub, y margin #add segcontrol height

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
    vis['total_title_h'] = 32
    vis['total_title_w'] = vis['psub_w']/5
    vis['total_title_x'] = 0
    vis['total_title_y'] = 150

    vis['total_values_h'] = 32
    vis['total_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['total_values_x'] = 1 #this is later changed dynamically
    vis['total_values_y'] = 150

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

    ########################################################FSUB########################################################
    #SEGMENTED CONTROL
    vis['fseg_control_h'] = 30
    vis['fseg_control_w'] = vis['psub_w']
    vis['fseg_control_x'] = vis['x_margin']
    vis['fseg_control_y'] = (vis['y_margin']/2) + vis['csub_h'] + vis['csub_y'] #margin plus the view above position and height

    #LABELS
    vis['ftitle_h'] = 20
    vis['ftitle_w'] = vis['psub_w']
    vis['ftitle_x'] = 0
    vis['ftitle_y'] = 0

    #box titles LEFT
    vis['fbox_titles_h'] = (vis['fsub_h'] - vis['ftitle_h']) / 7
    vis['fbox_titles_w'] = (vis['psub_w']/2) * .75
    vis['fbox_titles_x'] = 0
    vis['fbox_titles_y'] = 1 #this needs to be changed

    vis['fbox_values_h'] = vis['fbox_titles_h']
    vis['fbox_values_w'] = (vis['psub_w']/2) * .25
    vis['fbox_values_x'] = vis['fbox_titles_w']
    vis['fbox_values_y'] = 1 #this needs to be changed

    #box titles RIGHT
    vis['frbox_titles_h'] = (vis['fsub_h'] - vis['ftitle_h']) / 7
    vis['frbox_titles_w'] = vis['psub_w']/4
    vis['frbox_titles_x'] = (vis['psub_w']/4) * 2
    vis['frbox_titles_y'] = 1 #this needs to be changed

    vis['frbox_values_h'] = vis['frbox_titles_h']
    vis['frbox_values_w'] = vis['psub_w']/4
    vis['frbox_values_x'] = (vis['psub_w']/4) * 3
    vis['frbox_values_y'] = 1 #this needs to be changed
    return vis

vis = vis(w,h)

#SUBVIEWS
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'blue')
fsubview = ui.View(frame=(vis['fsub_x'], vis['fsub_y'], vis['fsub_w'], vis['fsub_h']), background_color = 'red')

view.add_subview(psubview)
view.add_subview(csubview)
view.add_subview(fsubview)


def generate_segmented_controls(view):
    def pseg_select(sender):
        if sender.selected_index == 0:
            print("pseg week 1")
            pseg_info = build.period(0,1,current_info) #build pseg info, give current stats to find remaining_miles and MPR
            generate_psubview(psubview,csubview,pseg_info)
        if sender.selected_index == 1:
            print("pseg week 2")
            pseg_info = build.period(1,2,current_info)
            generate_psubview(psubview,csubview,pseg_info)
        if sender.selected_index == 2:
            print("pseg week 3")
            pseg_info = build.period(2,3,current_info)
            generate_psubview(psubview,csubview,pseg_info)
        elif sender.selected_index == 3:
            print("pseg week 4")
            pseg_info = build.period(3,4,current_info)
            generate_psubview(psubview,csubview,pseg_info)

    def fseg_select(sender):
        if sender.selected_index == 0:
            print("fseg monthly")
            #period(master_dict,0,1)
        elif sender.selected_index == 1:
            print("fseg yearly")
            #period(master_dict,1,2)

    #seg control top of page
    pseg_control = ui.SegmentedControl(name= 'pseg_control', frame = (vis['pseg_control_x'], vis['pseg_control_y'],vis['pseg_control_w'],vis['pseg_control_h']))
    pseg_control.segments = ("Week 1","Week 2","Week 3","Week 4","Best Week")
    pseg_control.action = pseg_select
    pseg_control.selected_index = 0
    view.add_subview(pseg_control)

    #seg control bottom of page
    fseg_control = ui.SegmentedControl(name= 'fseg_control', frame = (vis['fseg_control_x'], vis['fseg_control_y'],vis['fseg_control_w'],vis['fseg_control_h']))
    fseg_control.segments = ("Monthly","Yearly")
    fseg_control.action = fseg_select
    fseg_control.selected_index = 0
    view.add_subview(fseg_control)

def generate_psubview(psubview,csubview,pseg_info): #give the subview and list of information and this generates the rest, adds to subview given

    #title
    ptitle = ui.Label(name = 'ptitle', bg_color ='yellow', frame = (vis['ptitle_x'], vis['ptitle_y'], vis['ptitle_w'], vis['ptitle_h']))
    ptitle.text = pseg_info['title']
    ptitle.alignment = 1 #1 is center
    psubview.add_subview(ptitle)

    #subtitles
    psubtitle_title = ui.Label(name = 'psubtitle_title', bg_color ='gray', frame = (vis['psubtitle_title_x'], vis['psubtitle_title_y'], vis['psubtitle_title_w'], vis['psubtitle_title_h']))
    psubtitle_title.text = pseg_info['subtitle_title']
    psubtitle_title.alignment = 1 #1 is center
    psubview.add_subview(psubtitle_title)

    psubtitle_value = ui.Label(name = 'psubtitle_value', bg_color ='pink', frame = (vis['psubtitle_value_x'], vis['psubtitle_value_y'], vis['psubtitle_value_w'], vis['psubtitle_value_h']))
    psubtitle_value.text = pseg_info['subtitle_value']
    psubtitle_value.alignment = 1 #1 is center
    psubview.add_subview(psubtitle_value)

    #box titles
    for n,label in enumerate(pseg_info['box_titles']): #enumerate over list
        count = len(pseg_info['box_titles'])
        vis['box_titles_w'] = vis['psub_w']/count #divide width by number of labels
        vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
        label_title.number_of_lines = 0
        label_title.text = label #since list, label is the value
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.border_color = 'black'
        label_title.border_width = 1
        psubview.add_subview(label_title)

    for n,label in enumerate(pseg_info['box_values']):
        count = len(pseg_info['box_values'])
        vis['box_values_w'] = vis['psub_w']/count #divide width by number of labels
        vis['box_values_x'] = vis['box_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
        label_title.number_of_lines = 0
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',10)
        label_title.border_color = 'black'
        label_title.border_width = 1
        psubview.add_subview(label_title)

    #total title/labels
    ptotal_title = ui.Label(name = 'ptotal_title', bg_color ='pink', frame = (vis['total_title_x'], vis['total_title_y'], vis['total_title_w'], vis['total_title_h']))
    ptotal_title.text = pseg_info['total_title']
    ptotal_title.alignment = 1 #1 is center
    ptotal_title.font =  ('<system>',10)
    psubview.add_subview(ptotal_title)

    for n,label in enumerate(pseg_info['total_values']):
        n = n+1 #account for first box being the static label
        count = len(pseg_info['total_values'])
        vis['total_values_w'] = vis['psub_w']/(count+1) #divide width by number of labels
        vis['total_values_x'] = vis['total_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'lightblue', frame = (vis['total_values_x'], vis['total_values_y'], vis['total_values_w'], vis['total_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',12)
        label_title.border_color = 'black'
        label_title.border_width = 1
        psubview.add_subview(label_title)

    #remaining - MODIFY CSUBVIEW HERE
    csubtitle1_value = ui.Label(name = 'csubtitle1_value', bg_color ='pink', frame = (vis['csubtitle1_value_x'], vis['csubtitle1_value_y'], vis['csubtitle1_value_w'], vis['csubtitle1_value_h']))
    csubtitle1_value.text = pseg_info['remaining_miles']
    csubtitle1_value.alignment = 1 #1 is center
    csubview.add_subview(csubtitle1_value)

    csubtitle2_value = ui.Label(name = 'csubtitle2_value', bg_color ='pink', frame = (vis['csubtitle2_value_x'], vis['csubtitle2_value_y'], vis['csubtitle2_value_w'], vis['csubtitle2_value_h']))
    csubtitle2_value.text = pseg_info['remaining_per_run']
    csubtitle2_value.alignment = 1 #1 is center
    csubview.add_subview(csubtitle2_value)

def generate_csubview(csubview,cseg_info):

    #Title
    ctitle = ui.Label(name = 'ctitle', bg_color ='yellow', frame = (vis['ctitle_x'], vis['ctitle_y'], vis['ctitle_w'], vis['ctitle_h']))
    ctitle.text = cseg_info['title']
    ctitle.alignment = 1 #1 is center
    csubview.add_subview(ctitle)

    #subtitles
    csubtitle1_title = ui.Label(name = 'csubtitle1_title', bg_color ='gray', frame = (vis['csubtitle1_title_x'], vis['csubtitle1_title_y'], vis['csubtitle1_title_w'], vis['csubtitle1_title_h']))
    csubtitle1_title.text = cseg_info['subtitle1_title']
    csubtitle1_title.alignment = 1 #1 is center
    csubview.add_subview(csubtitle1_title)

    #moved to above
    # csubtitle1_value = ui.Label(name = 'csubtitle1_value', bg_color ='pink', frame = (vis['csubtitle1_value_x'], vis['csubtitle1_value_y'], vis['csubtitle1_value_w'], vis['csubtitle1_value_h']))
    # csubtitle1_value.text = cseg_info['subtitle1_value']
    # csubtitle1_value.alignment = 1 #1 is center
    # csubview.add_subview(csubtitle1_value)

    csubtitle2_title = ui.Label(name = 'csubtitle2_title', bg_color ='gray', frame = (vis['csubtitle2_title_x'], vis['csubtitle2_title_y'], vis['csubtitle2_title_w'], vis['csubtitle2_title_h']))
    csubtitle2_title.text = cseg_info['subtitle2_title']
    csubtitle2_title.alignment = 1 #1 is center
    csubview.add_subview(csubtitle2_title)

    #moved to above
    # csubtitle2_value = ui.Label(name = 'csubtitle2_value', bg_color ='pink', frame = (vis['csubtitle2_value_x'], vis['csubtitle2_value_y'], vis['csubtitle2_value_w'], vis['csubtitle2_value_h']))
    # csubtitle2_value.text = cseg_info['subtitle2_value']
    # csubtitle2_value.alignment = 1 #1 is center
    # csubview.add_subview(csubtitle2_value)

    #box titles
    for n,label in enumerate(cseg_info['box_titles']):
        count = len(cseg_info['box_titles'])
        vis['box_titles_w'] = vis['csub_w']/count #divide width by number of labels
        vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.border_color = 'black'
        label_title.border_width = 1
        csubview.add_subview(label_title)

    for n,label in enumerate(cseg_info['box_values']):
        count = len(cseg_info['box_values'])
        vis['box_values_w'] = vis['csub_w']/count #divide width by number of labels
        vis['box_values_x'] = vis['box_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',10)
        label_title.border_color = 'black'
        label_title.border_width = 1
        csubview.add_subview(label_title)

    #total title/labels
    ctotal_title = ui.Label(name = 'ptotal_title', bg_color ='pink', frame = (vis['total_title_x'], vis['total_title_y'], vis['total_title_w'], vis['total_title_h']))
    ctotal_title.text = cseg_info['total_title']
    ctotal_title.alignment = 1 #1 is center
    csubview.add_subview(ctotal_title)

    for n,label in enumerate(cseg_info['total_values']):
        n = n+1 #account for first box being the static label
        count = len(cseg_info['total_values'])
        vis['total_values_w'] = vis['psub_w']/(count+1) #divide width by number of labels
        vis['total_values_x'] = vis['total_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'lightblue', frame = (vis['total_values_x'], vis['total_values_y'], vis['total_values_w'], vis['total_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',10)
        label_title.border_color = 'black'
        label_title.border_width = 1
        csubview.add_subview(label_title)

def generate_fsubview(fsubview,fseg_info):
    #title
    ftitle = ui.Label(name = 'ftitle', bg_color ='yellow', frame = (vis['ftitle_x'], vis['ftitle_y'], vis['ftitle_w'], vis['ftitle_h']))
    ftitle.text = "ftitle"
    ftitle.alignment = 1 #1 is center
    fsubview.add_subview(ftitle)

    #box titles LEFT
    for n,label in enumerate(fseg_info['flbox_titles']):
        #count = len(fbox_titles)
        #vis['fbox_titles_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['fbox_titles_y'] = (vis['fbox_titles_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1 #account for title
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['fbox_titles_x'], vis['fbox_titles_y'], vis['fbox_titles_w'], vis['fbox_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.border_color = 'black'
        label_title.border_width = 1
        fsubview.add_subview(label_title)

    for n,label in enumerate(fseg_info['flbox_values']):
        #count = len(fbox_values)
        #vis['fbox_values_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['fbox_values_y'] = (vis['fbox_values_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'pink', frame = (vis['fbox_values_x'], vis['fbox_values_y'], vis['fbox_values_w'], vis['fbox_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',10)
        label_title.border_color = 'black'
        label_title.border_width = 1
        fsubview.add_subview(label_title)

    # #box titles RIGHT
    for n,label in enumerate(fseg_info['frbox_titles']):
        #count = len(fbox_titles)
        #vis['fbox_titles_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['frbox_titles_y'] = (vis['frbox_titles_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1 #account for title
        label_title = ui.Label(name = label, bg_color = 'yellow', frame = (vis['frbox_titles_x'], vis['frbox_titles_y'], vis['frbox_titles_w'], vis['frbox_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.border_color = 'black'
        label_title.border_width = 1
        fsubview.add_subview(label_title)

    for n,label in enumerate(fseg_info['frbox_values']):
        #count = len(fbox_values)
        #vis['fbox_values_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['frbox_values_y'] = (vis['frbox_values_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'pink', frame = (vis['frbox_values_x'], vis['frbox_values_y'], vis['frbox_values_w'], vis['frbox_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',10)
        label_title.border_color = 'black'
        label_title.border_width = 1
        fsubview.add_subview(label_title)

##### run on open
global current_info #so this doesn't need to be passed into functions everywhere
current_info = build.current_period() #get current info, finds out current miles ran this week for pseg calculations
pseg_info = build.period(0,1,current_info) #build pseg, give current_info for initial run

generate_segmented_controls(view) #build segmented controls

generate_csubview(csubview,current_info) #build csubview
generate_psubview(psubview,csubview,pseg_info) #generate first pview
generate_fsubview(fsubview,build.monthly(4))

view.present(style='sheet', hide_title_bar=True)
