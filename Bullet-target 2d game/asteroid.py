from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Asteroid:
    p: Vector2
    R: int
    max_v: float
    min_v: float
    v: Vector2