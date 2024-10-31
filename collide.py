import pygame
#happy halloween

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

p=particle(.5, .5)
r=particle(0.4,0.1)

directions = {p: True, r: True} # starting directions true is right
parts = (p, r)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill("black")

    dt = clock.tick(60)/1000

    for n in parts:
        if directions[n]: #conditions for colliding while travelling right
            n.x += n.v * dt
            if n.x > 1:
                directions[n]=False
            if (n == p and 0 < r.x - p.x <= 0.01) or (n == r and 0 < p.x - r.x <= 0.01):
                p.v, r.v = r.v, p.v
                directions[n] = False
        else:
            n.x -= n.v*dt
            if n.x < 0:
                directions[n] = True
            if  (n == p and 0<p.x - r.x <= 0.01) or (n == r and 0<r.x - p.x <= 0.01):
                p.v, r.v = r.v, p.v
                directions[n] = True

    p.draw()
    r.draw()
    pygame.display.flip()



pygame.quit()
