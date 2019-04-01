import unittest
from word_counter import WordCounter


class CheckCounterClass(unittest.TestCase):
    """
    Tester class for WordCounter
    """
    def testGetTopOccurences(self):
        """
        Function that tests the getTopOccurrences method
        from WordCounter class. Takes a test .txt file and
        checks it against pre-checked dict

        """
        object = WordCounter("tests/testFile.txt")
        trueValue = {
            "quick": 7,
            "jumps": 7,
            "brown": 5,
            "zebra": 3,
            "table": 3,
            "over": 4,
            "dog": 4,
            "layer": 5,
            "crazy": 3,
            "productive": 4
        }
        self.assertDictEqual(object.getTopOccurrences(), trueValue)


    def testCountWords(self):
        """
        Function that tests the countWords function within the
        Word Counter class.
        """
        # Number of words in text4.txt
        num = 200
        tester = WordCounter("tests/text4.txt")
        self.assertEqual(tester.countWords(), num)


if __name__ == '__main__':
    unittest.main()
