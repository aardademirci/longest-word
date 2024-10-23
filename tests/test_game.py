from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        """Test that the game initializes with a valid grid."""
        new_game = Game()
        grid = new_game.grid

        # Verify that the grid is a list
        assert isinstance(grid, list), "Grid should be a list"

        # Verify that the grid has exactly 9 letters
        assert len(grid) == 9, "Grid should have 9 letters"

        # Verify that all letters in the grid are uppercase alphabets
        for letter in grid:
            assert letter in string.ascii_uppercase, f"Invalid letter in grid: {letter}"

    def test_space_in_word(self):
        """Test that a word with spaces is invalid."""
        new_game = Game()
        test_word = 'ERH YUE'
        assert new_game.is_valid(test_word) is False, "Word with spaces should be invalid"

    def test_not_contained_in_grid(self):
        """Test that a word not contained in the grid is invalid."""
        new_game = Game()
        new_game.grid = list('KWIENFUQW')  # Set a specific grid for testing
        test_word = 'VOIR'
        assert new_game.is_valid(test_word) is False, "Word not in grid should be invalid"

    def test_upper_case(self):
        """Test that a lowercase word is considered invalid."""
        new_game = Game()
        test_word = 'ertyh'
        assert new_game.is_valid(test_word) is False, "Lowercase word should be invalid"

    def test_unknown_word_is_invalid(self):
        """Test that a word not in the English dictionary is invalid."""
        new_game = Game()
        new_game.grid = list('KWIENFUQW')  # Force the grid to a test case
        assert new_game.is_valid('FEUN') is True, "Unknown word should be invalid"
