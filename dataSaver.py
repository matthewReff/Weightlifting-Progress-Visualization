import csv
import re
import json


def saveDataToCsv(liftData):
    with open('spreadsheetData.csv', 'w') as data:
        csvWriter = csv.writer(data, delimiter=',')

        csvWriter.writerow(["date", "bodyWeight", "exerciseName", "repetitions", "liftedWeight"])
        for liftingEntry in liftData:
            lifts = liftingEntry["lifts"]
            for liftDetail in lifts:
                date = liftingEntry["date"]
                bodyWeight = liftingEntry["weight"]
                exerciseName = liftDetail["exerciseName"]
                sets = liftDetail["sets"]
                for setDetail in sets:
                    reps = setDetail["reps"]
                    weight = setDetail["weight"]
                    csvWriter.writerow([date, bodyWeight, exerciseName, reps, weight])