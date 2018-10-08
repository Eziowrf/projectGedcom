import project3
import userStory17
import userStory18


(listOfPeople,listOfFamilies)= project3.gedComParse('US_17_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory17.US_17(listOfPeople)


(listOfPeople,listOfFamilies)= project3.gedComParse('US_18_test.ged')
project3.present(listOfPeople,listOfFamilies)
userStory18.US_18(listOfPeople)