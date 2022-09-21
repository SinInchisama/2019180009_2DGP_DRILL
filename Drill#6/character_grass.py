from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


while True:
        x = 400
        y = 90
        Angle = 0
        while Angle< 361:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x + x * math.sin(Angle / 360 *2*math.pi),y + 200 - 200 * math.cos(Angle / 360 * 2 * math.pi))
                Angle = Angle + 1
        while x<770:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x = x + 2
        while y<570:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y = y + 2
        while x>20:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x = x - 2
        while y>90:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                y = y - 2
        while x<400:
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,y)
                x = x + 2
        
close_canvas()
