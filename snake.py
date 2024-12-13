import pygame, sys
from pygame import Vector2

from random import randint

class Snake:

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load("graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("graphics/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load("graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("graphics/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("graphics/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("graphics/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load("graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("graphics/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("graphics/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("graphics/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("graphics/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("graphics/body_bl.png").convert_alpha()
    
    # def draw_snake(self):
    #     for index, block in enumerate(self.body):
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
    
    def add_block(self):
        self.new_block = True

class Fruit:

    def __init__(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # draw the rectangle
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("graphics/apple.png").convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)