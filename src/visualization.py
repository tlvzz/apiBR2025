import matplotlib.pyplot as plt
import pandas as pd

class BrasileiraoVisualization:
    @staticmethod
    def plot_team_position_history(history_df, team_name):
        plt.figure(figsize=(12, 6))
        ax = plt.gca()
        ax.invert_yaxis()
        # Restante da implementação do gráfico
        plt.savefig(f'outputs/graficos/evolucao_{team_name.lower()}.png')
