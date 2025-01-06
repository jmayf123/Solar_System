from tkinter import Tk, Canvas
from canvas_manager import CanvasManager
from simulation import SolarSystemSimulation

def main():
    # Initialize Tkinter
    root = Tk()
    root.title("Solar System Simulation")

    # Create Canvas
    canvas_width, canvas_height = 800, 800
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="black")
    canvas.pack()

    # Create Canvas Manager
    canvas_manager = CanvasManager(canvas)

    # Initialize Solar System Simulation
    simulation = SolarSystemSimulation(canvas_manager)
    simulation.start()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
