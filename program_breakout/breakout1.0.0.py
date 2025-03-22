import pygame
import random
# 啟動遊戲 python3 breakout.py
# 初始化 pygame
pygame.init()

# 視窗大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("打磚塊遊戲")

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)

# 遊戲參數
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10
BRICK_WIDTH = 75
BRICK_HEIGHT = 30
ROWS = 5  # 磚塊行數
COLS = 10  # 磚塊列數

# 建立滑板
paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# 建立球
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = -4

# 建立磚塊
bricks = []
for row in range(ROWS):
    for col in range(COLS):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5) , row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# 遊戲迴圈
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 滑板移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(8, 0)

    # 移動球
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 碰到牆壁反彈
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 碰到滑板反彈
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y
        ball.y = paddle.top - BALL_RADIUS * 2  # 讓球浮起來

    # 碰到磚塊
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            break  # 確保一次只破壞一個磚塊

    # 繪製磚塊
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # 繪製滑板
    pygame.draw.rect(screen, BLUE, paddle)

    # 繪製球
    pygame.draw.ellipse(screen, GREEN, ball)

    # 遊戲結束判定
    if ball.bottom >= HEIGHT:
        print("遊戲結束！你輸了！")
        running = False
    elif not bricks:
        print("恭喜！你贏了！")
        running = False

    # 更新畫面
    pygame.display.flip()
    clock.tick(60)  # 控制幀率

pygame.quit()

