from circleshape import *
from constants import *

class PewPew(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PEWPEW_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)