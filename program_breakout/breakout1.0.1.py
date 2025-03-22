import pygame
import random

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
        brick = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# 遊戲選項
sync_paddle_and_ball = False
score = 0

# 開始界面函數
def start_screen(final_score=None):
    global sync_paddle_and_ball
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    while True:
        screen.fill(BLACK)

        # 標題
        title_text = font.render("breakout", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # 顯示分數（如果有）
        if final_score is not None:
            score_text = small_font.render(f"Your score: {final_score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))

        # 選項
        sync_text = small_font.render(f"sync ball and paddle: {'Yes' if sync_paddle_and_ball else 'No'} (press s to switch)", True, WHITE)
        screen.blit(sync_text, (WIDTH // 2 - sync_text.get_width() // 2, 300))

        # 開始按鈕
        start_text = small_font.render("press enter to start the game", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    sync_paddle_and_ball = not sync_paddle_and_ball
                elif event.key == pygame.K_RETURN:
                    return

# 遊戲迴圈
while True:
    start_screen(final_score=score if 'score' in locals() else None)

    # 初始化遊戲狀態
    paddle = pygame.Rect(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed_x = 4 * random.choice((1, -1))
    ball_speed_y = -4
    bricks = []
    for row in range(ROWS):
        for col in range(COLS):
            brick = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick)
    score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 滑板移動
        if sync_paddle_and_ball:
            paddle.centerx = ball.centerx
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle.left > 0:
                paddle.move_ip(-8, 0)
            if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
                paddle.move_ip(8, 0)

        # 移動球
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # 碰到牆壁反彈
        if ball.left <= 0:
            ball_speed_x = abs(ball_speed_x)
        elif ball.right >= WIDTH:
            ball_speed_x = -abs(ball_speed_x)
        if ball.top <= 0:
            ball_speed_y = abs(ball_speed_y)

        # 碰到滑板反彈
        if ball.colliderect(paddle) and ball_speed_y > 0:
            ball.y = paddle.top - BALL_RADIUS * 2  # 讓球浮起來
            hit_pos = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH // 2)  # 計算擊中位置 (-1 ~ 1)
            ball_speed_x = hit_pos * 5  # 根據擊中位置改變橫向速度
            ball_speed_y = -abs(ball_speed_y)  # 讓球向上反彈

        # 碰到磚塊
        for brick in bricks[:]:
            if ball.colliderect(brick):
                # 計算碰撞區域
                overlap_left = abs(ball.right - brick.left)
                overlap_right = abs(ball.left - brick.right)
                overlap_top = abs(ball.bottom - brick.top)
                overlap_bottom = abs(ball.top - brick.bottom)

                # 判斷碰撞方向
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                if min_overlap == overlap_left:
                    ball_speed_x = -abs(ball_speed_x)  # 從左側碰撞，反轉 x 軸速度
                elif min_overlap == overlap_right:
                    ball_speed_x = abs(ball_speed_x)  # 從右側碰撞，反轉 x 軸速度
                elif min_overlap == overlap_top:
                    ball_speed_y = -abs(ball_speed_y)  # 從頂部碰撞，反轉 y 軸速度
                elif min_overlap == overlap_bottom:
                    ball_speed_y = abs(ball_speed_y)  # 從底部碰撞，反轉 y 軸速度

                bricks.remove(brick)
                score += 10  # 每破壞一個磚塊加 10 分
                break  # 確保一次只破壞一個磚塊

        # 防止球速過慢
        if abs(ball_speed_x) < 1:
            ball_speed_x = 1 * random.choice((1, -1))

        # 繪製磚塊
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        # 繪製滑板
        pygame.draw.rect(screen, BLUE, paddle)

        # 繪製球
        pygame.draw.ellipse(screen, GREEN, ball)

        # 繪製分數
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # 遊戲結束判定
        if ball.bottom >= HEIGHT:
            print("Lose")
            running = False
        elif not bricks:
            print("Win")
            running = False

        # 更新畫面
        pygame.display.flip()
        clock.tick(60)  # 控制幀率