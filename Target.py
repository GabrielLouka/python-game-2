from abc import ABC
from gameLogic import pg, WIDTH, LABEL_LIMIT, TARGET_SIDE_SIZE

class BaseTarget:
    def __init__(self, life) -> None:
        self.life = life

class BlackTarget(BaseTarget):
    def __init__(self, life) -> None:
        super().__init__(life)
        self.rect = pg.Rect(WIDTH - 100, 5*LABEL_LIMIT, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

class GreenTarget(BaseTarget):
    def __init__(self, life) -> None:
        super().__init__(life)
        self.rect = pg.Rect(WIDTH - 100, 10*LABEL_LIMIT, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

class SpecialTarget(BaseTarget):
    def __init__(self, life) -> None:
        super().__init__(life)
        self.rect = pg.Rect(WIDTH - 100, 15*LABEL_LIMIT, TARGET_SIDE_SIZE, TARGET_SIDE_SIZE)

    