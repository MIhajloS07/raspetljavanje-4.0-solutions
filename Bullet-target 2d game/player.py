from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Player:
    p: Vector2
    v: Vector2
    color: tuple
    R: int
    max_v: float
    angle: float
    lives: int
    points: int
    last_shot: int
    indestructible_from: int
    
    
