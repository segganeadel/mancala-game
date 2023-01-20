from mancalaboard import MancalaBoard
from game import Game
from play import Play
from Proprities import *
from pygame import draw,gfxdraw
from graph import *
from time import sleep


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def game_screen(game:Game):
    gs_surface = pygame.Surface(Dimension)
    while not game.gameOver():    


        gs_surface.fill(BLACK)
        draw_board(game,gs_surface)
        window.blit(gs_surface, (0,0))
        pygame.display.update()
        check_events()

        if game.playerSide == 1:
            Play.humanTurn(game)
        else:
            sleep(1)
            Play.computerTurn(game)

    gs_surface.fill(BLACK)
    draw_board(game,gs_surface)
    window.blit(gs_surface, (0,0))
    pygame.display.update()



board = MancalaBoard()
game = Game(board, 1)

pygame.init()
window = pygame.display.set_mode(Dimension)

window.fill(WHITE)

#Game screen
game_screen(game)

#Menu


print("winner is Player: ",game.findWinner())
print(game.state)

while True:
    check_events()


