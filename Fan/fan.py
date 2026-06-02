class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed:int = SLOW, radius: float = 5, color: str = "blue", state: bool = False):
        self.__speed: int = speed
        self.__state: bool = state
        self.__radius: float = radius
        self.__color: str = color