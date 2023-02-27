MAX_AVERAGES = 8
averages = []
total = 0

for x in range(MAX_AVERAGES):
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    averages.append(battingAverage)
    total = total + battingAverage

averages.sort()
minAverage = averages[0]
maxAverage = averages[-1]
average = sum(averages) / len(averages)

print("Minimum batting average is " + str(minAverage))
print("Maximum batting average is " + str(maxAverage))
print("Average batting average is " + str(average))