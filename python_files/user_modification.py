from setuptools import setup
import python_files.setup_workouts as setup_workouts
import python_files.shared as shared

PATH = setup_workouts.PATH


def chooseCategory() -> int:
    categories = shared.getCategories()

    print("Choose the category the user is competing in")
    for x in range(0, len(categories)):
        print(str(x + 1) + ": " + categories[x])

    print()
    category = input("Category number: ")

    try:
        if (int(category) > 0 and int(category) < len(categories) + 1):
            return int(category)
        print("Number chosen is not among the categories available")
    except:
        print("Please choose a valid number")


def addToTeamsFile(athleteName: str, category: int) -> None:
    competitionName = shared.getCompetitionName()
    nrOfCategories = len(shared.getCategories())

    commaString = ""
    for x in range(0, nrOfCategories):
        if category - 1 == x:
            commaString = commaString + ",x"
        else:
            commaString = commaString + ","

    addText = "_," + athleteName + commaString

    path = PATH + '/' + competitionName + '/lidin.csv'
    with open(path, 'a+', encoding='UTF8', newline='') as f:
        f.write("\n" + addText)


def addToWorkoutFiles(athleteName: str) -> None:
    workouts = shared.getWorkouts()

    path = PATH + '/' + shared.getCompetitionName() + '/'

    for name in workouts:
        with open(path + name + '.csv', 'a+', encoding='UTF8', newline='') as f:
            f.write("_," + athleteName + ",\n")


def addToFiles(athleteName: str, category: int) -> None:
    addToTeamsFile(athleteName, category)
    addToWorkoutFiles(athleteName)


def addUser() -> None:
    isTeamCompetition = shared.isTeamCompetition()
    if isTeamCompetition == False:
        athleteName = input("Name of the athlete: ")
        category = chooseCategory()
        addToFiles(athleteName, category)
    else:
        print("addUser not implemented for team competition yet")


def removeUserFromTeamsFile(athleteName: str):
    fileLines = shared.readFile(
        'lidin.csv', fileFolder='competitions/' + shared.getCompetitionName())

    newList = []
    for line in fileLines:
        if athleteName not in line:
            newList.append(line)

    competitionName = shared.getCompetitionName()
    path = PATH + '/' + competitionName + '/lidin.csv'
    with open(path, 'w', encoding='UTF8', newline='') as f:
        for line in newList:
            f.write(line)


def removeUserFromWorkouts(athleteName: str):
    workouts = shared.getWorkouts()

    for workout in workouts:
        fileLines = shared.readFile(
            workout + '.csv', fileFolder='competitions/' + shared.getCompetitionName())

        newList = []
        for line in fileLines:
            if athleteName not in line:
                newList.append(line)

        competitionName = shared.getCompetitionName()
        path = PATH + '/' + competitionName + '/' + workout + '.csv'


def removeUserHelper(athleteData: list) -> None:
    athleteName = input("Search for the athlete you wish to remove: ")

    nameList = []
    for dataPoint in athleteData:
        name = dataPoint[shared.getWorkoutFieldToIndexFor()]
        if athleteName.lower() in name.lower():
            nameList.append(name)

    print()
    if len(nameList) == 0:
        print("No athletes were found, please search again")
        print()
        removeUserHelper(athleteData)
    else:
        print(str(len(nameList)) + " athletes were found")
        for x in range(0, len(nameList)):
            print(str(x + 1) + ": " + nameList[x])

        print()
        chosenValue = input(
            "Choose user you wish to delete or choose 's' to search again: ")

        if chosenValue == 's':
            removeUserHelper(athleteData)
        else:
            if int(chosenValue) > 0 and int(chosenValue) < len(nameList) + 1:
                athleteName = nameList[int(chosenValue) - 1]

                print("Are you sure you wish to remove athlete " + athleteName)
                print()
                val = input("y for yes, n to quit, s to search again: ")
                if val == 's':
                    removeUserHelper(athleteData)
                if val == 'y':
                    # removeUserFromTeamsFile(athleteName)
                    removeUserFromWorkouts(athleteName)

                    print("Athlete '" + athleteName + "' has been removed")


def removeUser():
    isTeamCompetition = shared.isTeamCompetition()
    if isTeamCompetition == False:
        athleteData = shared.getDataFromFile('lidin.csv')
        removeUserHelper(athleteData)
    else:
        print("removeUser not implemented for team competition yet")
