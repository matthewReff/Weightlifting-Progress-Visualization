from dataLoader import extractDataIntoJSON
from dataSaver import saveDataToCsv
from strongAppParser import loadStrongData, saveStrongDataToCsv

def main():
    a = loadStrongData()
    saveStrongDataToCsv(a)
    #liftingData = extractDataIntoJSON()
    #saveDataToCsv(liftingData)

if __name__ == "__main__":
    main()