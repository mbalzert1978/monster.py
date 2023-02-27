from __future__ import annotations

import random
import abc

import main


def calculate_damage(entitiy: main.Entity, attack_roll: int) -> None:
    """Substracts the damage dealt."""
    entitiy.health -= attack_roll


def calculate_attack(entity: main.Entity) -> int:
    """
    Evaluate the entity attackvalue.

    Args:
        entity: The entity object.

    Returns:
        The damage dealt.
    """
    return random.randint(entity.attack_min, entity.attack_max)


class MonsterGameContext:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def attack(self, entity: main.Entity) -> None:
        """
        Calls the strategy's draw_outcome method.
        """
        attack_roll = calculate_attack(entity)
        calculate_damage(entity, attack_roll)
        self.strategy.draw_outcome(attack_roll)


class Strategy(abc.ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abc.abstractmethod
    def draw_outcome(self, attack_roll: int) -> None:
        pass


class MonsterAttack(Strategy):
    def __init__(self, monster: main.Entity, player: main.Entity) -> None:
        self.monster = monster
        self.player = player

    def draw_outcome(self, attack_roll: int) -> None:
        print(
            f"{self.monster.name} attacks "
            f"{self.player.name} for "
            f"{attack_roll} damage"
        )


class PlayerAttack(Strategy):
    def __init__(self, player: main.Entity) -> None:
        self.player = player

    def draw_outcome(self, attack_roll: int) -> None:
        print(f"{self.player.name} attacks monster for {attack_roll} damage.")
