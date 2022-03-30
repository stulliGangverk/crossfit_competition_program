import python_files.setup_workouts as setup_workouts
import python_files.calculate_results as calculate_results
import python_files.consts as consts
import python_files.shared as shared
import python_files.change_team_category as change_team_category
import python_files.sanitize_teams as sanitize_teams
import python_files.sanitize_results as sanitize_results


def main():
    print("1: Setup workouts based on settings")
    print("2: Calculate workout results based on inputs")
    print("3: Calculate only up to certain workouts")
    print("4: Sanitize results")
    print("5: Sanitize specific workout")
    if shared.isTeamCompetition():
        print("6: Change team's category")
    if shared.isTeamCompetition():
        print("7: Sanitize team names")
    val = input("Choose what you wish to do: ")

    if val == '1':
        if consts.SETUPWORKOUTS == False:
            print("Setting up workouts is disabled in consts, change and run again")
        else:
            if consts.ADDRANDOMSCORES:
                print("Random scores will be added to the workouts")
            setup_workouts.setupWorkouts()

    if val == '2':
        calculate_results.calculateWorkouts()

    if val == '3':
        calculate_results.calculateCertainWorkouts()

    if val == '4':
        sanitize_results.sanitizeResults()

    if val == '5':
        sanitize_results.sanitizeSpecificWorkout()

    if val == '6':
        sanitize_results.sanitizeSpecificWorkout()

    if shared.isTeamCompetition() and val == '6':
        change_team_category.changeTeams()

    if shared.isTeamCompetition() and val == '7':
        sanitize_teams.sanitizeTeams()


main()

# setup_workouts.setupWorkouts()
# calculate_results.calculateWorkouts()
# sanitize_results.sanitizeSpecificWorkout()
# calculate_results.calculateCertainWorkouts()