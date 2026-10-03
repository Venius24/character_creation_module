import os
from unittest.mock import patch

from main import Mage, choice_char_class, start_training


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['main.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f'Файл `{filename}` не найден в корне репозитория'


def test_invalid_class_then_confirm(capsys):
    with patch('builtins.input', side_effect=['unknown', ' MAGE ', 'Y']):
        character = choice_char_class('Тест')
    assert isinstance(character, Mage)
    assert 'Неизвестный класс' in capsys.readouterr().out


def test_training_handles_unknown_command(capsys):
    with patch('builtins.input', side_effect=['???', ' SPECIAL ', 'skip']):
        result = start_training(Mage('Тест'))
    output = capsys.readouterr().out
    assert 'Неизвестная команда' in output
    assert 'специальное умение' in output
    assert result == 'Тренировка окончена.'

