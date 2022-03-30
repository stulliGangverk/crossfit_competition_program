import python_files.shared as shared
import python_files.setup_workouts as setup_workouts
import os

SETUP_WORKOUTS_PATH = setup_workouts.PATH

def sanitizeResults():
    competitionName = shared.getCompetitionName()

    workoutList = shared.getAllWorkouts()
    for workout in workoutList:
        sanitizeWorkout(workout, competitionName)

def sanitizeSpecificWorkout():
    competitionName = shared.getCompetitionName()

    workoutList = shared.getAllWorkouts()
    print("Choose workout to sanitize")
    for x in range(0, len(workoutList)):
        print(str(1 + x) + ": " + workoutList[x])

    val = int(input("Choose the workout to sanitize: "))
    if val > 0 and val < len(workoutList) + 1:
        sanitizeWorkout(workoutList[val - 1], competitionName)
    else:
        print("Please choose a number from the list to sanitize a workout")

def sanitizeWorkout(workout: dict, competitionName: str) -> None:
    csvPath = workout + '.csv'
    # Does the workout file exist
    if not os.path.exists(SETUP_WORKOUTS_PATH + '/' + competitionName + '/' + csvPath):
        print("The workout file for " + workout + " has not been setup")
        quit()

    # Check if some score has not been filled out
    sanitized = True
    workoutData = shared.getDataFromFile(csvPath)
    for data in workoutData:
        if data['Skor'] == '' or data['Skor'] == None:
            print("Error found in " + workout)
            print("Skor has not been added for " +
                    data[shared.getWorkoutFieldToIndexFor()])
            sanitized = False

    if sanitized == True:
        print(workout + " is sanitized")
    else:
        print()
        print(workout + " is not sanitized, please fix")
