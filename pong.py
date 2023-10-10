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
WINNING_SCORE = 10


class Paddel:
    COLOR = WHITE
    VEL = 10

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
    MAX_VEL = 5


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

    def reset(self):
        if (self.x < 0) or (self.x > WIDTH):
            self.x = WIDTH//2
            self.y = HEIGHT//2
            self.x_vel *= -1
            self.y_vel = random.randint(-7,7)
        



        

def draw(win, paddles, ball, Left_Score, Right_Score ):
    win.fill(BLACK)

    Player1_score_text = SCORE_FONT.render(f"{Left_Score}",1,WHITE)
    Player2_score_text = SCORE_FONT.render(f"{Right_Score}",1,WHITE)
    win.blit(Player1_score_text, (WIDTH//4 - Player1_score_text.get_width()//2, 20))
    win.blit(Player2_score_text, (WIDTH - WIDTH//4 - Player2_score_text.get_width()//2, 20))
    

    for paddle in paddles:
        paddle.draw_p(win)

    for i in range(10,HEIGHT,HEIGHT//20):
        if i % 2 ==1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2-5, i, 10, HEIGHT//20))

    ball.draw_b(win)

    pygame.display.flip()


def handle_collision(ball,left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1
                ball.y_vel += random.randint(-3,3)
    
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1
                ball.y_vel += random.randint(-3,3)


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and (left_paddle.y - left_paddle.VEL) >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and (left_paddle.y + left_paddle.VEL + left_paddle.height) <= HEIGHT:
        left_paddle.move(up=False)
        
    if keys[pygame.K_KP5] and (right_paddle.y - right_paddle.VEL) >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_KP2] and (right_paddle.y - right_paddle.VEL + right_paddle.height) <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddel(10,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddel(WIDTH - 10 - PADDLE_WIDTH,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    Left_Score = 0
    Right_Score = 0

    
    ball = Ball(WIDTH//2,HEIGHT//2,BALL_RADIUS)

    while run:
        clock.tick(FPS)

        if ball.x  < 0:
            Right_Score += 1
            ball.reset()
        elif ball.x  > WIDTH:
            Left_Score += 1 
            ball.reset()

        if Left_Score >= WINNING_SCORE:
            pass
        elif Right_Score >= WINNING_SCORE:
            pass

        draw(WIN, [left_paddle, right_paddle], ball, Left_Score, Right_Score) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break   

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball,left_paddle,right_paddle)

    pygame.quit()

if __name__ == "__main__":
    main()
