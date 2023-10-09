#Создай собственный Шутер!

from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_sped, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (size_x, size_y)) 
        self.speed = pl_sped 
        self.rect = self.image.get_rect()
        self.rect.x = pl_x 
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bull = Bullet('bullet.png', self.rect.centerx, self.rect.top, -10, 10, 30)
        bullets.add(bull)
lost = 0
score=0
class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint (80, win_width-80)
            self.rect.y = 0
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()
win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('Shooter Game')
background = transform.scale(
    image.load('galaxy.jpg'),
    (win_width, win_height)
    )
ship = Player("rocket.png",6,win_height-100,6,65,75)


monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range (1,6):
    monster = Enemy('ufo.png', randint(80, win_width-80),-40, randint(1,5),90,60)
    monsters.add(monster)
for i in range(1,3):
    asteroid = Enemy('asteroid.png',randint(80,620), -40,randint(1,7),80,50)
    asteroids.add(asteroid)
health = 3
font.init()
#font1 = font.SysFont(Arial, 80)
font1 = font.SysFont('Arial', 36)
win = font1.render('YOU WiN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))


mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire1 = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60
run = True
finish = False
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
                fire1.play()
    if not finish:
        window.blit(background,(0,0))
        ship.update()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for c in sprites_list:
            score+=1
            monster = Enemy('ufo.png', randint(80, win_width-80),-40, randint(1,5),90,65)
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >=3:
            finish = True
            window.blit(lose, (200, 200))
        if score>=10:
            finish = True
            window.blit(win, (200, 200))
        if sprite.spritecollide(ship, asteroids, False):
            health -= 1
            sprite.spritecollide(ship, asteroids, True)

        if health == 0:
            finish = True
            window.blit(lose, (200, 200))
        text_score = font1.render('Счёт:'+ str(score),1,(255, 255, 255))
        window.blit(text_score, (10, 20))
        text_lose = font2.render('Пропущено:'+ str(lost),1,(255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_health = font1.render('Жизни:' +str(health),1,(255,255,255))
        window.blit(text_health, (10, 80))
        ship.reset()
        display.update()
    time.delay(50)
#clock.tick(FPS)

