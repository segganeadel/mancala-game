from mancalaboard import MancalaBoard
from copy import deepcopy

class Game:
    def __init__(self, mancalaBoard:MancalaBoard, player:int, heuristic = None):
        self.state = mancalaBoard
        self.playerSide = player
        self.heuristic = heuristic

    def gameOver(self):
        if not self.state.possibleMoves(1):
            for fosse in MancalaBoard.fosse2:
                self.state.board['1'] += self.state.board[fosse]
                self.state.board[fosse] = 0
            return True
        if not self.state.possibleMoves(2):
            for fosse in MancalaBoard.fosse1:
                self.state.board['2'] += self.state.board[fosse]
                self.state.board[fosse] = 0
            return True
        return False

    def findWinner(self):
        if self.state.board['1'] > self.state.board['2']:
            return 1, self.state.board['1']
        else: 
            return 2, self.state.board['2']

    def evaluate(self):
        #H4
        store = self.state.board[str(self.playerSide)]
        
        #H2
        sum_pits = 0
        for pit in self.state.fosse1 if self.playerSide == 1 else self.state.fosse2:
            sum_pits += self.state.board[pit]
        
        #H3
        max_pos_moves = len(self.state.possibleMoves(self.playerSide))
        
        #H6
        if self.playerSide == 1:
            min_opponent = -self.state.board['2']
        else:
            min_opponent = -self.state.board['1']

        self.heuristic = 1*store+0.3*sum_pits+0.4*max_pos_moves+0.5*min_opponent
        
        if self.playerSide == 1:
            self.heuristic = -self.heuristic

        return self.heuristic

    def ordered_children(self):
        children = []
        
        for move in self.state.possibleMoves(self.playerSide):
            clone_game = deepcopy(self)
            clone_game.playerSide = clone_game.state.doMove(self.playerSide, move)
            clone_game.replay = 1 if self.playerSide == clone_game.playerSide else 0
            clone_game.move = move
            clone_game.evaluate()

            children.append(clone_game)

        rev = True if self.playerSide == 2 else False
        children.sort(key=lambda x: x.heuristic, reverse=rev)
        children.sort(key=lambda x: x.replay, reverse=True)
        #print([game.heuristic for game in children],rev)
        children = [game.move for game in children]
        #print(children)
        return children


