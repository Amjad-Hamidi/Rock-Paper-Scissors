"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
# Made By : Amjad Hamidi
choices = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.points = 0
        self.my_choice = None
        self.opponent_choice = None

    def move(self):
        return 'rock'

    def learn(self, my_choice, opponent_choice):
        self.my_choice = my_choice
        self.opponent_choice = opponent_choice


class AlwaysRockPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Let's play (rock/paper/scissors): ").lower()
            if choice in choices:
                return choice
            print("Invalid choice. Try again.")

    def show_moves(self, my_choice, opponent_choice):
        print(f"You played {my_choice}.")
        print(f"Computer played {opponent_choice}.")


class RandomChoicePlayer(Player):
    def move(self):
        return random.choice(choices)


class ReflectPlayer(Player):
    def move(self):
        if self.opponent_choice is None:
            return random.choice(choices)
        return self.opponent_choice


class CyclePlayer(Player):
    def move(self):
        if self.my_choice is None:
            return random.choice(choices)
        return choices[(choices.index(self.my_choice) + 1) % len(choices)]


def defeats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, player1, player2, rounds=10):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.rounds = rounds

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player1: {move1}  Player2: {move2}")
        if defeats(move1, move2):
            self.score1 += 1
            print("Player 1 wins!")
        elif defeats(move2, move1):
            self.score2 += 1
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print(f"Score: Player1: {self.score1}, Player2: {self.score2}")
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):
        print("Start Game!")
        print("You will play against the computer.")
        for round_number in range(self.rounds):
            print(f"Round {round_number + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Final score: Player1 {self.score1}, Player2 {self.score2}")


if __name__ == '__main__':
    ai_players = [AlwaysRockPlayer(), RandomChoicePlayer(), ReflectPlayer(),
                  CyclePlayer()]
    player1 = HumanPlayer()
    player2 = random.choice(ai_players)
    game = Game(player1, player2)
    print("________")
    game.play_game()
