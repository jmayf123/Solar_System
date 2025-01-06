class CanvasManager:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw_circle(self, x, y, radius, color):
        """Draw a circle on the canvas."""
        return self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, fill=color, outline=color
        )

    def update_position(self, object_id, x, y, radius):
        """Update the position of a canvas object."""
        self.canvas.coords(
            object_id,
            x - radius, y - radius, x + radius, y + radius
        )

