from classes import *
import pytest
from io import StringIO

adventurer = Adventurer("arda", 1, 1, 1, 1)

#Exception Raise Test - Invalid Input is given to move_select function   
def test_move_select_raise_error(monkeypatch):
    move_input = (StringIO('2'))
    monkeypatch.setattr('sys.stdin', move_input)
    with pytest.raises(Exception):
        adventurer.move_select()

# Exception Raise Test - Invalid Input is given to attack() function - Fixed
def test_attack_select_raise_error(monkeypatch):
    move_input = (StringIO('2'))
    monkeypatch.setattr('sys.stdin', move_input)
    with pytest.raises(Exception):
        adventurer.attack()




# def test_double(monkeypatch):
#     number_inputs = (StringIO('1234\n'))
#     monkeypatch.setattr('sys.stdin', number_inputs)
#     assert Adventurer.double() == 2468


