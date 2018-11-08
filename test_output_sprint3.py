import main
import userStory01
import userStory02
import userStory03
import userStory04
import userStory05
import userStory06

import userStory09
import userStory10
import userStory11
import userStory12
import userStory13
import userStory14

import userStory17
import userStory18
import userStory19
import userStory20
import userStory21
import userStory22

import userStory25
import userStory26
import userStory27
import userStory28
import userStory29
import userStory30

(listOfPeople,listOfFamilies)= main.gedComParse('correct2.ged')
(listOfPeople2,listOfFamilies2)= main.gedComParse('correct2.ged')
(listOfPeople3,listOfFamilies3)= main.gedComParse('error3.ged')

userStory27.us_27(listOfPeople3)
main.present(listOfPeople3,listOfFamilies3)


userStory01.userStory01(listOfPeople, listOfFamilies)
userStory02.userStory02(listOfPeople, listOfFamilies)
userStory09.us_09(listOfFamilies, listOfPeople)
userStory10.us_10(listOfFamilies, listOfPeople)
userStory17.US_17(listOfPeople,listOfFamilies)
userStory18.US_18(listOfPeople)
userStory25.userStory25(listOfPeople,listOfFamilies)
userStory26.us_26(listOfFamilies,listOfPeople)



userStory03.userStory03(listOfPeople2)
userStory04.userStory04(listOfFamilies2)
userStory11.us_11(listOfFamilies2)
userStory12.us_12(listOfFamilies2, listOfPeople2)
userStory19.us_19(listOfPeople2, listOfFamilies2)
userStory20.us_20(listOfPeople2, listOfFamilies2)
#userStory28.us_28(listOfPeople2, listOfFamilies2)


userStory05.userStory05(listOfPeople3, listOfFamilies3)
userStory06.userStory06(listOfPeople3, listOfFamilies3)
userStory13.us_13(listOfFamilies3, listOfPeople3)
userStory14.us_14(listOfFamilies3, listOfPeople3)
userStory21.us_21(listOfPeople3, listOfFamilies3)
userStory22.us_22(listOfPeople3, listOfFamilies3)
userStory29.us_29(listOfPeople3)
userStory30.us_30(listOfPeople3)

