import logging
import random
import sys

import chess

logger = logging.getLogger("MarcoEngine")

def print_l(msg, type="INFO"):
    if type == "INFO":
        logger.info(msg)

    elif type == "WARN":
        logger.warning(msg)

    elif type == "ERROR":
        logger.error(msg)

    elif type == "CRITICAL":
        logger.critical(msg)
        sys.exit(1)

def create_file(name):
    open(name, "w")

    return open(name, "r")


def new_board(old_board, fen: str = None):
    del old_board

    if not fen is None:
        n_board = chess.Board(fen)

        return n_board

    else:
        n_board = chess.Board()

        return n_board


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def calculate_time(wtime, btime, depth):
    if wtime <= 1000 and btime >= 1000:
        return "0.{}".format(int(depth // 4))

    elif wtime <= 1000 and btime <= 1000:
        return "0.".format(int(depth // random.randint(3, 5)))

    else:
        return "0.".format(int(depth // random.randint(5, 9)))
