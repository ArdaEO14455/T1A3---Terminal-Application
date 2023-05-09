from classes import Adventurer
import pytest
from io import StringIO


move_input = StringIO('5')

def test_move_select_raise_error(monkeypatch):
    with pytest.raises(Exception):
        monkeypatch.setattr('sys.stdin', move_input)
        Adventurer.move_select()

def test_attack_select_raise_error(monkeypatch):
    with pytest.raises(Exception):
        monkeypatch.setattr('sys.stdin', move_input)
        Adventurer.attack()
        




        
        