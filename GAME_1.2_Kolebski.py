#Importieren der Bibliotheken:
import pygame, random, os
 
pygame.init()

class Settings(object):
    width = 400                                                       #Die breite des Fensters
    height = 500                                                      #Die höhe des Fensters
    imagewidth = 50
    imageheight = 50
    fps = 60       
    title = "GAME_1.2_KOLEBSKI" 
    file_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images")
    bordersize = 20
    Black = (0,0,0)
    White = (255,255,255)
    Red = (255,0,0)
    Green = (0,255,0)
    Blue = (0,0,255)
    @staticmethod
    def get_dim():
        return (Settings.width, Settings.height)

class Figur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.images_path, "bot.bmp")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Settings.imagewidth, Settings.imageheight))
        self.rect = self.image.get_rect()
        self.rect.left = (Settings.width - self.rect.width) // 2
        self.rect.bottom = Settings.height - Settings.bordersize
        self.direction = 0
        self.speed = 5
    
    def update(self):
        self.rect.left += (self.direction * self.speed)
        if self.rect.right >= Settings.width - Settings.bordersize:
            self.direction = 0
        elif self.rect.left <= Settings.bordersize:
            self.direction = 0

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.get_dim())
        pygame.display.set_caption(Settings.title)
        self.background = pygame.image.load(os.path.join(Settings.images_path, "blacc.bmp")).convert()
        self.background = pygame.transform.scale(self.background, (Settings.width, Settings.height))
        self.background_rect = self.background.get_rect()
        self.clock = pygame.time.Clock()
        self.done = False
        self.all_figuren = pygame.sprite.Group()
        self.Figur = Figur()
        self.all_figuren.add(self.Figur)

    def run(self):
        while not self.done:               
            self.clock.tick(Settings.fps)             
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:   
                    self.done = True  
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                    elif event.key == pygame.K_LEFT:
                        self.Figur.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.Figur.direction = 1
                    elif event.key == pygame.K_SPACE:
                        pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Figur.direction = 0
                    elif event.key == pygame.K_RIGHT:
                        self.Figur.direction = 0
                    elif event.key == pygame.K_SPACE:
                        pass
            self.screen.blit(self.background, self.background_rect)
            self.all_figuren.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':      
                                    
    pygame.init()               
    game = Game()
    game.run()
    pygame.quit()
