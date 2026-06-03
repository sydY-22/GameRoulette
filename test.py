import os
from dotenv import load_dotenv
from steam_web_api import Steam
import random

load_dotenv(encoding="utf-16")

KEY = os.environ.get("STEAM_API_KEY")
#print(KEY)
steam = Steam(KEY)


def get_games():
    """Gets the games from steam library."""
    all_games = steam.users.get_owned_games("76561198271994774")

    #print(len(user['games']))

    all_games_ls = []

    for i in range(0, len(all_games['games'])):
        all_games_ls.append(all_games['games'][i]['name'])
    return all_games_ls


def list_games():
    """List all the Games."""
    pass


def spin():
    """Randomly selects a game from library."""
    return print(random.choice(get_games()))


def main():
    get_games()
    spin()


if __name__ == "__main__":
    main()

