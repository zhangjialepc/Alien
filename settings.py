class Settings():
    '''存储外星人所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(255,255,255)

        #飞船的速度设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 60,60,60

        #外星人设置
        self.fleet_drop_speed = 20

        #加速
        self.speedup_scale = 1.2
        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed_factor = 1.8
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        #计分
        self.alien_points = 10

        #fleet_direction为1表示向右，为-1表示向左移
        self.fleet_directions = 1

    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points *self.score_scale)
        #print(self.alien_points)