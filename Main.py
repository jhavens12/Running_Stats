import get_data
import ui
import build
from pprint import pprint
import datetime


w,h = ui.get_screen_size()
view = ui.View(bg_color = 'white', frame = (0,0,w,h)) #main view

def vis(w,h):
    vis = {}
    vis['x_margin'] = 15
    vis['y_margin'] = 10

    vis['psub_h'] = h*.33
    vis['psub_w'] = w - (vis['x_margin']*2)
    vis['psub_x'] = vis['x_margin']
    vis['psub_y'] = vis['y_margin']

    vis['csub_h'] = h*.33
    vis['csub_w'] = w-(vis['x_margin']*2)
    vis['csub_x'] = vis['x_margin']
    vis['csub_y'] = vis['y_margin'] + vis['psub_h'] + vis['y_margin'] #y margin, height of psub, y margin

    return vis

vis = vis(w,h)

#past subview
psubview = ui.View(frame=(vis['psub_x'], vis['psub_y'], vis['psub_w'], vis['psub_h']), background_color = 'black')

#current subview
csubview = ui.View(frame=(vis['csub_x'], vis['csub_y'], vis['csub_w'], vis['csub_h']), background_color = 'blue')


view.add_subview(psubview)
view.add_subview(csubview)


view.present(style='sheet', hide_title_bar=True)
