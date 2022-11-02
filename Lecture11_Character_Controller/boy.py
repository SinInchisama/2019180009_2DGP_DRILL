from pico2d import *

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            print(self.event_que)
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            print(self.cur_state)
            self.cur_state.enter(self,event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self,event):
        print('add_event')
        self.event_que.insert(0,event)

    def handle_event(self, event):
        if(event.type,event.key) in key_event_table:
            print('handle_event')
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)

class IDLE:
    @staticmethod
    def enter(self,event):
        print('Enter Idle')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('Exit Idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100,300,100,100,self.x,self.y)
        else:
            self.image.clip_draw(self.frame * 100,200,100,100,self.x,self.y)
        pass

class RUN:
    @staticmethod
    def enter(self,event):
        print('Enter Run')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            print('1')
            self.dir -= 1
        elif event == LU:
            print('1')
            self.dir += 1
        else :
            print(event)

    @staticmethod
    def exit(self):
        print('Exit Run')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0,self.x,800)
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass


RD, LD, RU, LU = range(4)

key_event_table = {
    (SDL_KEYDOWN,SDLK_RIGHT) : RD,
    (SDL_KEYDOWN,SDLK_LEFT) : LD,
    (SDL_KEYUP,SDLK_RIGHT) : RU,
    (SDL_KEYUP,SDLK_LEFT) : LU
}

next_state = {
    IDLE: {RU:RUN,LU:RUN,RD:RUN,LD:RUN},
    RUN : {RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE}
}
