from enum import Enum


class GameOption(str, Enum):
    ROCK: str = "rock"
    PAPER: str = "paper"
    SCISSORS: str = "scissors"

    def __str__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        if other == GameOption.ROCK:
            return self == GameOption.SCISSORS
        elif other == GameOption.PAPER:
            return self == GameOption.ROCK
        elif other == GameOption.SCISSORS:
            return self == GameOption.PAPER


if __name__ == "__main__":
    rock_paper_scissors_mapping = {
        'A': GameOption.ROCK,
        'B': GameOption.PAPER,
        'C': GameOption.SCISSORS,
        'X': GameOption.ROCK,
        'Y': GameOption.PAPER,
        'Z': GameOption.SCISSORS
    }
    WINNING_POINTS = 6
    DRAW_POINTS = 3
    point_mapping = {
        GameOption.ROCK: 1,
        GameOption.PAPER: 2,
        GameOption.SCISSORS: 3
    }
    with open('./input.txt', 'r') as f:
        games = f.read().splitlines()
        total_points = 0
        for game in games:
            opponent_move, my_move = map(rock_paper_scissors_mapping.get, game.split(' '))
            total_points += point_mapping[my_move]
            if opponent_move == my_move:
                total_points += DRAW_POINTS
            elif opponent_move < my_move:
                total_points += WINNING_POINTS
        print(total_points)




