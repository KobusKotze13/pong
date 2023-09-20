import pygame
pygame.init


WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS = 60
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
WHITE = (255,255,255)
BLACK = (0,0,0)


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


class ball:
    COLOR = WHITE
    

def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw_p(win)

    pygame.display.update()


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

    left_paddle = Paddel(30,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddel(WIDTH - 30 - PADDLE_WIDTH,(HEIGHT//2) - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle]) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

                   

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)


    pygame.quit()

if __name__ == "__main__":
    main()
