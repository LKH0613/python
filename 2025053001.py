'''#수업
import sys
import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time. Clock()

light_img = pygame.image.load("light.png")

l_x = []
l_y = []

cnt = 0

man_img = pygame.image.load('man.png')

m_x, m_y = 250, 480

sysfont = pygame.font.SysFont(None, 72)

game_over = False

l_size = light_img.get_size()
m_size = man_img.get_size()

while True:
    SCREEN.fill((0, 0, 0))
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_over:
        break

    for i in range(len(l_x)):
        if l_x[i] + l_size[0] >= m_x and m_x + m_size[0] >= l_x[i]:
            if l_y[i] -l_size[1] >= m_y:
                msg = sysfont.render("Game Over!", True, (255, 0, 0))
                SCREEN.blit(msg, (160, 250))
                game_over = True
            
    cnt += 1
    if cnt >= 20:
        cnt = 0
        l_x.append(random.randint(0, 600))
        l_y.append(0)

    for i in range(len(l_x)):
        l_y[i] += 5

        SCREEN.blit(light_img, (l_x[i], l_y[i]))

        if l_y[i] >= 550:
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
            break

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        if m_x > 0 :
            m_x -= 5
            
    if key_event[pygame.K_RIGHT]:
        if m_x > 0 :
            m_x += 5

    SCREEN.blit(man_img, (m_x, m_y))
    
    pygame.display.update()
    CLOCK.tick(60)
    
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
'''
import pygame
import sys
import math
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("좀비 슈팅 게임 - 다양한 적 종류")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
PURPLE = (160, 32, 240)
GRAY = (120, 120, 120)
BLUE = (0, 100, 255)

# 플레이어 설정
player_size = 40
player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
player_speed = 5

# 총알 설정
bullets = []
bullet_speed = 10

# 점수 및 글꼴
score = 0
font = pygame.font.SysFont(None, 36)

# 방향 각도 계산 함수
def angle_to(target, source):
    dx, dy = target[0] - source[0], target[1] - source[1]
    return math.atan2(dy, dx)

# 좀비 클래스
class Zombie:
    def __init__(self, zombie_type="normal"):
        self.pos = pygame.Vector2(random.randint(0, WIDTH), random.choice([-50, HEIGHT + 50]))
        self.type = zombie_type
        self.zigzag_direction = 1
        self.zigzag_timer = 0
        self.charge_state = 0  # 0: 준비, 1: 돌진 중, 2: 쿨타임
        self.charge_speed = 0
        self.health = 1
        self.score_value = 10
        self.size = 30
        self.color = GREEN

        if self.type == "normal":
            self.speed = random.uniform(1.5, 2.5)
            self.color = GREEN
            self.health = 1
            self.score_value = 10
            self.size = 30
        elif self.type == "fast":
            self.speed = random.uniform(3.5, 4.5)
            self.color = PURPLE
            self.health = 1
            self.score_value = 15
            self.size = 25
        elif self.type == "tank":
            self.speed = 1.0
            self.color = GRAY
            self.health = 3
            self.score_value = 30
            self.size = 40
        elif self.type == "zigzag":
            self.speed = 2.5
            self.color = BLUE
            self.health = 1
            self.score_value = 25
            self.size = 28
        elif self.type == "charger":
            self.speed = 1.5
            self.color = RED
            self.health = 2
            self.score_value = 40
            self.size = 35
            self.charge_state = 0
            self.charge_speed = 0

    def move(self, target_pos):
        if self.type == "zigzag":
            self.zigzag_timer += 1
            if self.zigzag_timer > 30:
                self.zigzag_direction *= -1
                self.zigzag_timer = 0
            base_dir = (target_pos - self.pos).normalize()
            perpendicular = pygame.Vector2(-base_dir.y, base_dir.x) * self.zigzag_direction * 1.5
            move_vec = base_dir * self.speed + perpendicular
            self.pos += move_vec
        elif self.type == "charger":
            if self.charge_state == 0:
                direction = (target_pos - self.pos).normalize()
                self.pos += direction * self.speed * 0.5
                if self.pos.distance_to(target_pos) < 200:
                    self.charge_state = 1
                    self.charge_speed = 12
                    self.charge_dir = (target_pos - self.pos).normalize()
            elif self.charge_state == 1:
                self.pos += self.charge_dir * self.charge_speed
                self.charge_speed *= 0.95
                if self.charge_speed < 1:
                    self.charge_state = 2
                    self.charge_cooldown = 60
            elif self.charge_state == 2:
                self.charge_cooldown -= 1
                if self.charge_cooldown <= 0:
                    self.charge_state = 0
        else:
            if target_pos != self.pos:
                direction = (target_pos - self.pos).normalize()
                self.pos += direction * self.speed

# 좀비 스폰 관리
zombies = []
spawn_timer = 0
spawn_interval = 90

# 게임 루프
running = True
while running:
    dt = clock.tick(60)
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            angle = angle_to((mx, my), player_pos)
            bullet_dir = pygame.Vector2(math.cos(angle), math.sin(angle))
            bullets.append([player_pos.copy(), bullet_dir])

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_pos.y -= player_speed
    if keys[pygame.K_s]: player_pos.y += player_speed
    if keys[pygame.K_a]: player_pos.x -= player_speed
    if keys[pygame.K_d]: player_pos.x += player_speed

    # 총알 이동
    for bullet in bullets[:]:
        bullet[0] += bullet[1] * bullet_speed
        if not (0 <= bullet[0].x <= WIDTH and 0 <= bullet[0].y <= HEIGHT):
            bullets.remove(bullet)

    # 좀비 스폰
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        spawn_timer = 0
        z_type = random.choices(
            ["normal", "fast", "tank", "exploder", "zigzag", "charger"],
            weights=[50, 20, 10, 8, 7, 5]
        )[0]
        zombies.append(Zombie(z_type))

    # 좀비 처리
    for zombie in zombies[:]:
        zombie.move(player_pos)

        if zombie.pos.distance_to(player_pos) < (zombie.size + player_size) // 2:
            print("Game Over! Score:", score)
            running = False

        for bullet in bullets[:]:
            if zombie.pos.distance_to(bullet[0]) < zombie.size:
                bullets.remove(bullet)
                zombie.health -= 1
                if zombie.health <= 0:
                    if zombie.type == "exploder":
                        explosion(zombie, zombies)
                    zombies.remove(zombie)
                    score += zombie.score_value
                break

    # 총알 그리기
    for bullet in bullets:
        pygame.draw.circle(screen, YELLOW, bullet[0], 5)

    # 좀비 그리기
    for zombie in zombies:
        pygame.draw.circle(screen, zombie.color, (int(zombie.pos.x), int(zombie.pos.y)), zombie.size)

    # 플레이어 그리기
    pygame.draw.circle(screen, RED, (int(player_pos.x), int(player_pos.y)), player_size // 2)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()


