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


def addToWorkoutFiles(athleteName: str):
    workouts = shared.getWorkouts()

    path = PATH + '/' + shared.getCompetitionName() + '/'

    for name in workouts:
        with open(path + name + '.csv', 'a+', encoding='UTF8', newline='') as f:
            f.write("\n" + "_," + athleteName + ",")


def addToFiles(athleteName: str, category: int):
    # addToTeamsFile(athleteName, category)
    addToWorkoutFiles(athleteName)


def addUser() -> None:
    isTeamCompetition = shared.isTeamCompetition()
    if isTeamCompetition == False:
        athleteName = input("Name of the athlete: ")
        category = chooseCategory()
        addToFiles(athleteName, category)
    else:
        print("addUser not implemented for team competition")


def removeUser():
    print("Remove user")
