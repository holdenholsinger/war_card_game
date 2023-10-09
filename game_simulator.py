from game import Game
import pandas as pd

class GameSimulation:
    def __init__(self):
        self.simulation_results = pd.DataFrame()

    def run_simulation(self, game_iterations):
        for _ in range(game_iterations):
            game_iteration = Game()
            game_results = game_iteration.active_cards_fight()
            my_list.append(game_results)


game_simulation = GameSimulation()

game_simulation.run_simulation(100)

print(my_list)