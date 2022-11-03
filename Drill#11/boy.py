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

        if self.event_que:          #que에 이벤트가 들어가있다면
            event = self.event_que.pop()    # 이벤트를 입력받는다
            self.cur_state.exit(self)       # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 계산
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
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print('Exit Idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:  # 시간이 경과하면,
            # 이벤트를 발생시켜줘야한다. TIMER
            # self.event_que.insert(0,TIMER) # 객체지향프로그래밍 위배, q를 직접 액세스하고 있으니까
            self.add_event(TIMER)  # 객체지향적인 방법
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100,300,100,100,self.x,self.y)
        else:
            self.image.clip_draw(self.frame * 100,200,100,100,self.x,self.y)
        pass

class SLEEP:
    @staticmethod
    def enter(self,event):
        print('Enter SLEEP')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('Exit SLEEP')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,3.141592/2,'', self.x -25, self.y - 25,100,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,3.141592/2,'v', self.x + 25, self.y - 25,100,100)
        pass
class RUN:
    @staticmethod
    def enter(self,event):
        print('Enter Run')
        if event == RD:         # dir = IDLE에서 나올 때 무슨 키를 눌렀는지에 따라 결정됨.
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1


    @staticmethod
    def exit(self):
        print('Exit Run')
        self.face_dir = self.dir # run을 나가서, Idle로 갈때 얼굴 방향을 알려줄 필요가 있다.
        self.dir = 0
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

class AUTO_RUN:
    @staticmethod
    def enter(self,event):
        print('Enter AUTO Run')
        self.dir = self.face_dir


    @staticmethod
    def exit(self):
        print('Exit AUTO Run')
        self.face_dir = self.dir # run을 나가서, Idle로 갈때 얼굴 방향을 알려줄 필요가 있다.
        self.dir = 0
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if(self.x >= 750):
            self.dir = -1
        elif(self.x<= 50):
            self.dir = 1
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+40,200,200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+40,200,200)
        pass


RD, LD, RU, LU,TIMER,AD = range(6)

key_event_table = {
    (SDL_KEYDOWN,SDLK_RIGHT) : RD,
    (SDL_KEYDOWN,SDLK_LEFT) : LD,
    (SDL_KEYUP,SDLK_RIGHT) : RU,
    (SDL_KEYUP,SDLK_LEFT) : LU,
    (SDL_KEYDOWN,SDLK_a) : AD
}

next_state = {
    SLEEP : {RD:RUN,LD:RUN,RU: RUN,LU:RUN,SLEEP : SLEEP,AD:SLEEP},
    IDLE: {RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER : SLEEP,AD:AUTO_RUN},
    RUN : {RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,AD:AUTO_RUN},
    AUTO_RUN:{RU:RUN,LU:RUN,RD:RUN,LD:RUN,AD : IDLE}
}

