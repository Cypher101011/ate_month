import sys
import pygame

class AlienInvasion:
    '''overall class to manage game assets and behaviour'''
    def __init__(self):
        '''Initialize the game, and create game reasourses'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))

    def run_game(self):
        '''start the main loop for the game'''
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exist()
            

            # Make the most recently drawin screeen visible
            pygame.display.flip()

if __name__=='__main__':
    #make a game instances and run the game
    ai = AlienInvasion()
    ai.run_game()

