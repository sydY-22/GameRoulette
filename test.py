import os
from dotenv import load_dotenv
from steam_web_api import Steam

load_dotenv(encoding="utf-16")

KEY = os.environ.get("STEAM_API_KEY")
print(KEY)
steam = Steam(KEY)

user = steam.users.get_user_details("76561198271994774")  

print(user)
