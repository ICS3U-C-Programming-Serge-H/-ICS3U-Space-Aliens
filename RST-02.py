#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: March 24, 2025
# This program is the Space Aliens program in python

import ugame
import stage


def game_scene():
    # this function is the main game game_scene

    # image bank for CicruitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # sets the backround to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # sets the backround to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the backround and initial location of sprite list
    # most likely you will only render backround once per scene
    game.render_block()

    print("Hello, welcome to my Domain mortal!")

    # repeat forever, game loop
    while True:
        pass  # just a placeholder for now


if __name__ == "__main__":
    game_scene()
