import math
from pico2d import *        # 조금씩 붙이고 실행하기!!
                            # 그래야 어디서 오류가 발생하는지 알 수 있음.

open_canvas()

grass=load_image('grass.png')
character = load_image('character.png')

def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)


def run_circle():   # 내가 할려는 일의 설명.
    print('CIRCLE')
    
    cx, cy, r= 400,300,210
    for deg in range(0,360,5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        render_all(x,y)
    
   # pass            # == {}

def run_rectangle():
    print('RECTANGLE')

    # bottom line
    for x in range(50,750 + 1,10):
        render_all(x,90)

    # right line
    for y in range(90,550+1,10):
        render_all(750,y)

    # top line
    for x in range(750,50 - 1,-10):
        render_all(x,550)

    # left line
    for y in range(550,90 - 1,-10):
        render_all(50,y)  


while   True:
    run_circle()       #함수로 만들었기 때문에 코멧트아웃하기 쉬움. 실제로 어제 어려웟음.
    run_rectangle()
    break


close_canvas()
