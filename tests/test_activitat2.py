import pytest

import src.activitat_2 as activitat_2

def test_es_primo_1():
    assert activitat_2.es_primo(1) == False

def test_es_primo_numero_primo():
    assert activitat_2.es_primo(2) == True

def test_es_primo_negativo():
    assert activitat_2.es_primo(-10) == False

def test_es_primo_numero_primo_mayor_2():
    assert activitat_2.es_primo(29) == True
