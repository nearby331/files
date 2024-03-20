import json
import os
from time import sleep
from keyboard import is_pressed as key

class Game():
    def __init__(self):
        self.PLAYER_IMAGE = "@"
        self.WALK_UP = False
        self.WALK_DOWN = False
        self.WALK_LEFT = False
        self.WALK_RIGHT = False
        self.FON = [
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
        ]
        self.PLAYER = {
                       "img": "@",
                       "x": 0,
                       "y": 0
                       }
    
    def set(self,x: int,y: int,image: str):
        self.OUTPUT_IMAGE[y][x] = image
    
    def checkPress(self):
        self.WALK_LEFT = False
        self.WALK_RIGHT = False
        self.WALK_UP = False
        self.WALK_DOWN = False
        if key('w'):
            self.WALK_UP = True
        elif key('s'):
            self.WALK_DOWN = True
        if key('a'):
            self.WALK_LEFT = True
        elif key('d'):
            self.WALK_RIGHT = True

    def checkALL(self):
        self.checkPress(self)
        self.set(self,self.PLAYER["x"],self.PLAYER["y"])


    def drawALL(self):
        os.system("cls||clear")
        for line_words in self.FON:
            for word in line_words:
                print(word, end="")
            print("\n", end="")

        self.FON = [
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
            [" "," "," "," "," "," "]
        ]

    def run(self):
        self.checkALL(self)
        self.drawALL(self)
        sleep(0.01)