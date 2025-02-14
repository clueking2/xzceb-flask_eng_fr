import unittest

from translator import english_to_french, french_to_english

class TestMyProject(unittest.TestCase):

    def test_english_to_french(self):

        self.assertNotEqual(english_to_french('None'),'')

        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):

        self.assertNotEqual(french_to_english('None'), '')

        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')