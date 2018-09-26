import unittest
from tournament import Player


class TestPlayerClassMethods(unittest.TestCase):
    def test_player_creation(self):
        player = Player(1, "Arvid", 99, True, 3, 3)
        self.assertEqual(player.__repr__(), "(1, 'Arvid', 99, True, 3, 3)")

    def test_player_update(self):
        player = Player(1, "Arvid", 1, True, 3, 3)
        player.update_player(1)
        self.assertEqual(player.points, 4)

    def test_player_set_item(self):
        player = Player(2, "Victor", 0, False, 0, 0)
        player.__setitem__(2, 3)
        self.assertEqual(player.__getitem__(2), 3)


if __name__ == '__main__':
    unittest.main()