from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            print(event.key)
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_q:
                    if play_state.boy_count<10:
                        play_state.boy_count += 1
                    print(play_state.boy_count)
                case pico2d.SDLK_w:
                    if play_state.boy_count > 1:
                        play_state.boy_count -= 1
                case 61:
                    if play_state.boy_count < 10:
                        play_state.boy_count += 1
                case 45:
                    if play_state.boy_count > 1:
                        play_state.boy_count -= 1
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    play_state.draw_world()
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass

