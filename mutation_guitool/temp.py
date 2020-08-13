import pygame
import sys

clock = pygame.time.Clock()
fps = 1
bg = [255, 255, 255]
screen_size = (1200,700)
yet_start = True
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

class rectangle():
    def __init__(self, rect, color):
        self.button = pygame.Rect(rect)
        self.color = color
        # self.time = time
        # self.delay = delay
        # self.show = False
    def draw_rect(self, screen):
        pygame.draw.rect(screen,self.color,self.button)

class game():
    yet_start = True
    Not_cho_diff = True
    GameLevel = 0
    # 宣告四個長方形當作難度選項按鈕
    Hard_1_BT = rectangle((100, 300, 50, 50),RED)
    Hard_2_BT = rectangle((100, 400, 50, 50),RED)
    Hard_3_BT = rectangle((100, 500, 50, 50),RED)
    Hard_4_BT = rectangle((100, 600, 50, 50),RED)

    #專門顯示文字的方法，除了顯示文字還能指定顯示的位置
    def show_text(self, text, x, y):
        self.x = x
        self.y = y
        text = game.font.render(text, True, (0, 0, 0))
        game.screen.blit(text, (self.x, self.y))
        pygame.display.update()
    #初始化pygame的畫面及設定
    def init_screen(self):
        pygame.init()
        game.screen = pygame.display.set_mode(screen_size ,0 ,32)
        game.font = pygame.font.Font("font/微軟正黑體-1.ttf", 24) #指定字型位置及字形大小
        game.screen.fill(bg)
    def strat_menu(self):
        game.screen.fill(bg)
        self.show_text("請按任意件開始", 100, 100)
        while yet_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    return False
                

    #選擇題目難度
    def cho_diff(self):
        pygame.time.wait(100)
        game.screen.fill(bg)
        self.show_text("歡迎來到變異測試小遊戲", 100, 100)
        self.show_text("請選擇想要遊玩的難度", 100, 200)
        # 畫出選項
        self.Hard_1_BT.draw_rect(self.screen)
        self.Hard_2_BT.draw_rect(self.screen)
        self.Hard_3_BT.draw_rect(self.screen)
        self.Hard_4_BT.draw_rect(self.screen)
        pygame.display.update()
        while self.Not_cho_diff:
            for event in pygame.event.get():
                if event.type ==pygame.MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    if self.Hard_1_BT.button.collidepoint(mouse):
                        self.Not_cho_diff = False
                        return 1
                    if self.Hard_2_BT.button.collidepoint(mouse):
                        self.Not_cho_diff = False
                        return 2                  
                    if self.Hard_3_BT.button.collidepoint(mouse):
                        self.Not_cho_diff = False
                        return 3
                    if self.Hard_4_BT.button.collidepoint(mouse):
                        self.Not_cho_diff = False
                        return 4
    def start(self, GameLevel):
        game.screen.fill(bg)
        self.show_text("歡迎來到等級" + str(GameLevel) + "的關卡!", 100, 100)
        self.show_text("以下為本次變異測試的題目", 100, 200)
        self.show_text("請寫出能夠殺死所有變異程式的驗證程式以通過關卡", 100, 300)
        pygame.time.wait(10000)

    def game_start(self):
        print('into')
        self.init_screen()

        while True:
            #初始畫面
            
            if self.yet_start:
                self.yet_start = self.strat_menu()
            #選擇遊戲難度，條件為還沒選跟已離開初始畫面
            if self.yet_start == False and self.Not_cho_diff == True:
                self.GameLevel = self.cho_diff()
            if self.GameLevel != 0:
                self.start(self.GameLevel)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.update()
            # pygame.time.wait(1000)
            # print("pass")
            clock.tick(fps)
            

if __name__=='__main__':
    mangame = game()
    mangame.game_start()