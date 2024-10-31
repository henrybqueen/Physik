import pygame as pg
import numpy as np  

# Initialize Pygame
pg.init()
clock = pg.time.Clock()

# Set screen dimensions (in pixels)
width, height = 800, 600
screen = pg.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

class Particle:
    def __init__(self, x: np.array, v: np.array):
        self.x = np.array(x, dtype=float)  # Position in normalized coordinates
        self.v = np.array(v, dtype=float)  # Velocity

    def draw(self):
        pg.draw.circle(screen, blue, self.pixel_cords(), 7)

    def pixel_cords(self):
        """Convert from normalized coordinates [0,1] to screen coordinates [0,width] and [0,height]."""
        return (int(self.x[0] * width), int(self.x[1] * height))

    def step(self, dt: float):
        # Hooke's law 
        f = -(self.x[0] - 0.5)
        
        # Update velocity with damping: dv = (f/m - damping * v) * dt
        self.v[0] += f * dt

        # Update position
        self.x += dt * self.v


# Initialize particle
p = Particle([0.1, 0.5], [0, 0])

# Simulation loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(white)
    pg.draw.line(screen, black, (0, int(height/2)), (width, int(height/2)), 1)

    dt = clock.tick(256) / 1000.0

    # Update and draw particle
    p.step(dt)
    p.draw()

    pg.display.flip()

pg.quit()
