import chess
import random

board = chess.Board()

print(list(board.legal_moves))
print(random.choice(list(board.legal_moves)))