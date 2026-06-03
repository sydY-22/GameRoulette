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
    user = steam.users.get_owned_games("76561198271994774")

    #print(len(user['games']))

    games = []

    for i in range(0, len(user['games'])):
        games.append(user['games'][i]['name'])
    return games


def spin():
    """Randomly selects a game from library."""
    return print(random.choice(get_games()))

def main():
    get_games()

    spin()


if __name__ == "__main__":
    main()

