#import get_data
import ui
from pprint import pprint
import datetime
import build

w,h = ui.get_screen_size()
view = ui.View(bg_color = 'black', frame = (0,0,w,h)) #main view

runs_per_week = 5

def vis(w,h):
    vis = {}
    vis['x_margin'] = 5
    vis['y_margin'] = 50 #fixed for notch
    vis['first_box_width'] = 100

    #SUBVIEWS
    vis['psub_h'] = 182 #(h*.33) - 20
    vis['psub_w'] = w - (vis['x_margin']*2) #sets width for all subviews
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin'] + 30

    vis['csub_h'] = 182 #h*.33
    vis['csub_w'] = vis['psub_w']
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['psub_y'] + vis['psub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    vis['fsub_h'] = h*.33 #h*.29 #updated for iphone x
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
    vis['ptitle_h'] = 30
    vis['ptitle_w'] = vis['psub_w']
    vis['ptitle_x'] = 0
    vis['ptitle_y'] = 0

    vis['psubtitle_title_h'] = 20
    vis['psubtitle_title_w'] = vis['psub_w']/4
    vis['psubtitle_title_x'] = 0 #first
    vis['psubtitle_title_y'] = vis['ptitle_h']

    vis['psubtitle_value_h'] = 20
    vis['psubtitle_value_w'] = vis['psub_w']/4
    vis['psubtitle_value_x'] = vis['psub_w']/4 #second
    vis['psubtitle_value_y'] = vis['ptitle_h']

    vis['psubtitle2_title_h'] = 20
    vis['psubtitle2_title_w'] = vis['psub_w']/4
    vis['psubtitle2_title_x'] = vis['psub_w']/4 * 2 #third
    vis['psubtitle2_title_y'] = vis['ptitle_h']

    vis['psubtitle2_value_h'] = 20
    vis['psubtitle2_value_w'] = vis['psub_w']/4
    vis['psubtitle2_value_x'] = vis['psub_w']/4 * 3 #fourth
    vis['psubtitle2_value_y'] = vis['ptitle_h']

    #box titles
    vis['box_titles_h'] = 20
    vis['box_titles_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_titles_x'] = 1 #this is later changed dynamically
    vis['box_titles_y'] = vis['psubtitle_value_y'] + vis['psubtitle_value_h']

    vis['box_values_h'] = 90
    vis['box_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['box_values_x'] = 1 #this is later changed dynamically
    vis['box_values_y'] = vis['box_titles_y'] + vis['box_titles_h']

    #Bottom Labels - CSUB AND FSUB
    vis['total_title_h'] = 20
    vis['total_title_w'] = vis['first_box_width']
    vis['total_title_x'] = 0
    vis['total_title_y'] = vis['box_values_y'] + vis['box_values_h']  #150

    vis['total_values_h'] = 20
    vis['total_values_w'] = vis['psub_w'] #this is later changed dynamically
    vis['total_values_x'] = 1 #this is later changed dynamically
    vis['total_values_y'] = vis['total_title_y'] #150

    ########################################################cSUB########################################################

    #LABELS
    vis['ctitle_h'] = 30
    vis['ctitle_w'] = vis['psub_w']
    vis['ctitle_x'] = 0
    vis['ctitle_y'] = 0

    #subtitles 10 percent
    vis['csubtitle1_title_h'] = 20
    vis['csubtitle1_title_w'] = vis['psub_w']/6
    vis['csubtitle1_title_x'] = 0 #first
    vis['csubtitle1_title_y'] = vis['ctitle_h']

    vis['csubtitle1_value_h'] = 20
    vis['csubtitle1_value_w'] = vis['psub_w']/6
    vis['csubtitle1_value_x'] = vis['psub_w']/6 #second
    vis['csubtitle1_value_y'] = vis['ctitle_h']

    vis['csubtitle2_title_h'] = 20
    vis['csubtitle2_title_w'] = vis['psub_w']/6
    vis['csubtitle2_title_x'] = (vis['psub_w']/6) * 2 #third
    vis['csubtitle2_title_y'] = vis['ctitle_h']

    vis['csubtitle2_value_h'] = 20
    vis['csubtitle2_value_w'] = vis['psub_w']/6
    vis['csubtitle2_value_x'] = (vis['psub_w']/6) * 3 #fourth
    vis['csubtitle2_value_y'] = vis['ctitle_h']

    vis['csubtitle3_title_h'] = 20
    vis['csubtitle3_title_w'] = vis['psub_w']/6
    vis['csubtitle3_title_x'] = (vis['psub_w']/6) * 4 #fifth
    vis['csubtitle3_title_y'] = vis['ctitle_h']

    vis['csubtitle3_value_h'] = 20
    vis['csubtitle3_value_w'] = vis['psub_w']/6
    vis['csubtitle3_value_x'] = (vis['psub_w']/6) * 5 #sixth
    vis['csubtitle3_value_y'] = vis['ctitle_h']

    ########################################################FSUB########################################################
    #SEGMENTED CONTROL
    vis['fseg_control_h'] = 30
    vis['fseg_control_w'] = vis['psub_w']
    vis['fseg_control_x'] = vis['x_margin']
    vis['fseg_control_y'] = (vis['y_margin']/2) + vis['csub_h'] + vis['csub_y'] #margin plus the view above position and height

    #FLABELS
    vis['ftitle_h'] = 20
    vis['ftitle_w'] = vis['psub_w']
    vis['ftitle_x'] = 0
    vis['ftitle_y'] = 0

    #box titles LEFT
    subbox_count = 14 #this is not an accurate way to do this
    vis['fbox_titles_h'] = (vis['fsub_h'] - vis['ftitle_h']) / subbox_count
    vis['fbox_titles_w'] = (vis['psub_w']/2) * .7
    vis['fbox_titles_x'] = 0
    vis['fbox_titles_y'] = 1 #this needs to be changed

    vis['fbox_values_h'] = vis['fbox_titles_h']
    vis['fbox_values_w'] = (vis['psub_w']/2) * .3
    vis['fbox_values_x'] = vis['fbox_titles_w']
    vis['fbox_values_y'] = 1 #this needs to be changed

    #box titles RIGHT
    vis['frbox_titles_h'] = (vis['fsub_h'] - vis['ftitle_h']) / subbox_count
    vis['frbox_titles_w'] = (vis['psub_w']/2) * .7
    vis['frbox_titles_x'] = (vis['psub_w']/4) * 2
    vis['frbox_titles_y'] = 1 #this needs to be changed

    vis['frbox_values_h'] = vis['frbox_titles_h']
    vis['frbox_values_w'] = (vis['psub_w']/2) * .3
    vis['frbox_values_x'] =  vis['frbox_titles_x'] + vis['frbox_titles_w'] #where titles start, plus width of titles
    vis['frbox_values_y'] = 1 #this needs to be changed

    ###### Imageview

    vis['imageview_x'] = 0
    vis['imageview_y'] = 0 #vis['fbox_titles_h'] #start where title ends
    vis['imageview_h'] = vis['fsub_h'] #- vis['fbox_titles_h'] #tall as subview, minus title
    vis['imageview_w'] = vis['fsub_w'] #wide as subview

    vis['fbackground_x'] = 0
    vis['fbackground_y'] = 0 #vis['fbox_titles_h'] #start where title ends
    vis['fbackground_h'] = vis['fsub_h'] #- vis['fbox_titles_h'] #tall as subview, minus title
    vis['fbackground_w'] = vis['fsub_w'] #wide as subview

    return vis

vis = vis(w,h)

#SUBVIEWS
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'black')
fsubview = ui.View(frame=(vis['fsub_x'], vis['fsub_y'], vis['fsub_w'], vis['fsub_h']), background_color = 'black')

view.add_subview(psubview)
view.add_subview(csubview)
view.add_subview(fsubview)

def generate_segmented_controls(view):
    def pseg_select(sender):
        if sender.selected_index == 0:
            pseg_info = build.period(0,1,current_info) #build pseg info, give current stats to find remaining_miles and MPR
            generate_psubview(psubview,csubview,pseg_info)
        if sender.selected_index == 1:
            pseg_info = build.period(1,2,current_info)
            generate_psubview(psubview,csubview,pseg_info)
        if sender.selected_index == 2:
            pseg_info = build.period(2,3,current_info)
            generate_psubview(psubview,csubview,pseg_info)
        if sender.selected_index == 3:
            pseg_info = build.period(3,4,current_info)
            generate_psubview(psubview,csubview,pseg_info)
        elif sender.selected_index == 4:
            pseg_info = build.top_period(4,current_info)
            generate_psubview(psubview,csubview,pseg_info)

    def fseg_select(sender):
        if sender.selected_index == 0:
            generate_fsubview(fsubview,build.monthly(runs_per_week))
        if sender.selected_index == 1:
            generate_fsubview(fsubview,build.yearly(runs_per_week))
        if sender.selected_index == 2:
            generate_fsubview(fsubview,build.weekly(current_info))
        if sender.selected_index == 3:
            generate_yearly_graph()
        if sender.selected_index == 4:
            generate_yearly_prediction_graph()
        elif sender.selected_index == 5:
            generate_weekly_graph()


    #seg control top of page
    pseg_control = ui.SegmentedControl(name= 'pseg_control', frame = (vis['pseg_control_x'], vis['pseg_control_y'],vis['pseg_control_w'],vis['pseg_control_h']))
    pseg_control.segments = ("Week 1","Week 2","Week 3","Week 4","Best Week")
    pseg_control.action = pseg_select
    pseg_control.selected_index = 0
    view.add_subview(pseg_control)

    #seg control bottom of page
    fseg_control = ui.SegmentedControl(name= 'fseg_control', frame = (vis['fseg_control_x'], vis['fseg_control_y'],vis['fseg_control_w'],vis['fseg_control_h']))
    fseg_control.segments = ("Monthly","Yearly","Weekly","YTD","Predic","Weeks")
    fseg_control.action = fseg_select
    fseg_control.selected_index = 0
    view.add_subview(fseg_control)

def generate_psubview(psubview,csubview,pseg_info): #give the subview and list of information and this generates the rest, adds to subview given

    #title
    ptitle = ui.Label(name = 'ptitle', bg_color ='black', frame = (vis['ptitle_x'], vis['ptitle_y'], vis['ptitle_w'], vis['ptitle_h']))
    ptitle.text = pseg_info['title']
    ptitle.alignment = 1 #1 is center
    ptitle.font =  ('<system-bold>',18)
    ptitle.text_color = 'white'
    psubview.add_subview(ptitle)

    #subtitles
    psubtitle_title = ui.Label(name = 'psubtitle_title', bg_color ='black', frame = (vis['psubtitle_title_x'], vis['psubtitle_title_y'], vis['psubtitle_title_w'], vis['psubtitle_title_h']))
    psubtitle_title.text = pseg_info['subtitle_title']
    psubtitle_title.alignment = 1 #1 is center, 2 is right, 3
    psubtitle_title.font = ('<system>',14)
    psubtitle_title.text_color = 'white'
    #psubtitle_title.font =  ('<system-bold>',14)
    psubview.add_subview(psubtitle_title)

    psubtitle_value = ui.Label(name = 'psubtitle_value', bg_color ='black', frame = (vis['psubtitle_value_x'], vis['psubtitle_value_y'], vis['psubtitle_value_w'], vis['psubtitle_value_h']))
    psubtitle_value.text = pseg_info['subtitle_value']
    psubtitle_value.text_color = '#4286f4'
    psubtitle_value.alignment = 1 #1 is center
    psubtitle_value.font = ('<system>',10)
    psubview.add_subview(psubtitle_value)

    #new
    psubtitle2_title = ui.Label(name = 'psubtitle2_title', bg_color ='black', frame = (vis['psubtitle2_title_x'], vis['psubtitle2_title_y'], vis['psubtitle2_title_w'], vis['psubtitle2_title_h']))
    psubtitle2_title.text = pseg_info['subtitle2_title']
    psubtitle2_title.alignment = 1 #1 is center, 2 is right, 3
    psubtitle2_title.font = ('<system>',14)
    psubtitle2_title.text_color = 'white'
    #psubtitle_title.font =  ('<system-bold>',14)
    psubview.add_subview(psubtitle2_title)

    psubtitle2_value = ui.Label(name = 'psubtitle2_value', bg_color ='black', frame = (vis['psubtitle2_value_x'], vis['psubtitle2_value_y'], vis['psubtitle2_value_w'], vis['psubtitle2_value_h']))
    psubtitle2_value.text = pseg_info['subtitle2_value']
    psubtitle2_value.text_color = '#4286f4'
    psubtitle2_value.alignment = 1 #1 is center
    psubtitle2_value.font = ('<system>',10)
    psubview.add_subview(psubtitle2_value)

    #box titles
    for n,label in enumerate(pseg_info['box_titles']): #enumerate over list
        count = len(pseg_info['box_titles'])
        if n == 0:
            first_box_w = 100
            vis['box_titles_w'] = vis['first_box_width']
            vis['box_titles_x'] = 0
        else:
            vis['box_titles_w'] = (vis['psub_w']-vis['first_box_width'])/(count-1) #divide width by number of labels
            vis['box_titles_x'] = (vis['box_titles_w'] * (n-1)) + vis['first_box_width']#first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
        label_title.number_of_lines = 0
        label_title.text = label #since list, label is the value
        label_title.alignment = 1
        label_title.font =  ('<system>',15)
        label_title.text_color = 'white'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        psubview.add_subview(label_title)

    #box values
    for n,label in enumerate(pseg_info['box_values']):
        count = len(pseg_info['box_values'])
        if n == 0:
            first_box_w = 100
            vis['box_values_w'] = vis['first_box_width']
            vis['box_values_x'] = 0
        else:
            vis['box_values_w'] = (vis['psub_w']-vis['first_box_width'])/(count-1) #divide width by number of labels
            vis['box_values_x'] = (vis['box_values_w'] * (n-1)) + vis['first_box_width']#first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
        label_title.number_of_lines = 0
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14) #this is the top box values for previous peroids
        label_title.text_color = '#4286f4'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        psubview.add_subview(label_title)

    #total title
    ptotal_title = ui.Label(name = 'ptotal_title', bg_color ='black', frame = (vis['total_title_x'], vis['total_title_y'], vis['total_title_w'], vis['total_title_h']))
    ptotal_title.text = pseg_info['total_title']
    ptotal_title.alignment = 1 #1 is center
    ptotal_title.font =  ('<system-bold>',16)
    ptotal_title.text_color = 'white'
    psubview.add_subview(ptotal_title)

    #total value
    for n,label in enumerate(pseg_info['total_values']):
        #n = n+1 #account for first box being the static label
        count = len(pseg_info['total_values'])
        vis['total_values_w'] = (vis['psub_w']-vis['total_title_w'])/(count)
        vis['total_values_x'] = vis['total_title_w'] + (vis['total_values_w'] * n)
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['total_values_x'], vis['total_values_y'], vis['total_values_w'], vis['total_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',16)
        label_title.text_color = 'red'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        psubview.add_subview(label_title)

    #remaining - MODIFY CSUBVIEW HERE
    csubtitle1_value = ui.Label(name = 'csubtitle1_value', bg_color ='black', frame = (vis['csubtitle1_value_x'], vis['csubtitle1_value_y'], vis['csubtitle1_value_w'], vis['csubtitle1_value_h']))
    csubtitle1_value.text = pseg_info['remaining_miles']
    csubtitle1_value.font = ('<system>',14)
    csubtitle1_value.alignment = 1 #1 is center
    csubtitle1_value.text_color = '#4286f4'
    csubview.add_subview(csubtitle1_value)

    csubtitle2_value = ui.Label(name = 'csubtitle2_value', bg_color ='black', frame = (vis['csubtitle2_value_x'], vis['csubtitle2_value_y'], vis['csubtitle2_value_w'], vis['csubtitle2_value_h']))
    csubtitle2_value.text = pseg_info['remaining_miles_match']
    #csubtitle2_value.text = pseg_info['remaining_per_run']
    csubtitle2_value.font = ('<system>',14)
    csubtitle2_value.text_color = '#4286f4'
    csubtitle2_value.alignment = 1 #1 is center
    csubview.add_subview(csubtitle2_value)

    csubtitle3_value = ui.Label(name = 'csubtitle3_value', bg_color ='black', frame = (vis['csubtitle3_value_x'], vis['csubtitle3_value_y'], vis['csubtitle3_value_w'], vis['csubtitle3_value_h']))
    csubtitle3_value.text = pseg_info['remaining_miles_down']
    #csubtitle2_value.text = pseg_info['remaining_per_run']
    csubtitle3_value.font = ('<system>',14)
    csubtitle3_value.text_color = '#4286f4'
    csubtitle3_value.alignment = 1 #1 is center
    csubview.add_subview(csubtitle3_value)

