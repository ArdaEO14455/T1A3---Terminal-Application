import main
from classes2 import Adventurer
import pytest
from main2 import *
from io import StringIO


# def test_loop_break():
#     with main.adventurer.health < 0:
        

# def test_attack_select_raise_error():
#     with pytest.raises(NameError or TypeError or Exception):
#         Adventurer.attack()

move_input = StringIO('5')
choose_move = StringIO('5')

def test_move_select_raise_error(monkeypatch):
    with pytest.raises(Exception):
        monkeypatch.setattr('sys.stdin', move_input, choose_move)
        adventurer.move_select()
        

# def test_move_select_raise_error():
#     with pytest.raises(NameError or TypeError or Exception):
#         throwsomeerror()


# def test_division_raise_error():
#     with pytest.raises(Exception):
#         division(10, 0)

def test_move_select_raise_errror():
    with pytest.raises(Exception):


        
        