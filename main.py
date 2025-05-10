import chess
import chess.svg
import stockfish
engine = stockfish.Stockfish(path="/usr/games/stockfish",depth=10)
engine.set_elo_rating(2550)
def main():
    print("Hello from chess-engine!")
    board = chess.Board()
    # print(board)
    engine.set_fen_position(board.fen())
    best_move = engine.get_best_move()
    print(best_move)
    board.push(chess.Move.from_uci(best_move))
    print(board)


if __name__ == "__main__":
    main()
