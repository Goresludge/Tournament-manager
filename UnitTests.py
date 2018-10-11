import unittest
from unittest.mock import patch
from TournamentManager.tournament import Player
import TournamentManager.tournament as tt


class TestMethods(unittest.TestCase):
    def test_player_creation(self):
        player = Player(1, "Arvid", 99, True, 3, 3)
        self.assertEqual(player.__repr__(), "(1, 'Arvid', 99, True, 3, 3)")

    def test_player_set_item(self):
        player = Player(2, "Victor", 0, False, 0, 0)
        player.__setitem__(2, 3)
        self.assertEqual(player.__getitem__(2), 3)

    def test_update_score(self):
        player = Player(2, "Victor", 0, False, 0, 0)
        i = 0
        while(i < 10):
            i += 2
            player.update_score(1)
        self.assertEqual(player.points, 5)

    @patch('TournamentManager.tournament.select_game_type', return_value='3')
    # @patch('tt.select_game_type)
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '3')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='2')
    def test_select_cpu_level(self, input):
        self.assertEqual(tt.select_cpu_level(), '2')

    @patch('TournamentManager.tournament.select_cpu', return_value='True')
    def test_cpu_level(self, input):
        self.assertEqual(tt.select_cpu(), 'True')


if __name__ == '__main__':
    unittest.main()

