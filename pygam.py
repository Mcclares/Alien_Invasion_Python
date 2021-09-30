import pygame as py
import sys

def run_game():
    py.init()
    screen = py.display.set_mode((1200,800))
    while (True) :
        for event in py.event.get():
            if(event.type == py.QUIT):
                sys.exit()
            screen.fill((230,230,230))
            if(event.type == py.KEYDOWN):
                print(event.key)
        py.display.flip()

run_game()