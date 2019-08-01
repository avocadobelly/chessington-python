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

        #If the pawn has reaches the other side of the board then there are no legal moves left
        if (self.player == Player.WHITE and square_on_board.row == 7) or (self.player == Player.BLACK and square_on_board.row == 0):
           return moves

        #If the square in front of the piece is empty then moving one space is legal
        if board.get_piece(self.x_squares_in_front(square_on_board, 1)) is None:
            self.move_x_times(moves, square_on_board, 1)
            # If it's the first time the pawn has moved then moving two spaces is legal
            if (square_on_board.row == 1 and self.player == Player.WHITE) or (square_on_board.row == 6 and self.player == Player.BLACK):
                self.move_x_times(moves, square_on_board, 2)

        capturable_squares = self.one_square_in_front_digaonally(square_on_board)
        diagonal_square_1 = capturable_squares[0]
        diagonal_square_2 = capturable_squares[1]

        if self.is_piece_on_diagonal(board, diagonal_square_1) and self.is_opposing_piece(board.get_piece(diagonal_square_1)):
            moves.append(diagonal_square_1)
        if self.is_piece_on_diagonal(board, diagonal_square_2) and self.is_opposing_piece(board.get_piece(diagonal_square_2)):
            moves.append(diagonal_square_2)
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

    def one_square_in_front_digaonally(self, square_on_board):
        capturable_squares = []
        if self.player == Player.WHITE:
            capturable_squares.append(Square.at(square_on_board.row + 1, square_on_board.col + 1))
            capturable_squares.append(Square.at(square_on_board.row + 1, square_on_board.col - 1))
        else:
            capturable_squares.append(Square.at(square_on_board.row - 1, square_on_board.col + 1))
            capturable_squares.append(Square.at(square_on_board.row - 1, square_on_board.col - 1))
        return capturable_squares

    def is_opposing_piece(self, piece):
        if piece.player == self.player:
            return False
        else:
            return True

    def is_piece_on_diagonal(self, board, square):
        if not board.get_piece(square):
            return False
        else:
            return True

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