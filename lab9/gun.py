import math
from random import choice
from random import randint as rnd
import pygame

FPS = 30
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy += gt
        self.x += self.vx
        self.y -= self.vy
        if self.x <= 0:
            self.x = 0
            self.vx = -self.vx
        elif self.x + 2 * self.r >= WIDTH:
            self.x = WIDTH - 2 * self.r - 1
            self.vx = -self.vx
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        elif self.y > HEIGHT:
            balls.pop()

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 <= (obj.r + self.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK

    def draw(self):
        # FIXIT don't know how to do it
        pygame.draw.rect(screen, BLUE, (20,470, 50, 50))
        pygame.draw.rect(screen, self.color, (20,460,20,10))
        pygame.draw.polygon(screen, self.color, [(20, 460), (20+30 * math.cos(self.an), 
                            460 + 30 * math.sin(self.an))], 6)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = BLACK


class Target:
    def __init__(self):
     self.points = 0
     self.live = 1
     #FIXME: don't work!!! How to call this functions when object is created?
     self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 760)
        self.vx = rnd(1,6)
        y = self.y = rnd(300, 530)
        self.vy = rnd(1,6)
        r = self.r = rnd(2, 50)
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.r <= 0:
            self.vx = -self.vx
        elif self.x + self.r >= WIDTH:
            self.vx = -self.vx
        if self.y - self.r < 0:
            self.vy = -self.vy
        elif self.y + self.r>= HEIGHT:
            self.vy = -self.vy
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

        
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
gt = -1
SCORE = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target()
target_2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    text = pygame.font.Font(None, 36)
    text_1 = text.render(('SCORE: ' + str(SCORE)), True, MAGENTA)
    screen.blit(text_1, (100, 50))
    pygame.display.update()
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1 = Target()
            balls.remove(b)
            SCORE += 1
    for b in balls:
        b.move()
        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2 = Target()
            balls.remove(b)
            SCORE += 1

    gun.power_up()

pygame.quit()