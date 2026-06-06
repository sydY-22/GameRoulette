import os
from dotenv import load_dotenv
from steam_web_api import Steam
import random
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

load_dotenv(encoding="utf-16")

# color palettes:
GREEN = "#0A7C6E"
YELLOW = "#F59E0B"
ORANGE = "#FF6B35"
WHITE = "#FAFAFA"

class GameRoulette:

    # main window:
    window = tk.Tk()
    window.title('Game Roulette!')
    window.config(padx=40, pady=40, bg=ORANGE)
    window.geometry('550x450')

    # canvas:
    canvas = tk.Canvas(width=250, height=250, bg=ORANGE)
    roulette_img = tk.PhotoImage(file="roulette-img.png")
    canvas.create_image(100, 100, image=roulette_img)

    string_var = tk.StringVar(value='Game!')


    
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

        return print(f"PLAY!: {random.choice(games)}")
    
    def button_func(self):
        """Randomly select a game on button press."""
        games = self.get_games()
        self.string_var.set(f"PLAY!: {random.choice(games)}")
    

    
    # def menu(self):
    #     """Displays the menu."""
    #     print("1. List Games ")
    #     print("2. Spin!!!")
    #     print("3. Exit...")
    


def main():
    print("Welcome to Game Roulette!!!")
    pick = GameRoulette()

    # 

    label = ttk.Label(master=pick.window, text='label', textvariable=pick.string_var, background=YELLOW, foreground=GREEN)
    label.pack()

    button = tk.Button(master=pick.window, text='SPIN!', command=pick.button_func, background=GREEN, foreground=WHITE)
    button.pack()

    # run the app:
    pick.window.mainloop()

    # while True:
    #     pick.menu()
    #     prompt = input("Please choose options 1-3: ")

    #     if prompt == '1':
    #         pick.list_games()
    #     elif prompt == '2':
    #         pick.spin()
    #         print()
    #     else:
    #         return False
        


if __name__ == "__main__":
    main()


