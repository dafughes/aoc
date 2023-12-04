import sys
    
def read_input(day):
    inputfile = f"input/demo-input{day}.txt" if len(sys.argv) > 1 else  f"input/input{day}.txt"
    with open(inputfile, "r") as file:
        return file.read()

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, value):
        return Vec2(self.x * value, self.y * value)
    
    def __truediv__(self, value):
        return self * (1 / value)
    
    def __floordiv__(self, value):
        return Vec2(self.x // value, self.y // value)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not (self == other)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

EAST = Vec2(1, 0)
SOUTHEAST = Vec2(1, 1)
SOUTH = Vec2(0, 1)
SOUTHWEST = Vec2(-1, 1)
WEST = Vec2(-1, 0)
NORTHWEST = Vec2(-1, -1)
NORTH = Vec2(0, -1)
NORTHEAST = Vec2(1, -1)

DIRECTIONS = [EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST, NORTH, NORTHEAST]
CARDINALS = [NORTH, EAST, SOUTH, WEST]
INTERCARDINALS = [NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST]
    
def neighbors(pos, limits=None, intercardinals=True):
    candidates = [pos + dir for dir in (DIRECTIONS if intercardinals else CARDINALS)]
    
    if limits:
        def is_inside(p):
            return 0 <= p.x < limits.x and 0 <= p.y < limits.y
        return list(filter(lambda x: is_inside(x), candidates))
    else:
        return candidates
