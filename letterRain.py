import random
import pygame

PANEL_width = 1920       # 设置窗口的宽
PANEL_height = 1080       # 设置窗口的高
FONT_PX = 15             # 设置字体的像素度

pygame.init()

# 创建一个可视窗口（如果想要全屏效果，需要在32前加一个参数，"FULLSCREEN"，并更改宽高设置）
winStr = pygame.display.set_mode((PANEL_width, PANEL_height), pygame.FULLSCREEN, 32)
font = pygame.font.SysFont("SourceCodePro-Black.tff", 25)  # 必须带字体文件
bg_suface = pygame.Surface((PANEL_width, PANEL_height), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 25))  # 颜色及字体的密度
winStr.fill((0, 0, 0))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

texts = [font.render(str(letters[i]), True, (0, 255, 0)) for i in range(62)]

# 按屏幕的宽度计算可以在画板上放几列坐标并生成一个列表
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]

while True:
    # 从队列中获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            chang = pygame.key.get_pressed()
            if(chang[32]):
                exit()
    # 给定暂停毫秒数
    pygame.time.delay(30)

    # 重新编辑图像第二个参数是左上角坐标
    winStr.blit(bg_suface, (0, 0))

    for i in range(len(drops)):
        text = random.choice(texts)

        # 重新编辑每个坐标点的图像
        winStr.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
        drops[i] += 1
        if drops[i] * 10 > PANEL_height or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()