from game_state import GameState
from tippy_move import TippyMove   

class TippyGameState(GameState):
    
    ''' The state of a tippy game

    board: int   --- the latest move applied
    '''
    # assign class constants
   
    size = int(input('enter the board length (>=3):'))

    def __init__(self, p, interactive = False,
                            board = ['-' for i in range(size**2)]):
        ''' (TippyGameState, int, str) -> NoneType

        Initialize TippyGameState self with empty board to 
        fill the tippy shape.

        Assume: board is a n * n board
                p in {'p1', 'p2'}
        '''
        if interactive:
            return board

        GameState.__init__(self, p)  
        self.board = board
        self.over = self.is_gameover()
        self.instructions = ('On your turn, choose position on the board as'
                             'as long as the position has not been taken'
                             'the objective of this game is to form a tippy'
                             'enter number between 0 to (board-length**2-1)')
                             
                            

    def __repr__(self):
        ''' (TippyGameState) -> str

        Return a string representation of TippyGameState self
        that evaluates to an equivalent TippyGameState

        >>> s = TippyGameState('p1', board =['-', '-', '-', '-', '-', '-', '-',\ 
        '-', '-', '-'])
        >>> s
        TippyGameState('p1', 17)
        '''
        return 'TippyGameState({}, {})'.format(repr(self.next_player),
                                                    repr(self.board))

    def __str__(self):
        ''' (TippyGameState) -> str

        Return a convenient string representation of TippyGameState self.

        >>> s = TippyGameState('p1', board =['-', '-', '-', '-', '-', '-', '-',\ 
        '-', '-', '-']) 
        >>> print(s)
        ['-', '-', '-']
        ['-', '-', '-']
        ['-', '-', '-']
        
        Current board: ['-', '-', '-', '-', '-', '-', '-',\ 
        '-', '-', '-']; next player: p1
        '''
        self.print_board()
        print()
        return ('Current board: {}; next player: {}'.format(
            str(self.board), str(self.next_player)))

    def __eq__(self, other):
        ''' (TippyGameState, TippyGameState) -> bool

        Return True iff this TippyGameState is the equivalent to other.

        >>> s1 = TippyGameState('p1', current_board=['-', '-', '-', '-', '-', 
        '-', '-','-', '-', '-'] )
        >>> s2 = TippyGameState('p1', current_board=['-', '-', '-', '-', '-', 
        '-', '-','-', '-', '-']) ))
        >>> s1 == s2
        True
        '''
        return (isinstance(other, TippyGameState) and
                self.board == other.board and
                self.next_player == other.next_player)

    def apply_move(self, move):
        ''' (TippyGameState, TippyMove) -> TippyGameState

        Return the new TippyGameState reached by applying move to self.

        >>> s1 = TippyGameState('p1', current_board)
        >>> s2 = s1.apply_move(TippyMove(8))
        >>> print(s2)
        
        '''
        if move in self.possible_next_moves():
            upd_board = self.mark(move) 
            return TippyGameState(self.opponent(),upd_board)
                                       
        else:
            return None

    def rough_outcome(self):
        '''(TippyGameState) -> float

        Return an estimate in interval [LOSE, WIN] of best outcome next_player
        can guarantee from state self. p.s this is a really crude rough outcome
        if there is if you win, you get 1, if there are more moves to win you 
        get -1.
                
        '''
        if self.winner(player):
            return TippyGameState.WIN
        elif len(self.possible_next_moves) > 0:
            return TippyGameState.LOSE
        else:
            return TippyGameState.DRAW

    def get_move(self):
        '''(TippyGameState) -> TippyMove

        Prompt user and return move.
        '''
        return TippyMove(int(input('Your turn( 0 to n*n -1):  ')))

    def winner(self, player):
        ''' (TippyGameState, str) -> bool

        Return True iff the game is over and player has won.

        Preconditions: player is either 'p1' or 'p2'
        '''
        L = self.get_win_positions(size)
        for w,s,a,d in L:
            if (self.board[w] == self.board[s] == self.board[a] == self.board[d]
                and self.board[d]!='-' and self.opponent() == player):
                
                return True
            
        return False  
    
    def is_gameover(self):
        '''(TippyGameState) ->None
        
        Return whether the game is over
        '''
        if self.winner('p1') or self.winner('p2'):
            self.over = True
        elif '-' not in self.board:
            self.over = True
        else:
            self.over = False
        
        return self.over
            



    def possible_next_moves(self):
        ''' (TippyGameState) -> list of TippyMove

        Return a (possibly empty) list of moves that are legal
        from the present state.

        >>> s1 = TippyGameState('p1', board=['-', '-', '-', '-', '-', '-', '-', 
        '-', '-', '-']
        >>> L1 = s1.possible_next_moves()
        >>> L2 = [TippyMove(0), TippyMove(1), TippyMove(2), TippyMove(3)
        TippyMove(4), TippyMove(5), TippyMove(6), TippyMove(7), TippyMove(8)]
        >>> len(L1) == len(L2) and all([m in L2 for m in L1])
        True
        '''
        return [TippyMove(i)
                    for i in range(len(self.board))
                    if self.board[i] == '-']        

    def marker(self):
        '''(TippyGameState) -> str 
        Assign the marker to the player
        '''
        if player == 'p1':    
            return 'X'
        elif player == 'p2':
            return 'O'
    
    
    
    def print_board(self):   
        """(TippyGameState) -> None
        
        Print the board
        """
        h,t = 0,self.size
        while t<= self.size**2:
            print(self.board[h:t])
            h+=size
            t+=size    

    def mark(self,m):
        '''(TippyGameState, TippyMove) -> TippyGameState
        
        Return a updated board with a new move mark on it
    
        '''
        b= self.board[:]
        b[m.position] = marker(self.next_player)
        return b

    def get_win_positions(self):
        """(TippyGameState) -> list of int
        
        Return a list of winning combo
        
        
        """
        s = self.size
        sp1 = []   # z 
        sp2 = []   # s 
        sp3 = []   # N_left
        sp4 = []   # N_right  
        winning_combo = []
        for i in range(s**2 -1):
            if (i+s+2) <= (s**2-1)and (i+1)% s != 0 and (i+1+1)%s!=0:
                sp1.append((i,i+1,i+s+1,i+s+2))
            if (i+s-1)<= (s**2-1) and i%s!=0 and (i+1)% s!=0:
                sp2.append((i,i+1,i+s,i+s-1))
            if (i+2*s+1)<=(s**2-1) and (i+1)%s!=0:
                sp3.append((i,i+s,i+s+1,i+2*s+1))
            if (i+2*s-1)<=(s**2-1) and i%s!=0:
                sp4.append((i,i+s,i+s-1,i+2*s-1))
                winning_combo = sp1 + sp2 + sp3 + sp4
        return winning_combo        

if __name__ == '__main__':
    import doctest
    doctest.testmod()