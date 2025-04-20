from models import *
import random
class SnakeAndLadderGame:
    BOARD_END = 100

    def __init__(self, players, snakes, ladders):
        self.players = players
        self.snakes = {snake.head: snake.tail for snake in snakes}
        self.ladders = {ladder.start: ladder.end for ladder in ladders}
        self.current_turn = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def get_next_position(self, position):
        if position in self.snakes:
            print(f"Oops! Landed on a snake at {position}. Going down to {self.snakes[position]}")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"Yay! Climbed a ladder from {position} to {self.ladders[position]}")
            return self.ladders[position]
        return position

    def play_turn(self, player):
        dice_value = self.roll_dice()
        print(f"{player.name} rolled a {dice_value}")
        if player.position + dice_value <= self.BOARD_END:
            player.set_position(self.get_next_position(player.position))
        print(player)

        if player.position == self.BOARD_END:
            print(f"\n{player.name} wins the game! 🏆\n")
            return True
        return False

    def start_game(self):
        print("\nGame Started!\n")
        while True:
            player = self.players[self.current_turn]
            if self.play_turn(player):
                break
            self.current_turn = (self.current_turn + 1) % len(self.players)


if __name__ == "__main__":
    players = [Player("Shubham"), Player("Rahul")]
    snakes = [Snake(99, 54), Snake(70, 55), Snake(52, 42)]
    ladders = [Ladder(6, 25), Ladder(11, 40), Ladder(60, 85)]

    game = SnakeAndLadderGame(players, snakes, ladders)
    game.start_game()