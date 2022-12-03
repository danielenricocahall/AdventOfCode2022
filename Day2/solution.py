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

    def __gt__(self, other):
        if other == GameOption.ROCK:
            return self == GameOption.PAPER
        elif other == GameOption.PAPER:
            return self == GameOption.SCISSORS
        elif other == GameOption.SCISSORS:
            return self == GameOption.ROCK


class GameOutcome(str, Enum):
    WIN: str = "win"
    LOSE: str = "lose"
    DRAW: str = "draw"

    def __str__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


if __name__ == "__main__":
    rock_paper_scissors_mapping = {
        'A': GameOption.ROCK,
        'B': GameOption.PAPER,
        'C': GameOption.SCISSORS,
        'X': GameOption.ROCK,
        'Y': GameOption.PAPER,
        'Z': GameOption.SCISSORS
    }

    outcome_mapping = {
        'X': GameOutcome.LOSE,
        'Y': GameOutcome.DRAW,
        'Z': GameOutcome.WIN
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
            opponent_move, outcome = game.split(' ')
            opponent_move = rock_paper_scissors_mapping[opponent_move]
            outcome = outcome_mapping[outcome]
            if outcome == GameOutcome.WIN:
                my_move = next((move for move in GameOption if move > opponent_move))
            elif outcome == GameOutcome.LOSE:
                my_move = next((move for move in GameOption if move < opponent_move))
            else:
                my_move = opponent_move
            total_points += point_mapping[my_move]
            if opponent_move == my_move:
                total_points += DRAW_POINTS
            elif opponent_move < my_move:
                total_points += WINNING_POINTS
        print(total_points)
