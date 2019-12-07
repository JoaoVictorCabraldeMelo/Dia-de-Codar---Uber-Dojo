import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')  # pytest conseguir ver os imports do src
from src.numberwords import Converter
import src.numberwords


def test_unit_translation():
    converter = Converter()
    unit_text = converter.run(2)
    assert unit_text == "two"


def test_should_return_word_for_the_given_number():
    controller = Converter()
    word = controller.run(42)
    assert word == "forty two dollars"


def test_should_return_word_for_the_given_number_2():
    controller = Converter()
    word = controller.run(45)

    assert word == "forty five dollars"


def test_should_return_word_for_the_given_number_ending_with_zero():
    controller = Converter()
    word = controller.run(40)

    assert word == "forty dollars"
