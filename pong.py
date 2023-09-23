import pygame
import random

pygame.init()


WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS = 60
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
WHITE = (255,255,255)
BLACK = (0,0,0)
BALL_RADIUS = 8
SCORE_FONT = pygame.font.SysFont(name="Arial", size=50)
Player1_Score = 0
Player2_Score = 0

class Paddel:
    COLOR = WHITE
    VEL = 5
    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_p(self, win):
        pygame.draw.rect(win,self.COLOR,(self.x, self.y, self.width, self.height))
    
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        elif not up:
            self.y += self.VEL


class Ball:
    COLOR = WHITE
    MAX_VEL = 7

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = self.MAX_VEL - random.randint(0,7)

    def draw_b(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.radius)

    def move(self,x=True,y=True):
        self.x += self.x_vel
        self.y += self.y_vel

        

def draw(win, paddles,ball, p1_score, p2_score):
    win.fill(BLACK)

    Player1_score_text = SCORE_FONT.render(f'{p1_score}',1,WHITE)
    Player2_score_text = SCORE_FONT.render(f'{p2_score}',1,WHITE)
    win.blit(Player1_score_text, (WIDTH//4 - Player1_score_text.get_width()//2, 20))
    win.blit(Player2_score_text, (WIDTH - WIDTH//4 - Player2_score_text.get_width()//2, 20))
    

    for paddle in paddles:
        paddle.draw_p(win)

    for i in range(10,HEIGHT,HEIGHT//20):
        if i % 2 ==1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2-5, i, 10, HEIGHT//20))

    ball.draw_b(win)

    pygame.display.update()


def handle_collision(ball,left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                ball.y_vel = ball.MAX_VEL - random.randint(0,7)
    
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                ball.y_vel = ball.MAX_VEL - random.randint(0,7)

def ball_reset(ball):
    if (ball.x  - ball.radius <= 0) or (ball.x + ball.radius >= WIDTH):
        ball.x = WIDTH//2
        ball.y = HEIGHT//2
        ball.x_vel *= -1
        ball.y_vel = ball.MAX_VEL - random.randint(0,7)
        if ball.x  - ball.radius <= 0:
            Player2_Score += 1
        elif ball.x  + ball.radius >= WIDTH:
            Player1_Score += 1





def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and (left_paddle.y - left_paddle.VEL) >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and (left_paddle.y + left_paddle.VEL + left_paddle.height) <= HEIGHT:
        left_paddle.move(up=False)
        
    if keys[pygame.K_UP] and (right_paddle.y - right_paddle.VEL) >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and (right_paddle.y - right_paddle.VEL + right_paddle.height) <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddel(15,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddel(WIDTH - 15 - PADDLE_WIDTH,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    

    
    ball = Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, Player1_Score, Player2_Score) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

                   

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball,left_paddle,right_paddle)
        ball_reset(ball)


    pygame.quit()

if __name__ == "__main__":
    main()
