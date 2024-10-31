import pygame as pg
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 256
MAX_TRAIL_LENGTH = 128
SUN_POSITION = np.array([0, 0])

# Pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

class Particle:
    def __init__(self, position: np.array, velocity: np.array, color: tuple, size: float):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color
        self.size = size
        self.history = []

    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.to_pixel_coords(self.position), self.size)
        if len(self.history) > 1:
            pg.draw.aalines(surface, self.color, False, [self.to_pixel_coords(pos) for pos in self.history])

    def to_pixel_coords(self, pos):
        """Convert normalized coordinates [-1, 1] to screen coordinates."""
        return int((pos[0] + 1) / 2 * WIDTH), int((-pos[1] + 1) / 2 * HEIGHT)

    def apply_gravitational_force(self, dt: float):
        """Update particle velocity and position under central gravitational force."""
        if np.linalg.norm(self.position) > 1e-6:  # Avoid division by zero at the center
            force = -(self.position / np.linalg.norm(self.position)**3)
            self.velocity += force * dt
        self.position += self.velocity * dt

    def update_trail(self):
        """Manage the particle's trail history."""
        self.history.append(self.position.copy())
        if len(self.history) > MAX_TRAIL_LENGTH:
            self.history.pop(0)

    def update(self, dt: float):
        self.apply_gravitational_force(dt)
        self.update_trail()


def main():
    particle = Particle(position=[-0.5, 0], velocity=[0.1, 0.7], color=BLUE, size=5)
    sun = Particle(position=SUN_POSITION, velocity=[0, 0], color=BLACK, size=10)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Clear screen
        screen.fill(WHITE)
        #pg.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 1)

        # Update and draw particles
        dt = clock.tick(FPS) / 1000.0
        particle.update(dt)
        particle.draw(screen)
        sun.draw(screen)

        # Update display
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
