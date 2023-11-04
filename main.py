import csv

def extractDataIntoJSON():
    with open('weightliftingData.csv') as data:
        csvReader = csv.reader(data, delimiter=',')
        (DATE_COLUMN, WEIGHT_COLUMN, LIFT_1_COLUMN, LIFT_2_COLUMN, LIFT_3_COLUMN, LIFT_4_COLUMN) = next(csvReader)

        dataList = []
        for (DATE, WEIGHT, LIFT_1, LIFT_2, LIFT_3, LIFT_4) in csvReader:
            rowEntry = dict()
            rowEntry["date"] = DATE
            rowEntry["weight"] = WEIGHT
            rowEntry["lifts"] = list(map(extractLiftInfo, [LIFT_1, LIFT_2, LIFT_3, LIFT_4]))
            dataList.append(rowEntry)
        print(dataList)

def extractLiftInfo(rawString):
    return rawString

def main():
    extractDataIntoJSON()

if __name__ == "__main__":
    main()