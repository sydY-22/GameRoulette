import os
from dotenv import load_dotenv
from steam_web_api import Steam
import random
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from pathlib import Path
import math

load_dotenv(encoding="utf-16")

# color palettes:
GREEN = "#0A7C6E"
YELLOW = "#F59E0B"
ORANGE = "#FF6B35"
WHITE = "#FAFAFA"

class GameRoulette(tk.Tk):

    def __init__(self):
        super().__init__()
        # main window:
        self.title('Game Roulette!')
        self.config(padx=40, pady=40, bg=ORANGE)
        self.geometry('1000x850')

        self.string_var = tk.StringVar(value='Game!')

        # wheel colors:
        self.colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF0"]
        self.current_angle = 0.0
        self.target_angle = 0.0
        self.spin_speed = 0.0
        self.is_spinning = False

        # Canvas for the wheel
        self.canvas = tk.Canvas(self, width=500, height=500, bg=ORANGE)
        self.canvas.pack(pady=20)

        # wheel pointer:
        self.canvas.create_polygon(200, 20, 190, 50, 210, 50, fill="black")

        # draw the wheel:
        self.draw_wheel()

          # display the game
        self.label = tk.Label(master=self, text='label', textvariable=self.string_var, 
                        background=YELLOW, foreground=GREEN, font=("bold", 35))
        self.label.pack(pady=(0, 20))

        # spin button
        self.button = tk.Button(master=self, text='SPIN!', command=self.button_func, 
                        background=GREEN, foreground=WHITE, font=("bold", 30))
        self.button.pack(pady=(0, 20))

        # show roulette image
        # self.absolute_img_path = Path(r"E:\GameRoulette\PNG-Images\roulette-img2.png")
        # self.roulette_img = tk.PhotoImage(file=self.absolute_img_path)
        # self.label2 = tk.Label(self, image=self.roulette_img)
        # self.label2.pack(pady=(0, 20))


    
    def get_games(self):
        """Retrieve the games from steam library."""
        KEY = os.environ.get("STEAM_API_KEY")
        steam = Steam(KEY)
        all_games = steam.users.get_owned_games("76561198271994774")
        all_unplayed_games_ls = []

        for i in range(0, len(all_games['games'])):
            # filter out all the unplayed games:
            if all_games['games'][i]['playtime_forever'] == 0:
                all_unplayed_games_ls.append(all_games['games'][i]['name'])
        return all_unplayed_games_ls
    
    def list_games(self):
        """List all the games."""
        games = self.get_games()

        for game in games:
            print(f"{game}")
        print()
    
    def draw_wheel(self):
        """Draws the random wheel generator."""
        self.canvas.delete("slice")  # Clear old slices
        num_items = len(self.colors)
        slice_angle = 360 / num_items

        for i, item in enumerate(self.colors):
            start = self.current_angle + (i * slice_angle)
            extent = slice_angle
            color = self.colors[i % len(self.colors)]
            
            # Draw the pie slice
            self.canvas.create_arc(50, 50, 350, 350, start=start, extent=extent, 
                                   fill=color, outline="black", tags="slice")

            # Calculate text position
            angle_rad = math.radians(start + (slice_angle / 2))
            x = 200 + 120 * math.cos(angle_rad)
            y = 200 - 120 * math.sin(angle_rad)

            # Draw the text
            #self.canvas.create_text(x, y, text=item, font=("Arial", 12, "bold"), tags="slice")
    
    def spin(self):
        """Select a game randomly."""
        games = self.get_games()

        return print(f"PLAY!: {random.choice(games)}")
    
    def button_func(self):
        """Randomly select a game on button press."""
        games = self.get_games()
        self.string_var.set(f"PLAY!: {random.choice(games)}")
    


def main():
    print("Welcome to Game Roulette!!!")
    pick = GameRoulette()

    # run the app:
    pick.mainloop()
