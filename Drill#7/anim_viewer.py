from pico2d import*

open_canvas()

grass = load_image('grass.png')
Trainer = load_image('Trainer.png')
Trainer_walk = (6,443,20,28)
Treainer_runnig = (89,443,22,26)
left_fishing_xy = (283,308,334,368,402)
front_fishing_xy = (299,320,340,360,381)
right_fishing_xy =(284,309,336,368,402)
back_fishing_xy = (292,319,348,370,391)

def draw(left, bottom, width, height, x, y,speed):
    clear_canvas()
    Trainer.clip_draw(left,bottom,width,height,x,y)
    grass.draw(400, 30)
    update_canvas()
    delay(speed)
    get_events()

def left_fishing(x,y):
    frame = 0
    for i in range(0,12,1):
        draw(left_fishing_xy[frame],415,left_fishing_xy[frame+1]-left_fishing_xy[frame],26,x,y,0.2)
        frame = (frame + 1) %4

def front_fishing(x,y):
    frame = 0
    for i in range(0, 12, 1):
        draw(front_fishing_xy[frame], 376, front_fishing_xy[frame + 1] - front_fishing_xy[frame], 35, x, y,0.2)
        frame = (frame + 1) % 4

def right_fishig(x,y):
    frame = 0
    for i in range(0,12,1):
        draw(right_fishing_xy[frame],346,right_fishing_xy[frame+1]-right_fishing_xy[frame],26,x,y,0.2)
        frame = (frame + 1) %4

def back_fishing(x,y):
    frame = 0
    for i in range(0, 12, 1):
        draw(back_fishing_xy[frame], 443, back_fishing_xy[frame + 1] - back_fishing_xy[frame], 30, x, y, 0.2)
        frame = (frame + 1) % 4

def walk_rectangle():
    frame = 0
    for x in range(20,401,3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame,Trainer_walk[1] - Trainer_walk[3]*3,Trainer_walk[2],Trainer_walk[3],x,70,0.05)
        frame = (frame + 1) %3
    front_fishing(400, 70)
    for x in range(401, 780, 3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame, Trainer_walk[1] - Trainer_walk[3] * 3, Trainer_walk[2],Trainer_walk[3], x, 70,0.05)
        frame = (frame + 1) % 3
    for y in range(70,280,3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame, Trainer_walk[1] - Trainer_walk[3] * 2,Trainer_walk[2], Trainer_walk[3], 780, y,0.05)
        frame = (frame + 1) % 3
    right_fishig(780, 280)
    for y in range(280,570,3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame, Trainer_walk[1] - Trainer_walk[3] * 2,Trainer_walk[2], Trainer_walk[3], 780, y,0.05)
        frame = (frame + 1) % 3
    for x in range(780,401,-3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame,Trainer_walk[1] - Trainer_walk[3],Trainer_walk[2],Trainer_walk[3],x,570,0.05)
        frame = (frame + 1) % 3
    back_fishing(400,570)
    for x in range(401,20,-3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame,Trainer_walk[1] - Trainer_walk[3],Trainer_walk[2],Trainer_walk[3],x,570,0.05)
        frame = (frame + 1) % 3
    for y in range(570,280,-3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame, Trainer_walk[1],Trainer_walk[2] - 1, Trainer_walk[3], 20, y,0.05)
        frame = (frame + 1) % 3
    left_fishing(20, 280)
    for y in range(280,70,-3):
        draw(Trainer_walk[0] + Trainer_walk[2] * frame, Trainer_walk[1],Trainer_walk[2] - 1, Trainer_walk[3], 20, y,0.05)
        frame = (frame + 1) % 3

def run_rectangle():
    frame = 0
    for x in range(20,780,3):
        draw(Treainer_runnig[0] + Treainer_runnig[2] * frame,Treainer_runnig[1] - Treainer_runnig[3]*3,Treainer_runnig[2],Treainer_runnig[3],x,70,0.03)
        frame = (frame + 1) %3
    for y in range(70,570,3):
        draw(Treainer_runnig[0] + 20 * frame +4, Treainer_runnig[1],20 , Treainer_runnig[3], 780, y,0.03)
        frame = (frame + 1) % 3
    for x in range(780,20,-3):
        draw(Treainer_runnig[0] + Treainer_runnig[2] * frame,Treainer_runnig[1] - Treainer_runnig[3],Treainer_runnig[2],Treainer_runnig[3],x,570,0.03)
        frame = (frame + 1) % 3
    for y in range(570,70,-3):
        draw(Treainer_runnig[0] + Treainer_runnig[2] * frame, Treainer_runnig[1]- Treainer_runnig[3]*2,Treainer_runnig[2] - 1, Treainer_runnig[3], 20, y,0.03)
        frame = (frame + 1) % 3

def ride_rectangle():
    frame = 0
    for x in range(20,780,5):
        draw(11 + 22 * frame,132,22,27,x,70,0.03)
        frame = (frame + 1) %3
    for y in range(70,570,5):
        draw(8 + 19 * frame , 188,19 , 27, 780, y,0.03)
        frame = (frame + 1) % 4
    for x in range(780,20,-5):
        draw(11 + 23 * frame,244,23,27,x,570,0.03)
        frame = (frame + 1) % 3
    for y in range(570,70,-5):
        draw(5 + 19 * frame, 300,20, 26, 19, y,0.03)
        frame = (frame + 1) % 4


while True:
    walk_rectangle()
    run_rectangle()
    ride_rectangle()




close_canvas()
