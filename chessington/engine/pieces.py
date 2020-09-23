"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board):
        moves = []
        square_on_board = board.find_piece(self)

        #pawns cannot move through obstructions:
        if self.player == Player.WHITE:
            square_one_in_front = Square.at(square_on_board.row + 1, square_on_board.col)
        else:
            square_one_in_front = Square.at(square_on_board.row - 1, square_on_board.col)

        if board.get_piece(square_one_in_front) is None:
            self.single_move(moves, square_on_board)
            if (square_on_board.row == 1 and self.player == Player.WHITE) or (square_on_board.row == 6 and self.player == Player.BLACK):
                self.double_move(moves, square_on_board)
        return moves

    def single_move(self, moves, square_on_board):
        if self.player == Player.WHITE:
            moves.append(Square.at(square_on_board.row + 1, square_on_board.col))
        else:
            moves.append(Square.at(square_on_board.row - 1, square_on_board.col))

    def double_move(self, moves, square_on_board):
        if self.player == Player.WHITE:
            moves.append(Square.at(square_on_board.row + 2, square_on_board.col))
        else:
            moves.append(Square.at(square_on_board.row - 2, square_on_board.col))



class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []