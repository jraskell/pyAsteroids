from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for c in Asteroid.containers:
            c.add(self)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle1 = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle1)
        vel2 = self.velocity.rotate(-angle1)
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = vel1 * 1.2
        Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = vel2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)