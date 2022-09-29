from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 600

def keydowncheck(event):
    global movex, movey
    global framey
    global running
    if event.key == SDLK_LEFT:
        movex -= 1
        framey = 0
    elif event.key == SDLK_RIGHT:
        movex += 1
        framey = 1
    elif event.key == SDLK_UP:
        movey += 1
    elif event.key == SDLK_DOWN:
        movey -= 1
    elif event.key == SDLK_ESCAPE:
        running = False

def keyupcheck(event):
    global movex, movey
    global framey
    if event.key == SDLK_LEFT:
        movex += 1
        framey = 2
    elif event.key == SDLK_RIGHT:
        movex -= 1
        framey = 3
    elif event.key == SDLK_UP:
        movey -= 1
    elif event.key == SDLK_DOWN:
        movey += 1

def handle_events():
    global running
    global framey
    global movex,movey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            keydowncheck(event)

        elif event.type == SDL_KEYUP:
            keyupcheck(event)
    pass

def move_Character():
    global x,y
    if (30 < x + movex * 5 < 1250):
        x += movex * 5
    if (30 < y + movey * 5 < 570):
        y += movey * 5
    delay(0.02)



open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y,movex,movey = TUK_WIDTH // 2, 30,0,0
framex,framey = 0,3

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(framex * 100, 100 * framey, 100, 100, x, y)
    update_canvas()

    framex = (framex + 1) % 8

    move_Character()

    handle_events()

close_canvas()