import tkinter as tk
from Planet import Planet

class SolarSystem:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600, bg="black")
        self.canvas.pack()

        self.planets = []
        self.create_planets()
        self.animate()

    def create_planets(self):
        # Sun
        self.planets.append(Planet(self.canvas, 0, 0, 30, "yellow"))
        # Mercury
        self.planets.append(Planet(self.canvas, 50, 0, 5, "gray"))
        # Venus
        self.planets.append(Planet(self.canvas, 80, 0, 8, "orange"))
        # Earth
        self.planets.append(Planet(self.canvas, 110, 0, 10, "blue"))
        # Mars
        self.planets.append(Planet(self.canvas, 140, 0, 7, "red"))

    def animate(self):
        for planet in self.planets:
            planet.update()
        self.master.after(16, self.animate)