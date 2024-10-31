import pygame


# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Set screen dimensions, these are pixels
width, height = 800, 600

# screen object is needed for drawing things
screen = pygame.display.set_mode((width, height))


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


# Particle.x is normalized in [0, 1], so to get pixel coordinate we have to do int(p.x * width), where width is the number of pixels in the x dimension
class Particle():

    def __init__(self, x, v):
        self.x = x # position
        self.v = v # velocity 


    def draw(self):
        pygame.draw.circle(screen, blue, self.pixel_cords(), 7)


    # little method to convert from normalized cords [0, 1] to screen coords [0, width]. Since we are in one dimension, the y coordinate is fixed
    def pixel_cords(self):
        return (int(self.x * width), int(height/2))


p = Particle(0.1, 0)        

# Simulation loop
running = True

# each iteration of this loop is a "frame," so if our animation is 60 fps, this loop executes 60 times a second
while running:


    # this just checks if we've exited the window, boiler plate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # at the start of every render cycle, we paint over the screen to erase what we rendered on a previous cycle
    screen.fill(white)
    
    # a nice line for our particles to sit on 
    pygame.draw.line(screen, black, (0, int(height/2)), (width, int(height/2)), 2)



    # clock.tick(120) makes it so that our animation runs at <= 120 fps. If our animation gets really complicated it may run slower than 120 fps, but this
    # guarantees it will never exceed 120 fps. clock.tick() returns the elasped milli seconds since the last frame, so we divide by 1000 to get seconds
    dt = clock.tick(120) / 1000.0

    # hooks law
    f = (0.5-p.x)

    # f = m dv/dt, so dv = f/m * dt
    p.v += f * dt

    # v = dx/dt, so dx = v * dt
    p.x += p.v * dt



    p.draw()

    # this is critical. "Pygame uses a technique called double buffering. When you draw on the screen, 
    # you're actually drawing to a back buffer. The flip() function swaps this back buffer with the front buffer, making your changes visible"
    pygame.display.flip()


# Quit Pygame
pygame.quit()