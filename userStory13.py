from subtractAge import subtractAge
from change import changeDateToNum
def us_13(listOfFamilies, listOfPeople):
    flag = True
    for family in listOfFamilies:
        children_birthdays = []
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
                        if not (changeDateToNum(difference) < 2 or changeDateToNum(difference) > 800):
                            print("ERROR: FAMILY: US13: "+family.ID+": Siblings of Birthdays " + child_birthday + " and " +child2_birthday + " are born between 2 days and 8 months apart")
                            flag = False
    return flag
