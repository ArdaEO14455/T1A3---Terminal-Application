from functions import *
import pytest
from io import StringIO

adventurer = Adventurer("arda", 1, 1, 0, 1)
troll = Troll("troll", 1, 1, 0, 1)

#Test Adventurer Attacks

def test_fireball(monkeypatch):
    move_input = (StringIO('1')) #mocking valid input
    monkeypatch.setattr('sys.stdin', move_input)
    assert (65 <= adventurer.attack() <= 80)

def test_lightning(monkeypatch):
    move_input = (StringIO('2')) #mocking valid input
    monkeypatch.setattr('sys.stdin', move_input)
    assert (60 <= adventurer.attack() <= 90)

def test_life_drain(monkeypatch):
    move_input = (StringIO('3')) #mocking valid input
    monkeypatch.setattr('sys.stdin', move_input)
    assert (60 <= adventurer.attack() <= 80)

#Test Adventurer Heal

def test_self_heal():
    assert (40 <= adventurer.selfheal() <= 60)

#Test Troll Damage

def test_troll_damage():
    assert (15 <= troll.random_action() <= 35)
    
    
