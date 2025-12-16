import pygame
import os

class Scoreboard:
    '''handle rendering and storing the score & high score'''
    def __init__(self,game,font_path=None,size=28,color=(255,255,255)):
        self.game=game
        self.screen=game.screen
        self.screen_rect =self.screen.get_rect()
        self.settings=game.settings
        self.color =color

        # scorevalues
        self.score =0
        self.high_score=0
        self.score_str="Score:0"
        self.highscore_file='highscore.txt'

        try:
            if font_path and os.path.exist(font_path):
                self.font=pygame.font.Font(font_path,size)
            else:
                self.font = pygame.font.SysFont(None,size)
        except:
            self.font =pygame.font.SysFont(None,size)
        
        #prepare initial images
        self.prep_score()
        self._load_high_score()

    def prep_score(self):
        '''create image for the score text'''
        self.score_str=f"Score: {self.score}"
        self.score_image=self.font.render(self.score_str,True,self.color)
        padding=12

        self.score_rect=self.score_image.get_rect()
        self.score_rect.top =padding
        self.score_rect.right=self.screen_rect.right-padding
        self.high_score_image=self.font.render(f"High: {self.high_score}",True,self.color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.top=self.score_rect.bottom+6
        self.high_score_rect.right=self.screen_rect.right-padding

    def increase(self,amount=10):
        self.score+=amount
        if self.score>self.high_score:
            self.high_score=self.score
        self.prep_score()
    def draw(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
    def _load_high_score(self):
        if os.path.exists(self.highscore_file):
            try:
                with open(self.highscore_file,'r') as f:
                    val =f.read().strip()
                    self.high_score=int(val) if val.isdigit() else 0
            except Exception:
                self.high_score=0
            self.prep_score()
    def save_high_score(self):
        try:
            with open(welf.highscore_file,'w') as f:
                f.write(str(self.high_score))
        except Exception:
             pass
