from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid

        assert grid is not None, "Grid should not be None"
        assert len(grid) == 9, "Grid should have 9 letters"
        assert all(letter.isalpha() and letter.isupper() for letter in grid)
        assert isinstance(grid, list), "Grid should be a list"

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid('') is False

    def test_is_invalid(self):
        new_game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "EUREKA"
        new_game.grid = list(test_grid)
        assert new_game.is_valid(test_word) is True
        assert new_game.is_valid(test_word) is False

    def test_is_invalid(self):
        new_game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "SANDWICH"
        assert new_game.is_valid(test_word) is False
        assert new_game.grid == list(test_grid)
    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
