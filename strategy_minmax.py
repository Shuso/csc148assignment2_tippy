from strategy import Strategy

class StrategyMinimax(Strategy):

    
    

    '''Interface to suggest the best possible moves .
    '''

    def suggest_move(self, state):   
        '''(StrategyMinimax, GameState) -> Move

        Return a strongest possible move from those available for state.

        Overrides Strategy.suggest_move
        '''
        return self.minimax(state)[0]
    
  
     
   
    def base_case(self,state):
        """(StrategyMinimax, GameState) -> bool
        
        Return whether the gamestate reaches the end of game
        (base case of the recursive code)
        """
        max_score = None
        max_move = None        
        move_dict = {}
       
        for m in state.possible_next_moves():
            s = state[:]    # make a copy
            s = state.apply_move  #  simulate a move
            if s.over():  #  whether the move reach the end of the game 
                score = s.outcome()
                move_dict[m] = score   # build a dict of {TippyMove: int}
            else:
                return None
        if len(move_dict) != 0:        # make sure the dictionary is non-empty 
            max_score = max([v for v in move_dict.values()]) # get max_score
            for k in move_dict.keys():  # max_move corresponding to max_score
                if move_dict[k] == max_score:
                    max_move = k
            
            return True
        else:
            return False  
        
    def minimax(self,state):
        ''' (StrategyMinimax, GameState) -> list of [TipppyMove,int]  
        
        Find the max_move and max_score
        
        '''            
        if self.base_case(state):
            return [max_move, max_score]
        else: 
            return self.minimax(state) 