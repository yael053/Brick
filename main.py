import pygame

WIDTH, HEIGHT = 610, 610
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BRICK_WIDTH = 50
BRICK_HEIGHT = 20

COLORS = {'PURPLE': (166, 45, 151),
          'LIGHT_BLUE': (0, 128, 255),
          'ORANGE': (255, 128, 0),
          'GREEN': (0, 255, 0),
          'YELLOW': (255, 255, 0)
          }

class Brick:
    width = BRICK_WIDTH
    height = BRICK_HEIGHT


    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    radius = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)


class Player:
    width = 80
    height = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)




def create_bricks(colors):
    bricks = []

    lines = 10
    start_height = 50
    num_bricks_in_line = 9
    space = 9
    edge_space = (WIDTH - (num_bricks_in_line * BRICK_WIDTH + (num_bricks_in_line - 1) * space)) // 2

    colors_lst = [color for color in colors.values()]

    for i in range(lines):
        y = start_height + i * (BRICK_HEIGHT + space)
        for j in range(num_bricks_in_line):
            x = edge_space + j * (BRICK_WIDTH + space)
            bricks.append(Brick(x, y, colors_lst[i % len(colors_lst)]))

    return bricks



clock = pygame.time.Clock()
FPS = 60
def main():
    bricks = create_bricks(COLORS)
    ball = Ball(300, 300)
    while True:
        screen.fill(BLACK)
        ball.draw(screen, WHITE)
        for brick in bricks:
            brick.draw(screen)


        pygame.display.update()

    main()


if __name__ == "__main__":
    main()
