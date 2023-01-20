
from pygame import draw,gfxdraw,Rect
from Proprities import *
from game import Game
from mancalaboard import MancalaBoard

def draw_current_player(game:Game,surface):
    text = f"Current player {game.playerSide}"
    text_surface = textFont.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (100 , 50)
    surface.blit(text_surface,text_rect)


def draw_pits(game:Game,surface):

    stepH = Width/6
    for pit in game.state.fosse2:
        stepH += Width/10.5
        text = str(game.state.board[pit])
        text_surface = numberFont.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (stepH,Height/2-50)
        surface.blit(text_surface,text_rect)
        draw.circle(surface,WHITE,text_rect.center,Radius,2)

    stepH = Width/6
    for pit in game.state.fosse1:
        stepH += Width/10.5
        text = str(game.state.board[pit])
        text_surface = numberFont.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (stepH,Height/2+50)
        surface.blit(text_surface,text_rect)
        draw.circle(surface,WHITE,text_rect.center,Radius,2)
        


def draw_stores(game:Game,surface):

    text = str(game.state.board['2'])
    text_surface = numberFont.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (Width/6,Height/2)
    surface.blit(text_surface,text_rect)

    store_rect = Rect(100,200,100,200)
    store_rect.center = text_rect.center
    draw.rect(surface,WHITE,store_rect,2)

    text = str(game.state.board['1'])
    text_surface = numberFont.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (Width-Width/6,Height-Height/2)
    surface.blit(text_surface,text_rect)

    store_rect.center = text_rect.center
    draw.rect(surface,WHITE,store_rect,2)


def draw_board(game:Game,surface):

    draw_current_player(game,surface)
    draw_stores(game,surface)
    draw_pits(game,surface)

def get_pit_choice(game:Game):
    legal_moves = game.state.possibleMoves(1)
    while True:
        check_events()
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            stepH = Width/6
            for pit in MancalaBoard.fosse1:
                stepH += Width/10.5
                if pit in legal_moves:
                    rect = Rect(stepH-Radius,Height/2+50-Radius,Radius*2,Radius*2)
                    if rect.collidepoint(position):
                        return pit

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
