import unittest
import main
import userStory01
import userStory02
import userStory07
import userStory08
import userStory09
import userStory10
import userStory17
import userStory18
import userStory05
import userStory06
import userStory13
import userStory14
import userStory21
import userStory22
import userStory03
import userStory04
import userStory11
import userStory12
import userStory19
import userStory20
import userStory25
import userStory26
import userStory15
import userStory16
import userStory23
import userStory24
import userStory31
import userStory32
class TestMethods(unittest.TestCase):
    def test_us03(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error2.ged')
        condition1 = userStory03.userStory03(listOfPeople)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct2.ged')
        condition2 = userStory03.userStory03(listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us04(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error2.ged')
        condition1 = userStory04.userStory04(listOfFamilies)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct2.ged')
        condition2 = userStory04.userStory04(listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)
        
    def test_us11(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error2.ged')
        condition1 = userStory11.us_11(listOfFamilies)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct2.ged')
        condition2 = userStory11.us_11(listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us12(self):
        (listOfPeople,listOfFamilies)= main.gedComParse('error2.ged')
        condition1 = userStory12.us_12(listOfFamilies,listOfPeople)
        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct2.ged')
        condition2 = userStory12.us_12(listOfFamilies2,listOfPeople2)
        self.assertEqual(condition1, True)
        self.assertEqual(condition2, True)

    def test_us19(self):
        (listOfPeople,listOfFamilies)= main.gedComParse('error2.ged')
        condition1 = userStory19.us_19(listOfPeople,listOfFamilies)
        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct2.ged')
        condition2 = userStory19.us_19(listOfPeople2,listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)
        
    def test_us27(self):
        (listOfPeople,listOfFamilies)= main.gedComParse('error2.ged')
        condition1 = userStory20.us_20(listOfPeople,listOfFamilies)
        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct2.ged')
        condition2 = userStory20.us_20(listOfPeople2,listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us20(self):
        (listOfPeople,listOfFamilies)= main.gedComParse('error2.ged')
        condition1 = userStory20.us_20(listOfPeople,listOfFamilies)
        (listOfPeople2,listOfFamilies2)= main.gedComParse('correct2.ged')
        condition2 = userStory20.us_20(listOfPeople2,listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

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

    def test_us21(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error3.ged')
       condition1 = userStory21.us_21(listOfPeople,listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct3.ged')
       condition2 = userStory21.us_21(listOfPeople2,listOfFamilies2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)
       
    def test_us22(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error3.ged')
       condition1 = userStory22.us_22(listOfPeople,listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct3.ged')
       condition2 = userStory22.us_22(listOfPeople2,listOfFamilies2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)

    def test_us15(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory15.us_15(listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory15.us_15(listOfFamilies2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)
    
    def test_us16(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory16.us_16(listOfFamilies,listOfPeople)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory16.us_16(listOfFamilies2,listOfPeople2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)

    def test_us23(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory23.us_23(listOfPeople,listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory23.us_23(listOfPeople2,listOfFamilies2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)
    
    def test_us24(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory24.us_24(listOfPeople,listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory24.us_24(listOfPeople2,listOfFamilies2)
       self.assertEqual(condition1, False)
       self.assertEqual(condition2, True)

    def test_us07(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error4.ged')
        condition1 = userStory07.userStory07(listOfPeople)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct4.ged')
        condition2 = userStory07.userStory07(listOfPeople2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us08(self):
        (listOfPeople, listOfFamilies) = main.gedComParse('error4.ged')
        condition1 = userStory08.userStory08(listOfPeople, listOfFamilies)
        (listOfPeople2, listOfFamilies2) = main.gedComParse('correct4.ged')
        condition2 = userStory08.userStory08(listOfPeople2, listOfFamilies2)
        self.assertEqual(condition1, False)
        self.assertEqual(condition2, True)

    def test_us31(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory31.us_31(listOfPeople)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory31.us_31(listOfPeople2)
       self.assertEqual(condition1, True)
       self.assertEqual(condition2, True)
    
    def test_us32(self):
       (listOfPeople,listOfFamilies)= main.gedComParse('error4.ged')
       condition1 = userStory32.us_32(listOfPeople,listOfFamilies)
       (listOfPeople2,listOfFamilies2)= main.gedComParse('correct4.ged')
       condition2 = userStory32.us_32(listOfPeople2,listOfFamilies2)
       self.assertEqual(condition1, True)
       self.assertEqual(condition2, True)

if __name__ == "__main__":
    unittest.main()
