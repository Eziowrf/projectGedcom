from subtractAge import subtractAge
from change import changeDateToNum
def us_14(listOfFamilies, listOfPeople):
    flag = True
    for family in listOfFamilies:
        children_birthdays = []
        count = 0
        if family.Children != "NA":
            children = family.Children.split(',')
            for child in children:
                for people in listOfPeople:
                    if child == people.ID:
                        children_birthdays.append(people.Birthday)

            for child_birthday in children_birthdays:
                for child2_birthday in children_birthdays:
                    difference = subtractAge(child_birthday, child2_birthday)
                    if not difference[0] == "-":
                        if changeDateToNum(difference) < 2:
                            count = count + 1

            count = count - len(children_birthdays)
            if count > 5:
                print("ERROR: FAMILY: US14: "+family.ID+": Family has more than 5 Children born within 2 days of each other")
                flag = False
    return flag
