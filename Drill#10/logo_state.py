from pico2d import *
import game_framework
import play_state
import title_state

image = None
running = True
logo_time = 0.0

def enter():
    global image,logo_time,running
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    running = True
    pass

def exit():
    global image
    del image
    # fill here
    pass

def update():
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        game_framework.change_state(title_state)
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





