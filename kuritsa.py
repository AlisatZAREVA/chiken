from pygame import *

win_width = 600
win_height = 500
FPS = 60
clock = time.Clock()
window = display.set_mode((win_width, win_height))
display.set_caption('kuritsa')
background = transform.scale(image.load('i.jpg'),(win_width, win_height))
run = True

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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


chik =GameSprite('chik.jpg',200,200,10,60,60)
egg = Player('egg.png', 0,200,10,30,100)

speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('The chiken hit!', True, (180, 0, 0))

finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False    
    window.blit(background, (0, 0))
    if finish != True:
        egg.rect.x += speed_x
        egg.rect.y += speed_y
    if egg.rect.y > win_height-50 or egg.rect.y < 0:
            speed_y *= -1
    if sprite.collide_rect(chik, egg):
            speed_x *= -1
    if egg.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if egg.rect.x > win_width-50:
        finish = True
        window.blit(lose2, (200,200))
    

    chik.update()
    chik.reset()
    egg.reset()
    display.update()
    time.delay(50)


    
    
