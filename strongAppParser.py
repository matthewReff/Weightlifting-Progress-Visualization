## Date;Workout Name;Exercise Name;Set Order;Weight;Weight Unit;Reps;RPE;Distance;Distance Unit;Seconds;Notes;Workout Notes;Workout Duration
import csv 

def loadStrongData():
  with open('strong-data.csv') as data:
    csvReader = csv.reader(data, delimiter=';')
    (
      DATE_COLUMN,
      WORKOUT_NAME_COLUMN,
      EXERCISE_NAME_COLUMN,
      SET_ORDER_COLUMN,
      WEIGHT_COLUMN,
      WEIGHT_UNIT_COLUMN,
      REPS_COLUMN,
      RPE_COLUMN,
      DISTANCE_COLUMN,
      DISTANCE_UNIT_COLUMN,
      SECONDS_COLUMN,
      NOTES_COLUMN,
      WORKOUT_NOTES_COLUMN,
      WORKOUT_DURATION_COLUMN
    ) = next(csvReader)

    strongDataRows = []
    for row in csvReader:
      (date, _, exerciseName, _, weight, _, reps, *rest) = row
      strongDataRows.append((date, exerciseName, weight, reps))

    return strongDataRows

def saveStrongDataToCsv(strongAppData):
  with open('strong-data-parsed.csv', 'w') as data:
    csvWriter = csv.writer(data, delimiter=',')

    csvWriter.writerow(["date", "bodyWeight", "exerciseName", "repetitions", "liftedWeight"])
    for spreadsheetRow in strongAppData:
      (rawDate, rawExerciseName, weight, reps) = spreadsheetRow

      (datePart, timePart) = rawDate.split()
      (fullYear, month, day) = datePart.split("-")
      date = "/".join((month, day, fullYear[:2]))

      if rawExerciseName in exerciseAliases:
        exerciseName = exerciseAliases[rawExerciseName]
      else:
        exerciseName = rawExerciseName

      # TODO load bodyweight
      bodyWeight = 1
      csvWriter.writerow([date, bodyWeight, exerciseName, reps, weight])


exerciseAliases = {
  "farmer carry": "Farmer Carry",
  "Deadlift (Barbell)": "Deadlift",
  "Squat (Barbell)": "Squat",
  "Bench Press (Barbell)": "Bench"
}