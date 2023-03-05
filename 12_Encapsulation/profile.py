import unittest


class Profile:
    def __init__(self, user: str, password: str):
        self.username = user
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:

            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):

        if len(value) < 8 or \
                not any(char.isdigit() for char in value) or \
                not any(char.isupper() for char in value):

            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):

        pas_print = '*' * len(self.password)
        return f"You have a profile with username: \"{self.username}\" and password: {pas_print}"


class Tests(unittest.TestCase):
    def test_invalid_password(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('My_username', 'My-password')
            #print(Profile('My_username', 'My-password'))
        self.assertEqual(str(ve.exception), "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def test_invalid_username(self):
        with self.assertRaises(ValueError) as ve:
            self.profile = Profile('Too_long_username', 'Any')
        self.assertEqual(str(ve.exception), "The username must be between 5 and 15 characters.")

    def test_correct_profile(self):
        self.profile = Profile("Username", "Passw0rd")
        self.assertEqual(str(self.profile), 'You have a profile with username: "Username" and password: ********')

if __name__ == "__main__":
    unittest.main()


#profile_with_invalid_password = Profile('My_username', 'My-password')
#profile_with_invalid_username = Profile('Too_long_username', 'Any')
#correct_profile = Profile("Username", "Passw0rd")
#print(correct_profile)
