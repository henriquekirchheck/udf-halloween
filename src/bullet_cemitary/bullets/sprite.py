import abc

from bullet_cemitary.engine.sprite import Sprite


class BulletSprite(Sprite, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def damage(self) -> int: ...
