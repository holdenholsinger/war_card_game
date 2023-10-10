from game import Game
import pandas as pd


class GameSimulation:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Total Battles', 'Times Shuffled', 'Game Time Minutes'])

    def run_simulation(self, game_iterations):
        for _ in range(game_iterations):
            game_iteration = Game()
            game_results = game_iteration.active_cards_fight()
            self.data.loc[len(self.data)] = game_results
            # run analysis on the data; analyze mean and such

    def mean_total_battles(self):
        return self.data['Total Battles'].mean()

    def mean_times_shuffled(self):
        return self.data['Times Shuffled'].mean()

    def mean_game_time(self):
        return self.data['Game Time Minutes'].mean()

game_simulation = GameSimulation()
game_simulation.run_simulation(100)
print(game_simulation.data)

print(f"Average total battles per game: {game_simulation.mean_total_battles()}")
print(f"Average deck shuffles per game: {game_simulation.mean_times_shuffled()}")
print(f"Average game length in minutes: {game_simulation.mean_game_time()}")