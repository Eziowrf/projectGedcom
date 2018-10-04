from compareAge import compareAge
from subtractAge import subtractAge
def checkDeathvsBirth(listOfFamilies, listOfPeople):
    children_birthdays = []
    father_deathday = []
    mother_deathday = []
    for family in listOfFamilies:
        #check for children
        if family.Children != "NA":
            children = family.Children.split(',')
            for child in children:
                child = child.replace('@','')
                for people in listOfPeople:
                    if child == people.ID:
                        children_birthdays.append(people.Birthday)
        #print(children_birthdays)
        #check for parent deaths
        for people in listOfPeople:
            if family.WifeID == people.ID:
                if people.Death != "NA":
                    mother_deathday = people.Death
            if family.HusbandID == people.ID:
                if people.Death != "NA":
                    father_deathday = people.Death
        #compare deaths to birthdays
        if children_birthdays != []:
            for child in children_birthdays:
                if mother_deathday != []:
                    if compareAge(child, mother_deathday):
                        print("ERROR: INDIVIDUAL: US09: "+family.WifeID+": Mother dies on "+mother_deathday+" before child birthday "+child)
                if father_deathday != []:
                    father = subtractAge(father_deathday, "0-9-0")
                    #print(father)
                    if compareAge(child, father):
                        print("ERROR: INDIVIDUAL: US09: "+family.HusbandID+": Father dies on "+father_deathday+" less than 9 months before child birthday "+child)

        father_deathday = []
        mother_deathday = []
        children_birthdays = []
        
