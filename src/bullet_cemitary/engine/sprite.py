from typing import override

import pygame


class Sprite(pygame.sprite.Sprite):
    """simple base class for visible game objects

    bullet_cemitary.engine.sprite.Sprite(): return Sprite

    The base class for visible game objects. Derived classes will want to
    override the Sprite.update() method, the Sprite.physics_update() method,
    the Sprite.event() method, and assign Sprite.image and Sprite.rect
    attributes.

    When subclassing the Sprite class, be sure to call the base initializer
    before adding the Sprite to Groups.

    """

    def __init__(self) -> None:
        super().__init__()

    @override
    def update(self, delta: float) -> None: ...

    """method to control sprite behavior

    Sprite.update(delta: float):

    The default implementation of this method does nothing; it's just a
    convenient "hook" that you can override. This method is called by
    Group.update() with the delta you give it.

    There is no need to use this method if not using the convenience
    method by the same name in the Group class.

    """

    def physics_update(self) -> None: ...

    """method to control sprite behavior

    Sprite.physics_update():

    The default implementation of this method does nothing; it's just a
    convenient "hook" that you can override. This method is called by
    Group.physics_update().

    There is no need to use this method if not using the convenience
    method by the same name in the Group class.

    """

    def event(self, event: pygame.Event) -> None: ...  # pyright: ignore[reportUnusedParameter]

    """method to control sprite behavior

    Sprite.event():

    The default implementation of this method does nothing; it's just a
    convenient "hook" that you can override. This method is called by
    Group.event() with the event you give it.

    There is no need to use this method if not using the convenience
    method by the same name in the Group class.

    """


class AbstractGroup[T: Sprite](pygame.sprite.AbstractGroup[T]):
    """base class for containers of engine sprites

    AbstractGroup does everything needed to behave as a normal group. You can
    easily subclass a new group class from this or the other groups below if
    you want to add more features.

    Any AbstractGroup-derived sprite groups act like sequences and support
    iteration, len, and so on.

    """

    @override
    def update(self, delta: float) -> None:
        """call the update method of every member sprite

        Group.update(delta: float): return None

        Calls the update method of every member sprite. The delta argument that
        is passed to this method is passed to the Sprite update function.

        """
        for sprite in self.sprites():
            sprite.update(delta)

    def physics_update(self) -> None:
        """call the physics_update method of every member sprite

        Group.physics_update(): return None

        Calls the update method of every member sprite. This function should be
        called every few ms for consistent update timings.

        """
        for sprite in self.sprites():
            sprite.physics_update()

    def event(self, event: pygame.Event) -> None:
        """call the event method of every member sprite

        Group.event(event: pygame.Event): return None

        Calls the event method of every member sprite with the specified event.
        This function should be called every new event in the pool.

        """
        for sprite in self.sprites():
            sprite.event(event)


class Group[T: Sprite](AbstractGroup[T]):
    """container class for many Engine Sprites

    bullet_cemitary.engine.sprite.Group(*sprites): return Group

    A simple container for Sprite objects. This class can be subclassed to
    create containers with more specific behaviors. The constructor takes any
    number of Sprite arguments to add to the Group. The group supports the
    following standard Python operations:

        in      test if a Sprite is contained
        len     the number of Sprites contained
        bool    test if any Sprites are contained
        iter    iterate through all the Sprites

    The Sprites in the Group are not ordered, so the Sprites are drawn and
    iterated over in no particular order.

    """

    def __init__(self, *sprites: T) -> None:
        super().__init__()
        self.add(*sprites)


class GroupSingle[T: Sprite](AbstractGroup[T]):
    """A group container that holds a single item.

    This class works just like a regular group, but it only keeps a single
    sprite in the group.

    You can access its one sprite as the .sprite attribute.

    Calling add or remove does nothing.

    """

    __sprite: T

    def __init__(self, sprite: T) -> None:
        super().__init__()
        self.__sprite = sprite
        self.__sprite.add_internal(self)

    @override
    def copy(self) -> GroupSingle[T]:
        return GroupSingle[T](self.__sprite)

    @override
    def sprites(self) -> list[T]:
        return [self.__sprite]

    @property
    def sprite(self) -> T:
        """
        Property for the single sprite contained in this group

        :return: The sprite.
        """
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite: T) -> T:
        self.add_internal(sprite)
        sprite.add_internal(self)
        return sprite

    @override
    def add_internal(self, sprite: T, layer: int | None = None) -> None: ...

    @override
    def remove_internal(self, sprite: T) -> None: ...

    @override
    def has_internal(self, sprite: T) -> bool:
        return self.__sprite is sprite

    @override
    def __contains__(self, sprite: T) -> bool:
        return self.__sprite is sprite

    @override
    def __bool__(self) -> bool:
        return True
