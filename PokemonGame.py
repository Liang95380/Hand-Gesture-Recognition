import pygame
import os
import neat
import time
import random
import pyautogui
import clock

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)


# Window Size
WIN_WIDTH = 500
WIN_HEIGHT = 700


# Import Images
pic = pygame.image.load(os.path.join("imgs", "piplup.png"))
PIPLUP_IMGS = pygame.transform.scale(pic, (70, 50))
pic2 = pygame.image.load(os.path.join("imgs", "bg.jpg"))
BG_IMGS = pygame.transform.scale(pic2, (500, 800))
pic3 = pygame.image.load(os.path.join("imgs", "charmander.png"))
CHARMANDER_IMG = pygame.transform.scale(pic3, (88, 68))
pic4 = pygame.image.load(os.path.join("imgs", "fire.png"))
FIRE_IMG = pygame.transform.scale(pic4, (100, 70))

class Piplup:

    IMG = PIPLUP_IMGS

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

    def move(self, dir):
        if self.x != 100:
            if dir == "left":
                self.move_left()
        if self.x != 300:
            if dir == "right":
                self.move_right()

    def move_left(self):
        self.vel = 100
        self.x = self.x - self.vel

    def move_right(self):
        self.vel = 100
        self.x = self.x + self.vel

    def get_mask(self):  # To get mask of the bird for collision
        return pygame.mask.from_surface(self.IMG)


class Enemy:

    IMG = CHARMANDER_IMG

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movement = 0

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))


class Projectile:

    IMG = FIRE_IMG

    def __init__(self, x):
        self.vel = 0
        self.x = x
        self.y = 100
        self.vel = 5
        self.passed = False

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

    def move(self):
        self.y += self.vel

    def collide(self, piplup):
        piplup_mask = piplup.get_mask()
        projectile_mask = pygame.mask.from_surface(self.IMG)

        offset = (self.x - piplup.x, self.y - round(piplup.y))

        point = piplup_mask.overlap(projectile_mask, offset)  # Return True if overlapped

        if point:
            return True

        return False



def draw_window(win, piplup, charmander, projectiles, score):
    win.blit(BG_IMGS, (0, -20))
    piplup.draw(win)
    charmander.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score), 1, (255,255,  0))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    for projectile in projectiles:
        projectile.draw(win)

    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    positions = [100, 200, 300]

    score = 0

    clock = pygame.time.Clock()

    piplup = Piplup(200, 560)
    random1 = random.choice(positions)

    charmander = Enemy(random1, 60)
    projectiles = [Projectile(random1)]

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  # sys.exit() if sys is imported
                quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if piplup.x != 100:
                        piplup.move_left()

                elif event.key == pygame.K_RIGHT:
                    if piplup.x != 300:
                        piplup.move_right()

        # To check whether the fire hit penguin
        for projectile in projectiles:

            if projectile.passed is False and projectile.y + projectile.IMG.get_height() > 560:
                projectile.passed = True
                random2 = random.choice(positions)
                projectiles.append(Projectile(random2))
                charmander.x = random2

                score += 1

            if projectile.collide(piplup):
                print("Die")
                score = 0

            projectile.move()

        if projectile.passed:
            projectiles.append(Projectile(random.randrange(0, 320)))




        clock.tick(30)
        draw_window(win, piplup, charmander, projectiles, score)


main()
