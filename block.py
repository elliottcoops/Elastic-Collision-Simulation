class block:

    def __init__(self, mass, colour, speed):

        self.default_width, self.default_height = 40, 40 # Set the default width and height for 1kg block
        self.mass = mass # Mass in kg
        self.colour = colour
        self.proportion = mass * 0.5

        self.x = None
        self.y = None

        self.speed = speed

        self.momentum = None
        self.kinetic_energy = None

    def get_dimensions(self):
        return self.default_width, self.default_height
    
    def get_colour(self):
        return self.colour
    
    def get_momentum(self):
        return self.momentum
    
    def get_kinetic_energy(self):
        return self.momentum
    
    def set_momentum(self):
        self.momentum = self.mass * self.speed

    def set_kinetic_energy(self):
        self.momentum = (0.5 * self.mass) * (self.speed ** 2)
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def move(self):
        self.x += self.speed
