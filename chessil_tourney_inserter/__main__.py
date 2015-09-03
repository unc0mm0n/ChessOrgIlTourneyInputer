import chessil_tourney_inserter as cti
import sys

if len(sys.argv) == 1:
    print("Usage: chessil_tourney_inserter.py *tournament name*")
    exit()
cti.main(sys.argv);
    