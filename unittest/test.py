import unittest

class TestLogin(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        pass

    def test_valid_login(self):
          # Expect user preferences and display home page
          pass
    
    def test_valid_user_with_null_password(self):
        # Expect error message
        pass

    def test_valid_pass_with_null_username(self):
        # Expect error message
        pass

    def test_invalid_login(self):
        # Expect error message
        pass


if __name__ == '__main__':
    unittest.main()