import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')  # pytest conseguir ver os imports do src
from src.numberinwords import *


def test_should_return_number_in_extension():
    conveter = Converter()
    number = conveter.run(42)
    assert number == "forty two dollars"


def test_should_return_number_unit():
    converter = Converter()
    unidade = converter.unidade(195)
    assert unidade == "five dollars"


def test_should_return_number_ten_to_twenty():
    converter = Converter()
    dezena = converter.dezena(14)
    assert dezena == "fourteen dollars"
