from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("levski")

    def test_init(self):
        self.assertEqual("levski", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_team_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "levski1"
        expected = "Team Name can contain only letters!"
        self.assertEqual(expected, str(ve.exception))

    # add_member
    def test_add_member__correctly_added_return(self):
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        result = self.team.add_member(**name_age)
        expected = "Successfully added: Mario, Luigi, Kiro"
        self.assertEqual(expected, result)

    def test_add_member__members_update(self):
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age)
        self.assertEqual({"Mario": 30, "Luigi": 25, "Kiro": 50}, self.team.members)

    def test_add_member__member_already_added(self):
        name_age2 = {"Mario": 30, "Pippo": 25, "Kiro": 50}
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age)
        self.team.add_member(**name_age2)
        expected = {"Mario": 30, "Luigi": 25, "Kiro": 50, "Pippo": 25}
        self.assertEqual(expected, self.team.members)

    # remove_member
    def test_remove_member__correct_return(self):
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age)
        result = self.team.remove_member("Luigi")
        expected = "Member Luigi removed"
        self.assertEqual(expected, result)

    def test_remove_member__removed_from_dict(self):
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age)
        self.team.remove_member("Luigi")
        self.assertEqual({"Mario": 30, "Kiro": 50}, self.team.members)

    def test_remove_member__does_not_exist(self):
        name_age = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age)
        result = self.team.remove_member("Peter")
        expected = "Member with name Peter does not exist"
        self.assertEqual(expected, result)

    # __gt__
    def test_gt_true(self):
        team2 = Team("cska")
        name_age = {"slabak1": 18, "slabak2": 55}
        name_age1 = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age1)
        team2.add_member(**name_age)
        self.assertEqual(True, self.team.__gt__(team2))

    def test_gt_false(self):
        team2 = Team("cska")
        name_age = {"slabak1": 18, "slabak2": 55}
        name_age1 = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age1)
        team2.add_member(**name_age)
        self.assertEqual(False, team2.__gt__(self.team))
        self.assertFalse(team2.__gt__(self.team))

    def test_gt_equals(self):
        team2 = Team("cska")
        name_age = {"slabak1": 18, "slabak2": 55}
        name_age1 = {"Mario": 30, "Luigi": 25}
        self.team.add_member(**name_age1)
        team2.add_member(**name_age)
        self.assertEqual(False, team2 > self.team)

    # __len__
    def test_len_return(self):
        self.assertEqual(0, self.team.__len__())
        name_age1 = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age1)
        self.assertEqual(3, len(self.team))

    # __add__
    def test_add_return_type_Team(self):
        name_age1 = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age1)
        team2 = Team("super")
        name_age = {"Lillo": 40, "Franco": 30, "Ciccio": 60}
        team2.add_member(**name_age)
        self.team.__add__(team2)
        new_team = self.team + team2
        self.assertEqual("levskisuper", new_team.name)

    def test_add_new_members(self):
        name_age1 = {"Mario": 30, "Luigi": 25, "Kiro": 50}
        self.team.add_member(**name_age1)
        team2 = Team("super")
        name_age = {"Lillo": 40, "Franco": 30, "Ciccio": 60}
        team2.add_member(**name_age)
        self.team.__add__(team2)
        expected = {"Mario": 30, "Luigi": 25, "Kiro": 50, "Lillo": 40, "Franco": 30, "Ciccio": 60}
        new_team = self.team.__add__(team2)
        self.assertEqual(expected, new_team.members)

    # __str__
    def test_str_return(self):
        name_age1 = {"A": 30, "C": 25, "B": 50, "K": 30}
        team = Team("Levski")
        team.add_member(**name_age1)
        result = team.__str__()
        expected = f"Team name: Levski\n" \
                   f"Member: B - 50-years old\n" \
                   f"Member: A - 30-years old\n" \
                   f"Member: K - 30-years old\n" \
                   f"Member: C - 25-years old"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
