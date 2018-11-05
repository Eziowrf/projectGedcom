import unittest
import main
import userStory05
import userStory06
import userStory13
import userStory14
#import userStory21
#import userStory22

class TestMethods(unittest.TestCase):
    def test_us05(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error3.ged')
        condition1 = userStory05.userStory05(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct3.ged')
        condition2 = userStory05.userStory05(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us06(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error3.ged')
        condition1 = userStory06.userStory06(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct3.ged')
        condition2 = userStory06.userStory06(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)
        
    def test_us13(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error3.ged')
        condition1 = userStory13.us_13(listOfFamilies, listOfPeople)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct3.ged')
        condition2 = userStory13.us_13(listOfFamilies2, listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us14(self):
        (listOfPeople,listOfFamilies)= main.gedComParse('error3.ged')
        condition1 = userStory14.us_14(listOfFamilies,listOfPeople)
        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct3.ged')
        condition2 = userStory14.us_14(listOfFamilies2,listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

##    def test_us21(self):
##        (listOfPeople,listOfFamilies)= main.gedComParse('error3.ged')
##        condition1 = userStory21.us_21(listOfPeople,listOfFamilies)
##        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct3.ged')
##        condition2 = userStory21.us_21(listOfPeople2,listOfFamilies2)
##        self.assertEqual(condition1, False)
##        self.assertEqual(condition2, True)
##        
##    def test_us22(self):
##        (listOfPeople,listOfFamilies)= main.gedComParse('error3.ged')
##        condition1 = userStory22.us_22(listOfPeople,listOfFamilies)
##        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct3.ged')
##        condition2 = userStory22.us_22(listOfPeople2,listOfFamilies2)
##        self.assertEqual(condition1, False)
##        self.assertEqual(condition2, True)


if __name__ == "__main__":
    unittest.main()
