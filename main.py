from dataLoader import extractDataIntoJSON
from dataSaver import saveDataToCsv

def main():
    liftingData = extractDataIntoJSON()
    saveDataToCsv(liftingData)

if __name__ == "__main__":
    main()