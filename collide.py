import pygame
#happy halloween

pygame.init()
w=720
h=720
screen=pygame.display.set_mode((w, h))
clock=pygame.time.Clock()
running=True

class particle():
    def __init__(self, x, v, col):
        self.x=x
        self.v=v
        self.col=col
    def draw(self):
        pygame.draw.circle(screen, self.col, self.pixel_cords(), 10)

    def pixel_cords(self):
        return (int(self.x * w), int(h/2))

p=particle(.5, .5, "red")
r=particle(0.4,0.1, "blue")

directions = {p: False, r: True} # starting directions true is right
parts = (p, r)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill("black")

    dt = clock.tick(120)/1000


    for n in parts:
        if directions[n]: #conditions for colliding while travelling right
            n.x += n.v * dt
            if n.x > 1:
                directions[n]=False
        else:
            n.x -= n.v*dt
            if n.x < 0:
                directions[n] = True

    if abs(r.x - p.x) <= 0.01:
        p.v, r.v = r.v, p.v
        if directions[p] != directions[r]:
            directions[p], directions[r]= directions[r], directions[p]


    '''
    for n in parts:
            if directions[n]:  # Moving right
                n.x += n.v * dt
                if n.x > 1:
                    directions[n] = False
            else:  # Moving left
                n.x -= n.v * dt
                if n.x < 0:
                    directions[n] = True

            # Check for collision and swap velocities
            if (n == p and 0 < r.x - p.x <= 0.01) or (n == r and 0 < p.x - r.x <= 0.01):
                p.v, r.v = r.v, p.v  # Swap velocities
                if directions[p] == directions[r]:
                    directions[p] = not directions[p]
                    directions[r] = not directions[r]
    '''
    p.draw()
    r.draw()
    pygame.display.flip()



pygame.quit()
