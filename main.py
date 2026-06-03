import os
from dotenv import load_dotenv
from steam_web_api import Steam
import random

load_dotenv(encoding="utf-16")

class GameRoulette:
    
    def get_games(self):
        """Retrieve the games from steam library."""
        KEY = os.environ.get("STEAM_API_KEY")
        steam = Steam(KEY)
        all_games = steam.users.get_owned_games("76561198271994774")

        all_games_ls = []

        for i in range(0, len(all_games['games'])):
            all_games_ls.append(all_games['games'][i]['name'])
        return all_games_ls
    
    def list_games(self):
        """List all the games."""
        games = self.get_games()

        for game in games:
            print(f"{game}")
        print()
    
    def spin(self):
        """Select a game randomly."""
        games = self.get_games()

        return print(random.choice(games))
    


def main():
    pick = GameRoulette()
    #pick.list_games()
    pick.spin()



if __name__ == "__main__":
    main()


