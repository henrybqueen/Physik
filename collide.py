import pygame

pygame.init()
w=720
h=720
screen=pygame.display.set_mode((w, h))
clock=pygame.time.Clock()
running=True

class particle():
    def __init__(self, x, v):
        self.x=x
        self.v=v
    def draw(self):
        pygame.draw.circle(screen, "red", self.pixel_cords(), 10)
    def pixel_cords(self):
        return (int(self.x * w), int(h/2))

p=particle(.5, 0.5)

gor = True  # starting direction right

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill("black")

    dt = clock.tick(60) / 1000

    if gor==True:
        p.x += p.v * dt
        if p.x > 1:
            gor=False
    else:
        p.x -= p.v*dt
        if p.x<0:
            gor=True


    p.draw()

    pygame.display.flip()



pygame.quit()
