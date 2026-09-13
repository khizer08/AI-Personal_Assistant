import unittest

import main


class AppTest(unittest.TestCase):
    def test_app_imports(self):
        self.assertIsNotNone(main.app)


if __name__ == "__main__":
    unittest.main()
