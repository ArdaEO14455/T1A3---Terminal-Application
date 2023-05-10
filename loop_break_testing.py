from classes import *
from main import fight
import pytest
from io import StringIO

def test_raise_error_move_select(monkeypatch):
    name = 'adventurer'
    move_input = (StringIO('3')) #mocking invalid input
    monkeypatch.setattr('sys.stdin', name, move_input, move_input)
    with pytest.raises(Exception):
        fight()