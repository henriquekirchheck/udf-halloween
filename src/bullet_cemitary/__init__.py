import sys

import pygame

from bullet_cemitary.ball import Ball
from bullet_cemitary.soul.group import SoulGroup
from bullet_cemitary.soul.sprite import SoulSprite


def main() -> None:
    _ = pygame.init()

    screen = pygame.display.set_mode(
        (1280, 960),
        pygame.SCALED,
    )
    ball = Ball()
    bullets = pygame.sprite.Group(ball)
    soul = SoulGroup(SoulSprite())
    clock = pygame.Clock()

    while True:
        for event in pygame.event.get():
            soul.event(event=event)
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN  # pyright: ignore[reportAny]
                and event.mod & pygame.KMOD_ALT  # pyright: ignore[reportAny]
            ):
                _ = pygame.display.toggle_fullscreen()
            if event.type == pygame.QUIT:
                sys.exit()

        bullets.update()
        soul.update()

        # pygame.sprite.spritecollideany()

        _ = screen.fill((0, 0, 0))
        _ = bullets.draw(screen)
        _ = soul.draw(screen)

        pygame.display.flip()

        _ = clock.tick(60)


if __name__ == "__main__":
    main()
