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

    @patch('TournamentManager.tournament.select_game_type', return_value='1')
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '1')

    @patch('TournamentManager.tournament.select_game_type', return_value='2')
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '2')

    @patch('TournamentManager.tournament.select_game_type', return_value='3')
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '3')

    @patch('TournamentManager.tournament.select_game_type', return_value='4')
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '4')

    @patch('TournamentManager.tournament.select_game_type', return_value='5')
    def test_game_type(self, input):
        self.assertEqual(tt.select_game_type(), '5')

    @patch('TournamentManager.tournament.input_players', return_value='3')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '3')

    @patch('TournamentManager.tournament.input_players', return_value='3')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '4')

    @patch('TournamentManager.tournament.input_players', return_value='5')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '5')

    @patch('TournamentManager.tournament.input_players', return_value='6')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '6')

    @patch('TournamentManager.tournament.input_players', return_value='7')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '7')

    @patch('TournamentManager.tournament.input_players', return_value='8')
    def test_input_players(self, input):
        self.assertEqual(tt.input_players(), '8')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='1')
    def test_select_cpu_level(self, input):
        self.assertEqual(tt.select_cpu_level(), '1')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='2')
    def test_select_cpu_level(self, input):
        self.assertEqual(tt.select_cpu_level(), '2')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='3')
    def test_select_cpu_level(self, input):
        self.assertEqual(tt.select_cpu_level(), '3')

    @patch('TournamentManager.tournament.select_cpu', return_value='True')
    def test_cpu_level(self, input):
        self.assertEqual(tt.select_cpu(), 'True')

    @patch('TournamentManager.tournament.select_cpu', return_value='False')
    def test_cpu_level(self, input):
        self.assertEqual(tt.select_cpu(), 'False')

if __name__ == '__main__':
    unittest.main()

