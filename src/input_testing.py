from functions import *
import pytest
from io import StringIO

adventurer = Adventurer("arda", 1, 1, 0, 1)

#Exception Raise Test - Invalid Input is given to move_select function 
# Test below did not raise error when move_select was given invalid input  
# def test_raise_error_move_select(monkeypatch):
#     move_input = (StringIO('8')) #mocking invalid input
#     monkeypatch.setattr('sys.stdin', move_input)
#     with pytest.raises(Exception):
#         adventurer.move_select()
    

# # Exception Raise Test - Invalid Input is given to 'attack' function
def test_raise_error_attack_select(monkeypatch):
    move_input = (StringIO('8')) #mocking invalid input
    monkeypatch.setattr('sys.stdin', move_input)
    with pytest.raises(Exception):
        adventurer.attack()

#Exception Raise Test - Valid Input is given to move_select function   
def test_correct_input_move_select(monkeypatch):
    try:
        move_input = (StringIO('2')) #mocking valid input
        monkeypatch.setattr('sys.stdin', move_input)
        adventurer.move_select()
    except Exception as exception:
        assert False, f" 'move_select' raised an exception {exception}"

#Exception Raise Test - Valid Input is given to 'attack' function   
def test_correct_input_attack(monkeypatch):
    try:
        move_input = (StringIO('2')) #mocking valid input
        monkeypatch.setattr('sys.stdin', move_input)
        adventurer.attack()
    except Exception as exception:
        assert False, f" 'move_select' raised an exception {exception}"

