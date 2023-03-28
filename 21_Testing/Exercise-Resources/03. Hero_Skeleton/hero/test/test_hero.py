from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("user1", 2, 100, 50)
        self.enemy = Hero("enemy", 1, 100, 20)

    def test_init(self):
        self.assertEqual(self.hero.username, "user1")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_battle_exception_cannot_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_hero_health_lower_equal_zero(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_health_lower_equal_zero(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "You cannot fight enemy. He needs to rest")

    def test_battle_win__enemy_health(self):
        self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.health, 0)

    def test_battle_win_return(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "You win")

    def test_battle_win_new_values(self):
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 85)
        self.assertEqual(self.hero.damage, 55)

    def test_battle_draw_return(self):
        self.hero2 = Hero("user1", 5, 100, 50)
        self.enemy2 = Hero("enemy", 5, 100, 20)
        result = self.hero2.battle(self.enemy2)
        self.assertEqual(result, "Draw")

    def test_battle_loose_return(self):
        self.hero2 = Hero("user1", 1, 100, 50)
        self.enemy2 = Hero("enemy", 5, 100, 20)
        result = self.hero2.battle(self.enemy2)
        self.assertEqual(result, "You lose")

    def test_battle_enemy_new_values_updated(self):
        self.hero2 = Hero("user1", 1, 100, 50)
        self.enemy2 = Hero("enemy", 5, 100, 20)
        self.hero2.battle(self.enemy2)
        self.assertEqual(self.enemy2.level, 6)
        self.assertEqual(self.enemy2.health, 55)
        self.assertEqual(self.enemy2.damage, 25)

    def test_str_method(self):
        self.assertEqual(self.hero.__str__(), f"Hero user1: 2 lvl\n"
                                              f"Health: 100\n"
                                              f"Damage: 50\n")


if __name__ == "__main__":
    main()
