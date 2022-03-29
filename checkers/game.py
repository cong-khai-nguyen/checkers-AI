import pygame
from .board import Board
from .constants import RED, WHITE

class Game:
    def __init__(self, window):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.window = window

    def update(self):
        self.board.draw(self.window)
        pygame.display.update()