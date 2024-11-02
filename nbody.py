import pygame as pg
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
MAX_TRAIL_LENGTH = 128
G = 0.01  # Gravitational constant for scaling

# Pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

class Particle:
    def __init__(self, position, velocity, color, size, mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.color = color
        self.size = size
        self.mass = mass
        self.history = []

    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.to_pixel_coords(self.position), self.size)
        if len(self.history) > 1:
            pg.draw.aalines(surface, self.color, False, [self.to_pixel_coords(pos) for pos in self.history])

    def to_pixel_coords(self, pos):
        """Convert normalized coordinates [-1, 1] to screen coordinates."""
        return int((pos[0] + 1) / 2 * WIDTH), int((-pos[1] + 1) / 2 * HEIGHT)

    def update_trail(self):
        """Manage the particle's trail history."""
        self.history.append(self.position.copy())
        if len(self.history) > MAX_TRAIL_LENGTH:
            self.history.pop(0)

    def update_position(self, dt):
        """Update particle position based on its velocity."""
        self.position += self.velocity * dt

    def apply_gravitational_forces(self, other_particles, dt):
        """Update particle velocity under gravitational force from other particles."""
        total_force = np.zeros(2)
        for other in other_particles:
            if other != self:
                displacement = other.position - self.position
                distance = np.linalg.norm(displacement)
                if distance > 1e-2:  # Avoid division by zero
                    force_magnitude = G * self.mass * other.mass / distance**2
                    force_direction = displacement / distance
                    total_force += force_magnitude * force_direction
        # Update velocity based on the net force
        self.velocity += (total_force / self.mass) * dt


def main():
    n = 20  # Number of particles
    particles = []

    # Initialize particles with random positions and velocities
    for _ in range(n):
        position = np.random.uniform(-0.9, 0.9, 2)  # Random position in normalized coordinates
        velocity = np.random.uniform(-0.1, 0.1, 2)  # Random initial velocity
        color = (np.random.randint(50, 255), np.random.randint(50, 255), np.random.randint(50, 255))
        size = np.random.randint(3, 7)
        mass = np.random.uniform(0.5, 1.5)
        particles.append(Particle(position=position, velocity=velocity, color=color, size=size, mass=mass))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Clear screen
        screen.fill(WHITE)

        # Update and draw particles
        dt = clock.tick(FPS) / 1000.0
        for particle in particles:
            particle.apply_gravitational_forces(particles, dt)
        for particle in particles:
            particle.update_position(dt)
            particle.update_trail()
            particle.draw(screen)

        # Update display
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
