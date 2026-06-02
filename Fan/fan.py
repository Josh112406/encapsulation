class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed:int = SLOW, radius: float = 5, color: str = "blue", state: bool = False):
        self.__speed: int = speed
        self.__state: bool = state
        self.__radius: float = radius
        self.__color: str = color
        
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color