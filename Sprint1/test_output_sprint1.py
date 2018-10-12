import userStory01 
import userStory02 
import userStory09 
import userStory10 
import userStory17 
import userStory18 
import userStory22
import userStory25
import userStory26
import project3

(listOfPeople,listOfFamilies)= project3.gedComParse('error.ged')
project3.present(listOfPeople,listOfFamilies)
(listOfPeople1,listOfFamilies1)= project3.gedComParse('correct.ged')
project3.present(listOfPeople1,listOfFamilies1)

userStory01.userStory01(listOfPeople, listOfFamilies)
userStory02.userStory02(listOfPeople, listOfFamilies)
userStory09.us_09(listOfFamilies, listOfPeople)
userStory10.us_10(listOfFamilies, listOfPeople)
userStory17.US_17(listOfPeople,listOfFamilies)
userStory18.US_18(listOfPeople)
userStory25.userStory25(listOfPeople,listOfFamilies)
userStory26.us_26(listOfFamilies,listOfPeople)

userStory01.userStory01(listOfPeople1, listOfFamilies1)
userStory02.userStory02(listOfPeople1, listOfFamilies1)
userStory09.us_09(listOfFamilies1, listOfPeople1)
userStory10.us_10(listOfFamilies1, listOfPeople1)
userStory17.US_17(listOfPeople1,listOfFamilies1)
userStory18.US_18(listOfPeople1)
userStory25.userStory25(listOfPeople1,listOfFamilies1)
userStory26.us_26(listOfFamilies1,listOfPeople1)
