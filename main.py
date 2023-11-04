import csv
import re

def extractDataIntoJSON():
    with open('weightliftingData.csv') as data:
        csvReader = csv.reader(data, delimiter=',')
        (DATE_COLUMN, WEIGHT_COLUMN, LIFT_1_COLUMN, LIFT_2_COLUMN, LIFT_3_COLUMN, LIFT_4_COLUMN) = next(csvReader)

        dataList = []
        for row in csvReader:
            (DATE, WEIGHT, *LIFT) = row
            rowEntry = dict()
            rowEntry["date"] = DATE
            rowEntry["weight"] = WEIGHT
            rowEntry["lifts"] = list(map(extractLiftInfo, LIFT))
            dataList.append(rowEntry)
        print(dataList)

def extractLiftInfo(rawString):
    liftVsWeightPattern = r"^(\D*)\W(.*)$"
    weightPattern = r"((\d+x\d+\W?){1,}-?\d+)\W?"
    regexMatch = re.search(liftVsWeightPattern, rawString)
    exerciseName = regexMatch.group(1)
    weights = regexMatch.group(2)

    splitWeights = re.findall(weightPattern, weights)
    weightSets = list(map(lambda weightEntry: weightEntry[0], splitWeights))
    return { "exerciseName": exerciseName, "weights": weightSets}

def extract(a):
    return a[0]

def main():
    extractDataIntoJSON()

if __name__ == "__main__":
    main()