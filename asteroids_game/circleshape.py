import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)
        pass

    def update(self, dt):
        # must override
        pass
    def collides_with(self, other):
        space_between = self.position.distance_to(other.position)
        combined_radius = self.radius + other.radius
        if combined_radius > space_between:
            return True
        else:
            return False