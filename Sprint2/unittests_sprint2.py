import unittest
import project3
import userStory01
import userStory02
import userStory03
import userStory04
import userStory09
import userStory10
import userStory17
import userStory18
import userStory25
import userStory26
class TestMethods(unittest.TestCase):
    def test_us01(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory01.userStory01(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory01.userStory01(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

    def test_us02(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory02.userStory02(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory02.userStory02(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

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

    def test_us09(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_09_test.ged')
        condition1 = userStory09.us_09(listOfFamilies, listOfPeople)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory09.us_09(listOfFamilies2, listOfPeople2)
        self.assertTrue(condition1)
        self.assertTrue(condition2)

    def test_us10(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_10_test.ged')
        condition1 = userStory10.us_10(listOfFamilies, listOfPeople)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('correct.ged')
        condition2 = userStory10.us_10(listOfFamilies2, listOfPeople2)
        self.assertTrue(condition1)
        self.assertTrue(condition2)

    def test_us17(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_17_test.ged')
        condition1 = userStory17.US_17(listOfPeople,listOfFamilies)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('correct.ged')
        condition2 = userStory17.US_17(listOfPeople2,listOfFamilies2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

    def test_us18(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_18_test.ged')
        condition1 = userStory18.US_18(listOfPeople)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('correct.ged')
        condition2 = userStory18.US_18(listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us25(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_25_test.ged')
        condition1 = userStory25.userStory25(listOfPeople,listOfFamilies)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('correct.ged')
        condition2 = userStory25.userStory25(listOfPeople2,listOfFamilies2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

    def test_us26(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_26_test.ged')
        condition1 = userStory26.us_26(listOfFamilies,listOfPeople)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('correct.ged')
        condition2 = userStory26.us_26(listOfFamilies2,listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)



if __name__ == "__main__":
    unittest.main()
