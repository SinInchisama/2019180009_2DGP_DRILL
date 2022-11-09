from pico2d import*
from random import randint
import game_framework

PIXEL_PER_METER = (10.0 / 0.2) # 10픽셀 당 20cm
FLIGHT_SPEED_KMPH = 30.0 # Km / Hour 새의 평속
FLIGHT_SPEED_MPM = (FLIGHT_SPEED_KMPH * 1000.0 / 60.0)     # 시간당 가는 km를 분당 m로 바꿈
FLIGHT_SPEED_MPS = (FLIGHT_SPEED_MPM / 60.0)              # 분당m를 초당으로 바꿈
FLIGHT_SPEED_PPS = (FLIGHT_SPEED_MPS * PIXEL_PER_METER)   # m를 픽셀당 cm로 바꿈

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class bird():
    image = None

    def __init__(self):
        self.x = randint(0,800)
        self.y = randint(200,500)
        self.dir = 1
        self.frame = float(randint(0,14))

        if(bird.image == None):
            bird.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir * FLIGHT_SPEED_PPS * game_framework.frame_time
        self.frame =  (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if(self.x>= 770 and self.dir == 1):
            self.dir = -1
        elif(self.x<=30 and self.dir == -1):
            self.dir = 1

        pass

    def draw(self):
        if(self.dir == 1):
            self.image.clip_composite_draw(int(self.frame) % 5*183,338 - (int(self.frame) //5 * 168),183,168,0,'',self.x,self.y,91,73)
            pass
        else:
            self.image.clip_composite_draw(int(self.frame) % 5*183, 338- (int(self.frame) //5 * 168), 183, 168, 0, 'h', self.x, self.y,91,73)
            pass

    def handle_event(self):
        pass


