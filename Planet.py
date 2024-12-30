import math

class Planet:
    def __init__(self, canvas, x, y, radius, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.angle = 0
        self.speed = 0.1 # Adjust this to change speed
        self.orbit_radius = x

        self.planet = self.canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color
        )

    def update(self):
        self.angle += self.speed
        self.x = 400 + self.orbit_radius * math.cos(self.angle)
        self.y = 300 + self.orbit_radius * math.sin(self.angle)
        self.canvas.coords(
            self.planet,
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius
        )

