import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class FootballDataAPI:
    def __init__(self):
        self.BASE_URL = "https://api.football-data.org/v4"
        self.API_KEY = os.getenv("FOOTBALL_API_KEY")
        self.headers = {"X-Auth-Token": self.API_KEY}
    
    def get_league_matches(self, league_code=2013, season=2025):
        response = requests.get(
            f"{self.BASE_URL}/competitions/{league_code}/matches",
            headers=self.headers,
            params={"season": season}
        )
        response.raise_for_status()
        return response.json()["matches"]
