import main
import userStory03
import userStory04
import userStory11
import userStory12
import userStory19
import userStory20

(listOfPeople,listOfFamilies)= main.gedComParse('error.ged')
main.present(listOfPeople,listOfFamilies)
# (listOfPeople1,listOfFamilies1)= project3.gedComParse('correct.ged')
# project3.present(listOfPeople1,listOfFamilies1)


userStory03.userStory03(listOfPeople)
userStory04.userStory04(listOfFamilies)
userStory11.us_11(listOfFamilies)
userStory12.us_12(listOfFamilies, listOfPeople)
userStory19.us_19(listOfPeople, listOfFamilies)
userStory20.us_20(listOfPeople, listOfFamilies)
