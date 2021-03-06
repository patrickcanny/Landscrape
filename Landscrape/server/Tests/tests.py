from Scraper import scrape
import unittest

class TestScraper(unittest.TestCase):

    #This Tests that a dictionary is returned when the "get_results" fucntion is called on a single search term
    def test_Get_Output_Given_Input_Single(self):
        # Single Term Test, Checking if a single input produces something.
        testInput_SingleTerm= 'Coffee'
        TestScraper = Scraper(testInput_SingleTerm)
        self.assertEqual(TestScraper.get_results(), not None)

    #This Tests that a dictionary is returned when the function "get_results" is called with multiple terms
    def test_Get_Output_Given_Input_Multi(self):
        # Multi-Term Test, Checking that something is returned.
        testInput_MultiTerm = 'Coffee, Bars, Tacos'
        TestScraper = Scraper(testInput_MultiTerm)
        self.assertEqual(TestScraper.get_results(), not None)
        self.assertFalse(TestScraper.get_results(), None)

    # This Tests that the length of the output Dictionary is the same as the number of inputs
    def test_Get_Output_Given_Input_SameNumberOfDictEntriesAsInputs(self):
        testInput_MultiTerm = 'Coffee, Bars, Tacos'
        TestScraper = Scraper(testInput_MultiTerm)
        self.assertEqual(len(TestScraper.get_results()), 3)

    #I think this is all the tests we need? Please review

if __name__ == '__main__':
    unittest.main()
