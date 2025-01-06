def random_color():
    """Generate a random hex color."""
    import random
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
