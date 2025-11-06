import pygame

from bullet_cemitary.soul.sprite import SoulSprite


class SoulGroup(pygame.sprite.GroupSingle[SoulSprite]):
    def event(self, event: pygame.Event) -> None:
        if self.sprite:
            self.sprite.event(event)
