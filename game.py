"""
Monster Game v0.1 (OO)
"""
import random
from Player.player_module import (
    HumanPlayer,
    RandomComputerPlayer,
    BetterComputerPlayer,
)


class MonsterGame:
    """
    Game Class
    """

    rounds = 1

    def __init__(self) -> None:
        self.current_winner = None

    def print_board(self, active_player, target):
        """
        prints the board
        """
        print(f"{self.rounds}, Rounds played ")
        print(
            f"{active_player.name}'s, remaining health: {active_player.health}"
        )
        print(f"{target.name}'s, remaining health: {target.health} ")

    @staticmethod
    def make_move(attacker, target, print_game=True):
        """
        gets attacker move and makes the move happen
        """
        if attacker.get_move(attacker, target) == 1:
            attack = random.choice(
                list(range(attacker.attack_min, attacker.attack_max + 1))
            )
            if print_game:
                print(
                    f"{attacker.name} hits {target.name} for {attack} damage."
                )
            target.health -= attack
            return True
        if attacker.get_move(attacker, target) == 2:
            if print_game:
                print(f"{attacker.name} heals himself for {attacker.heal}.")
            attacker.health += attacker.heal
            return True
        return False

    @staticmethod
    def is_health_zero(player) -> bool:
        """
        checks if any player has 0 health
        """
        if player.health <= 0:
            return True
        return False

    def is_winner(self, player, target) -> bool:
        """
        checks wincondition
        """
        if self.is_health_zero(target):
            self.current_winner = player
            return True
        return False


def play(game, player1, player2, print_game=True):
    """Play game function"""
    attacker = player1
    target = player2
    while not game.current_winner:
        if print_game:
            game.print_board(attacker, target)
        game.make_move(attacker, target, print_game)
        game.is_winner(attacker, target)
        if game.current_winner:
            if print_game:
                print(
                    f"{attacker.name} wins the Match.\
After {game.rounds} rounds."
                )
            return attacker.name
        attacker, target = target, attacker
        game.rounds += 1


if __name__ == "__main__":
    CPU1WINS = 0
    CPU2WINS = 0
    for _ in range(1000):
        human_player = HumanPlayer()
        random_cpu = RandomComputerPlayer()
        better_cpu = BetterComputerPlayer("cpu2")
        m = MonsterGame()
        result = play(m, random_cpu, better_cpu, False)
        if result in ["Hal9000", "T-800", "ED-209", "M.A.R.K.13"]:
            CPU1WINS += 1
        if result in "cpu2":
            CPU2WINS += 1
    print(
        f"after 1000 rounds, we see cpu1 {CPU1WINS} \
wins, and cpu2 {CPU2WINS} wins"
    )
