from pygame import *
from random import randint
import sys

misses = 1

def game():
    killing = 0
    kd = 1.0
    def showEndWindow(window, message):
        clock = time.Clock()

        font.init()
        text = font.Font(None, 70).render(message, True, (255, 255, 255))
        while True:
            # обробка подій
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()

            #рендер
            window.blit(text, (250, 250))
            display.update()
            clock.tick(60)

    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            super().__init__()
            self.speed = speed
            self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
            self.rect = self.player_image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))

    class Hero(GameSprite):
        def __init__(self, player_image, x, y, speed, size_w, size_h):
            super().__init__(player_image, x, y, speed, size_w, size_h)
            self.bullets = []

        def update(self):
            keys = key.get_pressed()
            if keys[K_a]:
                self.rect.x -= self.speed
            if keys[K_d]:
                self.rect.x += self.speed
            for bullet in self.bullets:
                bullet.update()
            if keys[K_w]:
                self.rect.y -= self.speed
            if keys[K_s]:
                self.rect.y += self.speed


        def draw(self, screen):
            screen.blit(self.player_image, (self.rect.x, self.rect.y))
            for bullet in self.bullets:
                bullet.draw(screen)

    class Bullet(GameSprite):
        def update(self):
            self.rect.y -= self.speed


    class Enemy(GameSprite):
        def update(self):
            global misses
            self.rect.y += self.speed
            if self.rect.y > 550:
                self.rect.y = -100
                self.rect.x = randint(0, 500)
                misses +=1






    monsters =[]
    # mixer.init()
    # mixer.music.load(name_of_music)
    # mixer.music.play
    # shootSound = mixer.Sound(name_of_shoot)
    y = 0
    x= 0
    for i in range(5):
        monsters.append(Enemy("error.png", randint(0, 700), y, 2, 50, 50), )
        y -= 50

    rocket = Hero("android.png", 250, 400, 4, 60, 70)
    window = display.set_mode((700, 500))
    clock = time.Clock()
    background = transform.scale(image.load("back.jpeg"), (700, 500))

    font.init()

    font1 = font.Font(None,20)

    while True:
        #обробка подій
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    rocket.bullets.append(Bullet("bullet.png", rocket.rect.centerx, rocket.rect.y, 10, 5, 10))
                    # mixer.music.load(shootSound)
                    # shootSound.play()
        # оновлення обєктів

        for mon in monsters:
            mon.update()
        rocket.update()

        kd =round(killing/misses , 2)
        text = font1.render("Missing: "+ str(misses), False ,(255,255,255))
        text2 = font1.render("Kill: "+ str(killing), False ,(255,255,255))
        text3 = font1.render("K/D:" + str(kd), False ,(255,255,255))

        # відмалювати
        window.blit(background, (0, 0))
        window.blit(text,[20,40])
        window.blit(text2, [20,70])
        window.blit(text3, [20,90])
        for mon in monsters:
            mon.draw(window)

        for mon in monsters:
            for bullet in rocket.bullets:
                if bullet.rect.colliderect(mon.rect):
                    mon.rect.x = randint(0, 500)
                    mon.rect.y = -100
                    rocket.bullets.remove(bullet)
                    killing += 1
                    break

        for mon in monsters:
            if mon.rect.colliderect(rocket.rect):
                showEndWindow(window , "You loser")


        if killing == 200:
            showEndWindow(window, "You Win, Ha Ha")
        rocket.draw(window)
        display.update()
        clock.tick(60)