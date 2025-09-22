import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball Escape Maze')
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

space = pymunk.Space()
space.gravity = (0, 900)

def create_platform(x, y, width, height):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x + width / 2, y + height / 2)
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.elasticity = 0.2
    shape.friction = 1.0
    space.add(body, shape)
    return shape

platform1 = create_platform(50, 550, 700, 20)
platform2 = create_platform(50, 450, 150, 20)
platform3 = create_platform(250, 450, 200, 20)
platform4 = create_platform(500, 450, 250, 20)
platform5 = create_platform(50, 350, 200, 20)
platform6 = create_platform(400, 350, 300, 20)
platform7 = create_platform(50, 250, 150, 20)
platform8 = create_platform(300, 250, 250, 20)
platform9 = create_platform(600, 250, 150, 20)
platform10 = create_platform(50, 150, 100, 20)
platform11 = create_platform(250, 150, 300, 20)
platform12 = create_platform(600, 150, 150, 20)

def create_ball():
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = (70, 520)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.8
    shape.friction = 0.7
    space.add(body, shape)
    return body

ball = create_ball()
exit_rect = pygame.Rect(750, 50, 50, 100)

def draw_message(text, color):
    font = pygame.font.SysFont(None, 60)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        ball.velocity = (ball.velocity.x, -200)
    if keys[pygame.K_LEFT]:
        ball.apply_impulse_at_local_point((-15, 0))
    if keys[pygame.K_RIGHT]:
        ball.apply_impulse_at_local_point((15, 0))

    if ball.position.y > HEIGHT:
        draw_message('Game Over!', RED)

    if exit_rect.collidepoint(ball.position.x, ball.position.y):
        draw_message('You Win!', GREEN)

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, exit_rect)
    space.debug_draw(draw_options)
    space.step(1 / 60)
    pygame.display.flip()
    clock.tick(60)
