import userStory03
import userStory04

(listOfPeople,listOfFamilies)= project3.gedComParse('error.ged')
project3.present(listOfPeople,listOfFamilies)
# (listOfPeople1,listOfFamilies1)= project3.gedComParse('correct.ged')
# project3.present(listOfPeople1,listOfFamilies1)

userStory03.userStory03(listOfPeople)
userStory04.userStory04(listOfFamilies)
