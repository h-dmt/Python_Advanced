from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Mario", 27, 0)

    def test_init_values(self):
        self.assertEqual("Mario", self.player.name)
        self.assertEqual(27, self.player.age)
        self.assertEqual(0, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_property_set(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("aa", 27, 0)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_property_set(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Maria", 17, 0)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    # add_new_win method
    def test_add_new_win__already_added(self):
        self.player.wins.append("Tournament1")
        result = self.player.add_new_win("Tournament1")
        self.assertEqual("Tournament1 has been already added to the list of wins!", result)

    def test_add_new_win__correctly_added(self):
        result = self.player.add_new_win("Tournament1")
        self.assertEqual(None, result)
        self.assertEqual("Tournament1", self.player.wins[0])

    # __lt__ method
    def test_lt__top_speed_player(self):
        self.player.points = 21
        player2 = TennisPlayer("Maria", 19, 51)
        result = self.player < player2
        expected = 'Maria is a top seeded player and he/she is better than Mario'
        self.assertEqual(expected, result)

    def test_lt__better_player(self):
        self.player.points = 21
        player2 = TennisPlayer("Maria", 19, 51)
        result = player2 < self.player
        expected = 'Maria is a better player than Mario'
        self.assertEqual(expected, result)

    def test_str_output(self):
        self.player.points = 97.55
        self.player.add_new_win("Tournament_2020")
        self.player.add_new_win("Tournament_2023")
        expected = f"Tennis Player: Mario\n" \
                   f"Age: 27\n" \
                   f"Points: 97.5\n" \
                   f"Tournaments won: Tournament_2020, Tournament_2023"

        result = str(self.player)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
