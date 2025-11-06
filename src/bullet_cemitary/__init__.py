import sys

import pygame
from pygame.sprite import Group

from bullet_cemitary.bullets.ball import Ball
from bullet_cemitary.engine.asset_loader import load_font
from bullet_cemitary.soul.group import SoulGroup
from bullet_cemitary.soul.sprite import SoulSprite


def main() -> None:
    _ = pygame.init()

    sans = load_font("fonts/DTM-Sans.ttf")
    mono = load_font("fonts/DTM-Mono.ttf")

    screen = pygame.display.set_mode(
        (1280, 960),
        pygame.SCALED,
    )

    ball = Ball()
    bullets: Group[pygame.sprite.Sprite] = pygame.sprite.Group(ball)

    soul = SoulGroup(SoulSprite())
    if soul.sprite is None:
        sys.exit(1)

    clock = pygame.Clock()

    while True:
        for event in pygame.event.get():
            soul.sprite.event(event=event)
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN  # pyright: ignore[reportAny]
                and event.mod & pygame.KMOD_ALT  # pyright: ignore[reportAny]
            ):
                _ = pygame.display.toggle_fullscreen()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        bullets.update()
        soul.update()

        if sprite := pygame.sprite.spritecollideany(soul.sprite, bullets):
            soul.sprite.collision(sprite)

        health = mono.render(f"{soul.sprite.health}/20", True, (255, 255, 255))

        _ = screen.fill((0, 0, 0))
        _ = bullets.draw(screen)
        _ = soul.draw(screen)
        _ = screen.blit(health, health.get_rect())

        pygame.display.flip()

        _ = clock.tick(30)


if __name__ == "__main__":
    main()