def generate_csubview(csubview,cseg_info):

    #Title
    ctitle = ui.Label(name = 'ctitle', bg_color ='black', frame = (vis['ctitle_x'], vis['ctitle_y'], vis['ctitle_w'], vis['ctitle_h']))
    ctitle.text = cseg_info['title']
    ctitle.font =  ('<system-bold>',18)
    ctitle.text_color = 'white'
    ctitle.alignment = 1 #1 is center
    csubview.add_subview(ctitle)

    #subtitles
    csubtitle1_title = ui.Label(name = 'csubtitle1_title', bg_color ='black', frame = (vis['csubtitle1_title_x'], vis['csubtitle1_title_y'], vis['csubtitle1_title_w'], vis['csubtitle1_title_h']))
    csubtitle1_title.text = cseg_info['subtitle1_title']
    csubtitle1_title.font = ('<system>',14)
    csubtitle1_title.text_color = 'white'
    csubtitle1_title.alignment = 1 #1 is center
    csubview.add_subview(csubtitle1_title)

    csubtitle2_title = ui.Label(name = 'csubtitle2_title', bg_color ='black', frame = (vis['csubtitle2_title_x'], vis['csubtitle2_title_y'], vis['csubtitle2_title_w'], vis['csubtitle2_title_h']))
    csubtitle2_title.text = cseg_info['subtitle2_title']
    csubtitle2_title.font = ('<system>',14)
    csubtitle2_title.text_color = 'white'
    csubtitle2_title.alignment = 1 #1 is center
    csubview.add_subview(csubtitle2_title)

    csubtitle3_title = ui.Label(name = 'csubtitle3_title', bg_color ='black', frame = (vis['csubtitle3_title_x'], vis['csubtitle3_title_y'], vis['csubtitle3_title_w'], vis['csubtitle3_title_h']))
    csubtitle3_title.text = cseg_info['subtitle3_title']
    csubtitle3_title.font = ('<system>',14)
    csubtitle3_title.text_color = 'white'
    csubtitle3_title.alignment = 1 #1 is center
    csubview.add_subview(csubtitle3_title)

    #box titles
    for n,label in enumerate(cseg_info['box_titles']):
        count = len(cseg_info['box_titles'])
        if n == 0:
            first_box_w = 100
            vis['box_titles_w'] = vis['first_box_width']
            vis['box_titles_x'] = 0
        else:
            vis['box_titles_w'] = (vis['csub_w']-vis['first_box_width'])/(count-1) #divide width by number of labels
            vis['box_titles_x'] = (vis['box_titles_w'] * (n-1)) + vis['first_box_width']#first label at 0, second label at width*1

        #vis['box_titles_w'] = vis['csub_w']/count #divide width by number of labels
        #vis['box_titles_x'] = vis['box_titles_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['box_titles_x'], vis['box_titles_y'], vis['box_titles_w'], vis['box_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',15)
        label_title.text_color = 'white'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        csubview.add_subview(label_title)

    #box values
    for n,label in enumerate(cseg_info['box_values']):
        count = len(cseg_info['box_values'])
        if n == 0:
            first_box_w = 100
            vis['box_values_w'] = vis['first_box_width']
            vis['box_values_x'] = 0
        else:
            vis['box_values_w'] = (vis['csub_w']-vis['first_box_width'])/(count-1) #divide width by number of labels
            vis['box_values_x'] = (vis['box_values_w'] * (n-1)) + vis['first_box_width']#first label at 0, second label at width*1
        #vis['box_values_w'] = vis['csub_w']/count #divide width by number of labels
        #vis['box_values_x'] = vis['box_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['box_values_x'], vis['box_values_y'], vis['box_values_w'], vis['box_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.number_of_lines = 0
        label_title.font =  ('<system>',14)
        label_title.text_color = '#4286f4'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        csubview.add_subview(label_title)

    #total title/labels
    ctotal_title = ui.Label(name = 'ptotal_title', bg_color ='black', frame = (vis['total_title_x'], vis['total_title_y'], vis['total_title_w'], vis['total_title_h']))
    ctotal_title.text = cseg_info['total_title']
    ctotal_title.alignment = 1 #1 is center
    ctotal_title.font =  ('<system-bold>',16)
    ctotal_title.text_color = 'white'
    csubview.add_subview(ctotal_title)

    #total values
    for n,label in enumerate(cseg_info['total_values']):
        #n = n+1 #account for first box being the static label
        count = len(cseg_info['total_values'])
        vis['total_values_w'] = (vis['psub_w']-vis['total_title_w'])/(count)
        vis['total_values_x'] = vis['total_title_w'] + (vis['total_values_w'] * n)
        #vis['total_values_w'] = vis['psub_w']/(count+1) #divide width by number of labels
        #vis['total_values_x'] = vis['total_values_w'] * n #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['total_values_x'], vis['total_values_y'], vis['total_values_w'], vis['total_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',16)
        label_title.text_color = 'red'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        csubview.add_subview(label_title)

