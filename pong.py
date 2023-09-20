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
#player_pos = pygame.Vector2(30, screen.get_height() / 2)

class Paddel:
    COLOR = WHITE
    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_p(self, win):
        pygame.draw.rect(win,self.COLOR,(self.x, self.y, self.width, self.height))


def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw_p(win)

    pygame.display.update



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

                   

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_pos.y -= 300 * dt
        # if keys[pygame.K_s]:
        #     player_pos.y += 300 * dt
        # if keys[pygame.K_a]:
        #     player_pos.x -= 300 * dt
        # if keys[pygame.K_d]:
        #     player_pos.x += 300 * dt

    pygame.quit()

if __name__ == "__main__":
    main()
