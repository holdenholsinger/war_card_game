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
            # run analysis on the data
#             analyze mean and such
game_simulation = GameSimulation()

game_simulation.run_simulation(100)

print(game_simulation.data)