from pico2d import *
import game_framework
import logo_state
import title_state
import Item_state
import random
import Add_Sum_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,700), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_state(Item_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            game_framework.push_state(Add_Sum_state)
# 게임 초기화 : 객체들을 생성
boy = None
grass = None # == Null
boy_count = None

def enter():
    global boy, grass, running,boy_count
    boy = [Boy() for i in range(0,10)]
    grass = Grass()
    running = True
    boy_count = 1

# 게임 종료 - 객체를 소멸
def exit():
    global boy, grass
    del boy
    del grass

# 게임 월드 객체를 업데이트. ( 게임 로직 )
def update():
    for i in range(0, boy_count):
        boy[i].update()


# 게임 월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()
    delay(0.001)

def draw_world():
    grass.draw()
    for i in range (0,boy_count):
        boy[i].draw()
    # print(boy[0].item)


def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':  # 만약 단독 실행 상태이면,
    test_self()

