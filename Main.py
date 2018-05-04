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
    vis['psub_w'] = w - (vis['x_margin']*2)
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin']

    vis['csub_h'] = h*.33
    vis['csub_w'] = w-(vis['x_margin']*2)
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['y_margin'] + vis['psub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    vis['fsub_h'] = h*.26
    vis['fsub_w'] = w-(vis['x_margin']*2)
    vis['fsub_x'] = vis['x_margin']
    vis['fsub_y'] = vis['csub_y'] + vis['csub_h'] + (vis['y_margin']/2) #y margin, height of psub, y margin

    #LABELS
    vis['psub_title_h'] = 20
    vis['psub_title_w'] = vis['psub_w']
    vis['psub_title_x'] = 0
    vis['psub_title_y'] = 0

    return vis

vis = vis(w,h)

#SUBVIEWS
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'blue')
fsubview = ui.View(frame=(vis['fsub_x'], vis['fsub_y'], vis['fsub_w'], vis['fsub_h']), background_color = 'red')
view.add_subview(psubview)
view.add_subview(csubview)
view.add_subview(fsubview)

#LABELS
ptitle = ui.Label(name = 'ptitle', bg_color ='yellow', frame = (vis['psub_title_x'], vis['psub_title_y'], vis['psub_title_w'], vis['psub_title_h']))
ptitle.text = "ptitle"
ptitle.alignment = 1 #1 is center

psubview.add_subview(ptitle)

view.present(style='sheet', hide_title_bar=True)
