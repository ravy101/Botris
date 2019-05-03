import pygame
import gamesettings

class BotrisGame(self):
        
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Botris")

    def create_players(self, genomes = None, config = None):
        if genomes is not None and config is not None:
                for g in genomes:
                    pass   
            else:      
                pass

    def play(self):
        running = True
        scroll_speed_boost = 0
        # ************************* MAIN LOOP *******************************
        while running:
            pass
        # *******************************************************************
        

        
if __name__ == "__main__":
    game = HopperGame()
    game.human_player = True
    game.create_players()
    game.play()   