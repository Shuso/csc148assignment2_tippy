from move import Move
# TippyMove is a subclass of Move

class TippyMove(Move):
    
    ''' A move in the tippy game.

    amount: int -- amount to subtract from current value.
    '''

    def __init__(self, position):
        ''' (TippyMove, int) -> NoneType

        Initialize a new TippyMove that to be marked on the board.

        Assume: position is a integer greater than 0, less than the (square of 
        
        length of board -1)
        '''
        self.position = position

    def __repr__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove.
        >>> m1 = TippyMove(4)
        >>> m1
        TippyMove(4)
        '''
        return 'TippyMove({})'.format(str(self.position))

    def __str__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove
        that is suitable for users to read.

        >>> m1 = TippyMove(4)
        >>> print(m1)
        Place on position 4
        '''

        return 'Place on position {}'.format(str(self.position))

    def __eq__(self, other):
        ''' (TippyMove, TippyMove) -> bool

        Return True iff this TippyMove is the same as other.

        >>> m1 = TippyMove(4)
        >>> m2 = TippyMove(3)
        >>> print(m1 == m2)
        False
        '''
        return (isinstance(other, TippyMove) and 
                self.position == other.position)


if __name__ == '__main__':
    import doctest
    doctest.testmod()