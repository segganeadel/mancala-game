
class MancalaBoard:
    fosse1=('A', 'B', 'C', 'D', 'E', 'F')

    fosse2=('G', 'H', 'I', 'J', 'K', 'L')

    nextFosse = {'A':'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'1', '1':'L', 
                    'L':'K', 'K':'J', 'J':'I', 'I':'H', 'H':'G','G':'2', '2':'A'}

    opposite = {'A':'G', 'B':'H', 'C':'I', 'D':'J', 'E':'K','F':'L', 
                'G':'A', 'H':'B', 'I':'C', 'J':'D','K':'E', 'L':'F'}

    def __init__(self):
        self.board={"A":4, "B":4, "C":4, "D":4, "E":4, "F":4,
                    "G":4, "H":4, "I":4, "J":4, "K":4, "L":4,
                    "1":0, "2":0}
    
    # mouvements possibles
    # retourne une list des codes ASCII des fosses
    def possibleMoves(self,player:int):
        Moves = []
        if player == 1:
            for c in MancalaBoard.fosse1:
                if self.board[c] !=0:
                    Moves.append(c)
        elif player == 2 :
            for c in MancalaBoard.fosse2:
                if self.board[c] !=0:
                    Moves.append(c)
        return Moves

    def doMove(self, player, position):

        graines = self.board[position]
        self.board[position] = 0
        while graines > 0:

            position = MancalaBoard.nextFosse[position] 
            if (player == 1 and position == '2') or (player == 2 and position == '1'):
                continue

            self.board[position] += 1
            graines -= 1
            
            if graines == 0:
                if (position == str(player) == '1') or (position == str(player) == '2'):
                    return player
                if self.board[position] == 1 and self.board[MancalaBoard.opposite[position]] != 0:
                    if player == 1 and position in MancalaBoard.fosse1 :
                        oppositeFosse = MancalaBoard.opposite[position]
                        self.board['1'] += self.board[oppositeFosse]+1
                        self.board[oppositeFosse] = 0
                        self.board[position] = 0
                    elif player == 2 and position in MancalaBoard.fosse2 :
                        oppositeFosse = MancalaBoard.opposite[position]
                        self.board['2'] += self.board[oppositeFosse]+1
                        self.board[oppositeFosse] = 0 
                        self.board[position] = 0               
        if player == 1:
            return 2
        if player == 2:
            return 1


    def __str__(self):
        """Render the game board along with the number of seeds and indices of each pit"""
        board = "\n         G   H   I   J   K   L\n   |===============================|\n   "
        board += "|---| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}|---|".format(
            self.board['G'], self.board['H'], self.board['I'],
            self.board['J'], self.board['K'], self.board['L'])
        board += f"\n2  |{self.board['2']:>2} |=======================| {self.board['1']:<2}| 1"
        board += "\n   |---| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}|---|\n   ".format(
            self.board['A'], self.board['B'], self.board['C'],
            self.board['D'], self.board['E'], self.board['F'])
        board += "|===============================|\n         A   B   C   D   E   F\n"
        return board
