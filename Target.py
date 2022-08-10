from abc import ABC
from gameLogic import pg, TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_LARGE, TARGET_SIDE_SIZE_MEDIUM

class BaseTarget:
    def __init__(self, life, x, y) -> None:
        self.life = life
        self.x = x
        self.y = y

class BlackTarget(BaseTarget): 
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_SMALL)

class GreenTarget(BaseTarget):
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE_MEDIUM, TARGET_SIDE_SIZE_MEDIUM)

class SpecialTarget(BaseTarget):
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE_LARGE, TARGET_SIDE_SIZE_LARGE)

    