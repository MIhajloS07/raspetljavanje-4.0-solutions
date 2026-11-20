from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Bullet:
    p: Vector2
    R: int
    max_v: float
    v: Vector2
    start: Vector2
    max_distance: Vector2