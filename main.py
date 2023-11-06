import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from datetime import datetime

from dataLoader import extractDataIntoJSON

def main():
    liftingData = extractDataIntoJSON()
    weightData = list(map(lambda x: x["weight"], liftingData))
    dateData = list(map(lambda x: convertDateStringToDate(x["date"]), liftingData))

    #print(weightData, dateData)
    #print(len(weightData), len(dateData))

    plt.title("Weight Over Time")
    plt.rcParams["figure.figsize"] = (20,20)
    plt.plot(dateData, weightData, color='blue')

plt.show()

def convertDateStringToDate(dateString):
    print(dateString)
    return datetime.strptime(dateString, "%m/%d/%y")

if __name__ == "__main__":
    main()