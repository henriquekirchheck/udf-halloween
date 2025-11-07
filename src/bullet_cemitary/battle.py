from typing import final, override

import pygame

from bullet_cemitary.bullets.ball import Ball
from bullet_cemitary.bullets.group import BulletGroup
from bullet_cemitary.engine.asset_loader import load_font
from bullet_cemitary.engine.scene import Scene
from bullet_cemitary.soul.group import SoulGroup
from bullet_cemitary.soul.sprite import SoulSprite


@final
class BattleScene(Scene):
    @override
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        self.sans = load_font("fonts/DTM-Sans.ttf")
        self.mono = load_font("fonts/DTM-Mono.ttf")

        ball = Ball()
        self.bullets = BulletGroup(ball)

        self.soul = SoulGroup(SoulSprite())

    @override
    def update(self, delta: float) -> None:
        self.bullets.update(delta)
        self.soul.update(delta)

        if sprite := pygame.sprite.spritecollideany(self.soul.sprite, self.bullets):
            self.soul.sprite.collision(sprite)

        health = self.mono.render(
            f"{self.soul.sprite.health}/20",
            False,
            (255, 255, 255),
        )

        _ = self.screen.fill((0, 0, 0))

        _ = self.bullets.draw(self.screen)
        _ = self.soul.draw(self.screen)
        _ = self.screen.blit(health, health.get_rect())

    @override
    def physics_update(self) -> None:
        self.bullets.physics_update()
        self.soul.physics_update()

    @override
    def event(self, event: pygame.Event) -> None:
        self.bullets.event(event)
        self.soul.event(event)
