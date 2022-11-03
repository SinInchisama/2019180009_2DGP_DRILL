from pico2d import *
import game_framework
from Ball import Ball
import game_world
from grass import Grass
from boy import Boy


boy = None
grass = None
balls = None
ball1 = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass,balls
    boy = Boy()
    game_world.add_Object(boy,1)
    grass = Grass()
    game_world.add_Object(grass,0)
    grass = Grass(400,20)
    game_world.add_Object(grass, 1)
    # balls = [Ball()]

# 종료
def exit():
    game_world.clear()

def update():
    for Object in game_world.all_objects():
        Object.update()

    # boy.update()
    # for ball in balls:
    #     ball.update()

def draw_world():
    for Object in game_world.all_objects():
        Object.draw()
    # grass.draw()
    # boy.draw()
    # for ball in balls:
    #     ball.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
