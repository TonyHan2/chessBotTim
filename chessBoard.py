import chess
import random

#from randomPlayer import botMove

#CONSULT DE ORACLE
#https://www.chessprogramming.org/Main_Page
#https://python-chess.readthedocs.io/en/latest/

board = chess.Board(
    ' rnbqkbnr'
    '/pppppppp'
    '/8'
    '/8'
    '/8'
    '/8'
    '/PPPPPPPP'
    '/RNBQKBNR'
    ' w KQkq - 0 1'
    )
peices = ['r','n','b','q','k','p','R','N','B','Q','K','P']

def printBoard(board):
    print("\u0332".join("  A B C D E F G H"))
    rowNum = 8
    board = board.board_fen()
    board = board.split("/")
    for row in board:
        print(str(rowNum)+"|",end="")
        rowNum-=1
        for item in row:
            if item in peices:
                print("\u0332".join(item+"|"),end="")
            else:
                print("\u0332".join("_|"*int(item)),end="")
        print()

playerColor = False

import randomPlayer

run = True
while run:
    printBoard(board)
    if board.color_at == playerColor:
        print('player')
        move = input()
    else:
        move = randomPlayer.botMove(board)
        move = str(random.choice(list(board.legal_moves)))

    move = chess.Move.from_uci(move)
    if move in board.legal_moves:
        board.push(move)
        if board.is_checkmate():
            print("checkmate")
            run = False
        if board.is_stalemate():
            print("stalemate")
            run = False
        if board.is_insufficient_material():
            print("insufficient")
            run = False
    else:
        print("INVALID")
        run = False