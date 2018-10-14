import unittest
import project3
import userStory03
import userStory04

class TestMethods(unittest.TestCase):
    def test_us03(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory03.userStory03(listOfPeople)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory03.userStory03(listOfPeople2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

    def test_us04(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory04.userStory04(listOfFamilies)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory04.userStory04(listOfFamilies2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

if __name__ == "__main__":
    unittest.main()
