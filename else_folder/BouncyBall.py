import pygame
import random
FPS = 60
screen_width, screen_height = 800, 600

# 定義顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ball():
    def __init__(self,screen, color, radius, pos, velocity, line_width):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.line_width = line_width

    def update_ball(self):
        
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 檢查左右邊界，若碰到則反轉 x 軸速度
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]

        # 檢查上下邊界，若碰到則反轉 y 軸速度
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw_ball(self):
        # add your code here
        pygame.draw.circle(self.screen, self.color, self.pos , self.radius, self.line_width)

def main():
    # add your code here
    pygame.init()
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BouncyBall")
    
    ball1 = Ball(screen, WHITE, 20, [screen_width // 2, screen_height // 2], [random.randrange(-3,3),random.randrange(-3,30)], 10)
    ball2 = Ball(screen, RED, 20, [screen_width // 2 + screen_width // 4, screen_height // 4 + screen_height // 4], [random.randrange(-30,30), random.randrange(-3,3)], 5)

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(BLUE)
        # 更新球的位置及反彈邏輯
        ball1.update_ball()
        ball2.update_ball()
        ball1.draw_ball()
        ball2.draw_ball()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

    

if __name__ == "__main__":
    main()