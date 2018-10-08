import unittest
import project3
import userStory01
import userStory02
import userStory17
import userStory18

class TestMethods(unittest.TestCase):
    def test_us01(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory01.userStory01(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('My-Family-9-Sep-2018-162.ged')
        condition2 = userStory01.userStory01(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us02(self):
        (listOfPeople, listOfFamilies) = project3.gedComParse('US_01_02_test.ged')
        condition1 = userStory02.userStory02(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = project3.gedComParse('My-Family-9-Sep-2018-162.ged')
        condition2 = userStory02.userStory02(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us17(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_17_test.ged')
        condition1 = userStory17.US_17(listOfPeople)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('My-Family-9-Sep-2018-162.ged')
        condition2 = userStory17.US_17(listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us18(self):
        (listOfPeople,listOfFamilies)= project3.gedComParse('US_18_test.ged')
        condition1 = userStory18.US_18(listOfPeople)
        (listOfPeople2,listOfFamilies2)= project3.gedComParse('My-Family-9-Sep-2018-162.ged')
        condition2 = userStory18.US_18(listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)



if __name__ == "__main__":
    unittest.main()
