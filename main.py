import pygame,sys,os


class vaiseaux(pygame.sprite.Sprite):
    # tt les variable
    x = 0
    y = 0
    speed = 1.0

    distance_de_dash = 100

    dash_is_ok = True

    # tt les methode
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('perso.jpg')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.y -= 0.25 * self.speed
        if pressed_key[pygame.K_DOWN]:
            self.y += 0.25 * self.speed
        if pressed_key[pygame.K_LEFT]:
            self.x -= 0.25 * self.speed
        if pressed_key[pygame.K_RIGHT]:
            self.x += 0.25 * self.speed

        self.x = max(min(self.x,700-70),0)
        self.y = max(min(self.y,1000-40),0)

        self.rect.x = self.x  # go to x
        self.rect.y = self.y  # go to y

    def dash(self):
        if self.dash_is_ok:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LEFT]:
                self.x -= self.distance_de_dash
            if pressed_key[pygame.K_RIGHT]:
                self.x += self.distance_de_dash
            if pressed_key[pygame.K_UP]:
                self.y -= self.distance_de_dash
            if pressed_key[pygame.K_DOWN]:
                self.y += self.distance_de_dash
            self.update()

pygame.init()

size = width, height = 700, 1000
screen = pygame.display.set_mode(size)

player = vaiseaux()

player_list = pygame.sprite.Group()
player_list.add(player)

backdropbox = screen.get_rect()
backdrop = pygame.image.load(os.path.join('bg.png'))


while 1:
    screen.blit(backdrop, backdropbox)
    player_list.draw(screen)
    pygame.display.flip()

    player.update()

    ticks = pygame.time.get_ticks()
    #print(ticks)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.dash()