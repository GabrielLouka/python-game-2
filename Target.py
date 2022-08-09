from abc import ABC
from gameLogic import pg, WIDTH, LABEL_LIMIT, TARGET_SIDE_SIZE

class BaseTarget:
    def __init__(self, life, x, y) -> None:
        self.life = life
        self.x = x
        self.y = y

class BlackTarget(BaseTarget):
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

class GreenTarget(BaseTarget):
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

class SpecialTarget(BaseTarget):
    def __init__(self, life, x, y) -> None:
        super().__init__(life, x, y)
        self.rect = pg.Rect(x, y, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

    