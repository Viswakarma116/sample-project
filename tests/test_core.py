import unittest

from sample_project import greet


class GreetTests(unittest.TestCase):
    def test_greets_named_person(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_defaults_for_missing_name(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_defaults_for_blank_name(self):
        self.assertEqual(greet("   "), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
