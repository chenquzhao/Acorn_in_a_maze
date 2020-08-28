"""
A simple program that will import your tests and run them all!
Be sure you include tests for your other modules like cells and player!

Usage: python3 test_all.py
"""

import subprocess
from test_cell import run_tests as test_cell
from test_player import run_tests as test_player
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_run import run_tests as test_run

print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_cell()
test_player()
test_parser()
test_grid()
test_game()
test_run()

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
