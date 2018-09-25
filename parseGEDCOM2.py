from prettytable import PrettyTable

#opening file
ged_file = open('C:\\Users\Erik\Google Drive\SSW-555\My-Family-11-Sep-2018-855.ged', 'r')

class Person:
    ID = "NA"
    Name = ""
    Gender = ""
    Birthday = ""
    Age = ""
    Alive = True
    Death = "NA"
    Child = "NA"
    Spouse = "NA"

    def __init__(self, ID):
        self.ID = ID

class Families:
    ID = "NA"
    Married = "NA"
    Divorced = "NA"
    HusbandID = "NA"
    HusbandName = "NA"
    WifeID = "NA"
    WifeName = "NA"
    
    def __init__(self, ID):
        self.ID = ID
        self.Children = []

birth = False
death = False
divorce = False
married = False
listOfPeople = []
listOfFamilies = []
current_family = []
current_person = []
count = 0
    
for line in ged_file:
    # split the line into words
    line_words = line.split()
    # get the second element since that is the tag of line
    line_tag = line_words[1].strip()
    # get the first element to indicate the level
    line_level = line_words[0].strip()

    # get the third element in case of INDI or FAM tags
    if len(line_words)> 2:
        special_tag = line_words[2].strip()
    else:
        special_tag = "FALSE"
        

    arguments = []
    for x in range(2, len(line_words)):
        arguments.append(line_words[x].strip())

    argument = " ".join(arguments)

    # check for new people or family information
    if line_level == '0':
        if special_tag == 'INDI':
            current_person = Person(line_tag)
            listOfPeople.append(current_person)
        elif special_tag == 'FAM':
            current_family = Families(line_tag)
            listOfFamilies.append(current_family)

    elif line_level == '1':
        if line_tag == 'NAME':
            current_person.Name = argument
        elif line_tag == 'SEX':
            current_person.Gender = argument
        elif line_tag == 'BIRT':
            birth = True
        elif line_tag == 'DEAT':
            death = True
        elif line_tag == 'FAMS':
            current_person.Spouse = argument
        elif line_tag == 'FAMC':
            current_person.Child = argument
        elif line_tag == 'HUSB':
            current_family.HusbandID = argument
            for person in listOfPeople:
                if person.ID == argument:
                    current_family.HusbandName = person.Name
        elif line_tag == 'WIFE':
            current_family.WifeID = argument
            for person in listOfPeople:
                if person.ID == argument:
                    current_family.WifeName = person.Name
        elif line_tag == 'MARR':
            married = True
        elif line_tag == 'DIV':
            divorce = True
        elif line_tag == 'CHIL':
            current_family.Children.append(argument)

    elif line_level == '2':
        if line_tag == 'DATE':
            if birth:
                current_person.Birthday = argument
                birth = False
            elif death:
                current_person.Death = argument
                current_person.Alive = False
                death = False
            elif married:
                current_family.Married = argument
                married = False
            elif divorce:
                current_family.Divorced = argument
                divorce = False

individuals = PrettyTable()
individuals.field_names = ["ID","Name","Gender","Birthday","Age","Alive","Death","Child","Spouse"]
for people in listOfPeople:
    individuals.add_row([people.ID, people.Name, people.Gender, people.Birthday, people.Age, people.Alive, people.Death, people.Child, people.Spouse])

print(individuals)

families = PrettyTable()
families.field_names = ["ID","Married","Divorced","Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
for family in listOfFamilies:
    families.add_row([family.ID, family.Married, family.Divorced, family.HusbandID, family.HusbandName, family.WifeID, family.WifeName, family.Children])


print(families)
