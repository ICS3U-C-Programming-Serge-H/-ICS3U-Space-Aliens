#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program is the Space Aliens program in python

import ugame
import stage

def game_scene():
    # this function is the main game game_scene
    
    image_bank_background = stage .Bank. from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60 )
    game.layers = [background]
    game.render_block()

    print("Hello, Serge!")
    print("Hello, welcome to my Domain mortal!")

    # repeat forever, game loop
    while True:
        pass # just a placeholder for now

if __name__ == "__main__":
    game_scene()