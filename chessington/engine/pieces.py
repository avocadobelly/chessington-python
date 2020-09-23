"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod
from typing import List, Any

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
        moves: List[Any] = []
        square_on_board = board.find_piece(self)

        if board.get_piece(self.x_squares_in_front(square_on_board, 1)) is None:
            self.move_x_times(moves, square_on_board, 1)
            if (square_on_board.row == 1 and self.player == Player.WHITE) or (square_on_board.row == 6 and self.player == Player.BLACK):
                self.move_x_times(moves, square_on_board, 2)
        return moves

    def x_squares_in_front(self, square_on_board, x_squares):
        if self.player == Player.WHITE:
            num_of_squares_in_front = Square.at(square_on_board.row + x_squares, square_on_board.col)
        else:
            num_of_squares_in_front = Square.at(square_on_board.row - x_squares, square_on_board.col)
        return num_of_squares_in_front

    def move_x_times(self, moves, square_on_board, x_times):
        if self.player == Player.WHITE:
            moves.append(Square.at(square_on_board.row + x_times, square_on_board.col))
        else:
            moves.append(Square.at(square_on_board.row - x_times, square_on_board.col))


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