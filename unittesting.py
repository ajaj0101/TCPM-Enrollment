import unittest
from Identity import Person

class TestPerson(unittest.TestCase):
    def test_init(self):
        obj = Person("Andrew Chiang")
        self.assertEqual(obj.name, "Andrew Chiang")