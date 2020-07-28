import pygame
import sys

def show_text(text, x, y):#專門顯示文字的方法，除了顯示文字還能指定顯示的位置
    x = x
    y = y
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (x, y))
    pygame.display.update()

# def start_menu():

def game_start(diffculty = 0):

    background_image_filename = '73804930_p0.png'
    mouse_image_filename = 'mapel.png'

    screen.fill(bg)
    show_text("難度:" + str(diffculty) + "的關卡",100,100)
    global gameover 
    gameover = True
    #遊戲主循環
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #觸發事件後退出
                exit()

        pygame.display.update()

def choose_diff():
    # screen.fill(bg)
    text = "請選擇遊戲難度"
    button = pygame.Rect(200, 200, 100, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    # return 4

        screen.fill(bg)
        show_text(text,100, 100)
        pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
        pygame.display.update()
        clock.tick(fps)

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         return 4
clock = pygame.time.Clock()
fps = 60
bg = [255, 255, 255]
#初始化pygame
pygame.init()
screen_size = (600,600)
#創建一個窗口
screen = pygame.display.set_mode(screen_size, 0, 32)
font = pygame.font.Font("font/微軟正黑體-1.ttf", 24) #指定字型位置及字形大小
screen.fill(bg)

text = "歡迎來到變異測試遊戲間按任意鍵進入遊戲"
show_text(text,100, 100)
pygame.display.update()
flag = True

while flag:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            flag = False


ch = choose_diff()
game_start(ch)

