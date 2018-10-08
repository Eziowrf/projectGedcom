import project3
import userStory01
import userStory02
import userStory17
import userStory18

(listOfPeople,listOfFamilies)= project3.gedComParse('US_01_02_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory01.userStory01(listOfPeople, listOfFamilies)

(listOfPeople,listOfFamilies)= project3.gedComParse('US_01_02_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory02.userStory02(listOfPeople, listOfFamilies)

(listOfPeople,listOfFamilies)= project3.gedComParse('US_17_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory17.US_17(listOfPeople)

(listOfPeople,listOfFamilies)= project3.gedComParse('US_18_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory18.US_18(listOfPeople)
