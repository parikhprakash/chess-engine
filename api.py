from fastapi import FastAPI, Request
from pydantic import BaseModel
import chess
import chess.engine

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:5500"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to your stockfish binary
STOCKFISH_PATH = "/usr/games/stockfish"  # change this

# Create engine
# engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

import stockfish
engine = stockfish.Stockfish(path="/usr/games/stockfish",depth=15)
engine.set_elo_rating(1500)
class FENRequest(BaseModel):
    fen: str

class EloRequest(BaseModel):
    elo: int

@app.post("/set-elo")
async def set_elo(req: EloRequest):
    try:
        engine.set_elo_rating(req.elo)
        return {"status": "Elo Has been updated"}
    except:
        return {"status": "Failed to set Elo"}



@app.post("/best-move")
async def best_move(req: FENRequest):
    board = chess.Board(req.fen)
    engine.set_fen_position(board.fen())
    # result = engine.play(board, chess.engine.Limit(time=0.1))
    return {"best_move": engine.get_best_move()}
