from api_football import FootballDataAPI
from analysis import BrasileiraoAnalysis
from visualization import BrasileiraoVisualization
import pandas as pd

def main():
    api = FootballDataAPI()
    analyzer = BrasileiraoAnalysis()
    visualizer = BrasileiraoVisualization()
    
    matches = api.get_league_matches()
    df_matches = pd.DataFrame(matches)
    
    # Processamentos e análises
    standings = analyzer.create_standings(df_matches)
    corinthians_history = analyzer.get_team_history(df_matches, "Corinthians")
    
    # Visualização
    visualizer.plot_team_position_history(corinthians_history, "Corinthians")

if __name__ == "__main__":
    main()
