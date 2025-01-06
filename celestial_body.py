import math

class CelestialBody:
    def __init__(self, name, radius, distance, speed, color):
        self.name = name
        self.radius = radius
        self.distance = distance
        self.speed = speed
        self.color = color
        self.angle = 0  # Initial angle for orbit
        self.object_id = None  # Canvas object ID

    def update_position(self, center_x, center_y):
        """Calculate the new position of the celestial body."""
        self.angle += self.speed
        x = center_x + self.distance * math.cos(self.angle)
        y = center_y + self.distance * math.sin(self.angle)
        return x, y
