import pygame
import random

pygame.init()

# カラー設定
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# ウィンドウ設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ブロック崩し")

# サウンド
bounce_sound = pygame.mixer.Sound('bounce.wav')

# ボール設定
ball_radius = 15
ball_speed = [4, 4]
ball_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, ball_radius * 2, ball_radius * 2)

# パドル設定
paddle_width, paddle_height = 75, 12
paddle_speed = 7
paddle_rect = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10, paddle_width, paddle_height)

# ブロック設定
block_width, block_height = 60, 25
blocks = [pygame.Rect(x, y, block_width, block_height) for x in range(5, WIDTH, 65) for y in range(5, 150, 30)]

font = pygame.font.Font(None, 36)

running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_rect.left > 0:
            paddle_rect.move_ip(-paddle_speed, 0)
        if keys[pygame.K_RIGHT] and paddle_rect.right < WIDTH:
            paddle_rect.move_ip(paddle_speed, 0)

        ball_rect.move_ip(ball_speed)
        if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
            bounce_sound.play()
        if ball_rect.top <= 0:
            ball_speed[1] = -ball_speed[1]
            bounce_sound.play()
        if ball_rect.bottom >= HEIGHT:
            game_over = True

        if ball_rect.colliderect(paddle_rect):
            ball_speed[1] = -ball_speed[1]
            bounce_sound.play()

        hit_index = ball_rect.collidelist(blocks)
        if hit_index != -1:
            hit_rect = blocks.pop(hit_index)
            ball_speed[1] = -ball_speed[1]
            bounce_sound.play()

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, ball_rect)
    pygame.draw.rect(screen, BLUE, paddle_rect)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

    if game_over:
        if not blocks:
            message = "You Win!"
        else:
            message = "game over!"
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()
