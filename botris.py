import pygame
import numpy as np
import gamesettings

class BotrisGame(object):
        
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.human_player = False
        pygame.display.set_caption("Botris")
        self.grid = np.zeros(gamesettings.GRID_DIM, dtype = int)
        print(self.grid)

    def create_players(self, genomes = None, config = None):
        if genomes is not None and config is not None:
            for g in genomes:
                pass   
        else:      
            pass
    

    def play(self):
        running = True
        # ************************* MAIN LOOP *******************************
        while running:
            self.clock.tick(gamesettings.FPS)
            print(self.grid)
            pass
        # *******************************************************************
        
    def draw_grid(self, screen, grid):
        pass

        
if __name__ == "__main__":
    game = BotrisGame()
    game.human_player = True
    game.create_players()
    game.play()   