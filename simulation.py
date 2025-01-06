from celestial_body import CelestialBody

class SolarSystemSimulation:
    def __init__(self, canvas_manager):
        self.canvas_manager = canvas_manager
        self.center_x = 400
        self.center_y = 400
        self.bodies = []

        # Add celestial bodies
        self.bodies.append(CelestialBody("Sun", 30, 0, 0, "yellow"))
        self.bodies.append(CelestialBody("Mercury", 5, 50, 0.1, "gray"))
        self.bodies.append(CelestialBody("Venus", 7, 100, 0.07, "yellow"))
        self.bodies.append(CelestialBody("Earth", 10, 150, 0.05, "blue"))
        self.bodies.append(CelestialBody("Mars", 8, 200, 0.04, "red"))

    def start(self):
        """Initialize canvas objects and start animation."""
        # Draw celestial bodies
        for body in self.bodies:
            x, y = self.center_x, self.center_y  # Start at center
            if body.distance > 0:  # Skip Sun's position calculation
                x += body.distance
            body.object_id = self.canvas_manager.draw_circle(
                x, y, body.radius, body.color
            )
        
        # Begin animation loop
        self.animate()

    def animate(self):
        """Update positions and animate celestial bodies."""
        for body in self.bodies:
            if body.distance > 0:  # Skip the Sun
                x, y = body.update_position(self.center_x, self.center_y)
                self.canvas_manager.update_position(body.object_id, x, y, body.radius)
        
        # Schedule the next frame
        self.canvas_manager.canvas.after(20, self.animate)
