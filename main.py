import csv
import re

def extractDataIntoJSON():
    with open('weightliftingData.csv') as data:
        csvReader = csv.reader(data, delimiter=',')
        (DATE_COLUMN, WEIGHT_COLUMN, LIFT_1_COLUMN, LIFT_2_COLUMN, LIFT_3_COLUMN, LIFT_4_COLUMN, LIFT_5_COLUMN) = next(csvReader)

        dataList = []
        for row in csvReader:
            (DATE, WEIGHT, *LIFT) = row
            nonEmptyLifts = filter(lambda liftData: len(liftData) != 0, LIFT)
            rowEntry = dict()
            rowEntry["date"] = DATE
            rowEntry["weight"] = WEIGHT
            rowEntry["lifts"] = list(map(extractLiftInfo, nonEmptyLifts))
            dataList.append(rowEntry)
        #print(dataList)

def extractLiftInfo(rawString):
    nameVsSetPattern = r"^(\D*)\W(.*)$"
    nameVsSetMatch = re.search(nameVsSetPattern, rawString)
    exerciseName = nameVsSetMatch.group(1)
    setInfo = nameVsSetMatch.group(2)

    splitSetPattern = r"((\d+x\d+\W?){1,}-?\d+)\W?"
    splitSets = re.findall(splitSetPattern, setInfo)
    cleanSets = list(map(lambda set: set[0], splitSets))

    setVsWeightPattern = r"(.*)\W(\d+)$"
    for set in cleanSets:
        setWeightMatch = re.search(setVsWeightPattern, set)
        sets = setWeightMatch.group(1)
        weight = setWeightMatch.group(2)

        setPattern = r"(\d+)x(\d+)"
        setDataList = list(re.findall(setPattern, sets))
        for entry in setDataList:
            print(exerciseName, " ", entry[0], "x", entry[1], " @ ", weight, sep="")
        
    #weightSets = list(map(lambda weightEntry: weightEntry[0], splitSets))
    #return { "exerciseName": exerciseName, "weights": weightSets}
    return {}

def main():
    extractDataIntoJSON()

if __name__ == "__main__":
    main()