def generate_fsubview(fsubview,fseg_info):
    #background
    fbackground = ui.Label(name = 'fbackground', bg_color ='black', frame = (vis['fbackground_x'], vis['fbackground_y'], vis['fbackground_w'], vis['fbackground_h']))
    fbackground.text = ''
    #sublabel.text_color = 'white'
    #sublabel.alignment = 1 #1 is center
    fsubview.add_subview(fbackground)

    #title
    ftitle = ui.Label(name = 'ftitle', bg_color ='black', frame = (vis['ftitle_x'], vis['ftitle_y'], vis['ftitle_w'], vis['ftitle_h']))
    ftitle.text = fseg_info['title']
    ftitle.text_color = 'white'
    ftitle.alignment = 1 #1 is center
    fsubview.add_subview(ftitle)

    #box titles LEFT
    for n,label in enumerate(fseg_info['flbox_titles']):
        #count = len(fbox_titles)
        #vis['fbox_titles_w'] = vis['fsub_w']/count #divide width by number of labels
        ####vis['fbox_titles_h']
        vis['fbox_titles_y'] = (vis['fbox_titles_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1 #account for title
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['fbox_titles_x'], vis['fbox_titles_y'], vis['fbox_titles_w'], vis['fbox_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.text_color = 'white'
        #label_title.border_color = 'white'
        #label_title.border_width = 1
        fsubview.add_subview(label_title)

    for n,label in enumerate(fseg_info['flbox_values']): #very bottom, right hand values
        #count = len(fbox_values)
        #vis['fbox_values_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['fbox_values_y'] = (vis['fbox_values_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['fbox_values_x'], vis['fbox_values_y'], vis['fbox_values_w'], vis['fbox_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',13)
        label_title.text_color = '#4286f4'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        fsubview.add_subview(label_title)

    # #box titles RIGHT
    for n,label in enumerate(fseg_info['frbox_titles']):
        #count = len(fbox_titles)
        #vis['fbox_titles_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['frbox_titles_y'] = (vis['frbox_titles_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1 #account for title
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['frbox_titles_x'], vis['frbox_titles_y'], vis['frbox_titles_w'], vis['frbox_titles_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',14)
        label_title.text_color = 'white'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        fsubview.add_subview(label_title)

    for n,label in enumerate(fseg_info['frbox_values']): #very bottom, right hand values
        #count = len(fbox_values)
        #vis['fbox_values_w'] = vis['fsub_w']/count #divide width by number of labels
        vis['frbox_values_y'] = (vis['frbox_values_h'] * n) + vis['ftitle_h'] #first label at 0, second label at width*1
        label_title = ui.Label(name = label, bg_color = 'black', frame = (vis['frbox_values_x'], vis['frbox_values_y'], vis['frbox_values_w'], vis['frbox_values_h']) )
        label_title.text = label
        label_title.alignment = 1
        label_title.font =  ('<system>',13)
        label_title.text_color = '#4286f4'
        #label_title.border_color = 'black'
        #label_title.border_width = 0
        fsubview.add_subview(label_title)

def generate_yearly_graph():
    #title
    # ftitle = ui.Label(name = 'ftitle', bg_color ='black', frame = (vis['ftitle_x'], vis['ftitle_y'], vis['ftitle_w'], vis['ftitle_h']))
    # ftitle.text = 'GRAPH'
    # ftitle.text_color = 'white'
    # ftitle.alignment = 1 #1 is center
    # fsubview.add_subview(ftitle)

    #background
    fbackground = ui.Label(name = 'fbackground', bg_color ='black', frame = (vis['fbackground_x'], vis['fbackground_y'], vis['fbackground_w'], vis['fbackground_h']))
    fbackground.text = ''
    #sublabel.text_color = 'white'
    #sublabel.alignment = 1 #1 is center
    fsubview.add_subview(fbackground)

    #graph
    b = build.yearly_graph()
    imageview1 = ui.ImageView(frame = (vis['imageview_x'], vis['imageview_y'], vis['imageview_w'], vis['imageview_h']))
    imageview1.image = ui.Image.from_data(b.getvalue())
    fsubview.add_subview(imageview1)

def generate_yearly_prediction_graph():

    #background
    fbackground = ui.Label(name = 'fbackground', bg_color ='black', frame = (vis['fbackground_x'], vis['fbackground_y'], vis['fbackground_w'], vis['fbackground_h']))
    fbackground.text = ''
    #sublabel.text_color = 'white'
    #sublabel.alignment = 1 #1 is center
    fsubview.add_subview(fbackground)

    #graph
    b = build.yearly_prediction_graph()
    imageview1 = ui.ImageView(frame = (vis['imageview_x'], vis['imageview_y'], vis['imageview_w'], vis['imageview_h']))
    imageview1.image = ui.Image.from_data(b.getvalue())
    fsubview.add_subview(imageview1)

def generate_weekly_graph():

    #background
    fbackground = ui.Label(name = 'fbackground', bg_color ='black', frame = (vis['fbackground_x'], vis['fbackground_y'], vis['fbackground_w'], vis['fbackground_h']))
    fbackground.text = ''
    fsubview.add_subview(fbackground)

    #graph
    b = build.weekly_graph()
    imageview1 = ui.ImageView(frame = (vis['imageview_x'], vis['imageview_y'], vis['imageview_w'], vis['imageview_h']))
    imageview1.image = ui.Image.from_data(b.getvalue())
    fsubview.add_subview(imageview1)

##### run on open
global current_info #so this doesn't need to be passed into functions everywhere
current_info = build.current_period() #get current info, finds out current miles ran this week for pseg calculations
pseg_info = build.period(0,1,current_info) #build pseg, give current_info for initial run

generate_segmented_controls(view) #build segmented controls

generate_csubview(csubview,current_info) #build csubview
generate_psubview(psubview,csubview,pseg_info) #generate first pview
generate_fsubview(fsubview,build.monthly(4))

view.present(style='sheet', hide_title_bar=True)
