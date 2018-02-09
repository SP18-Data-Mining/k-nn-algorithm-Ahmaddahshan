import csv 
import math
import sys

dataObjectCount = 0
testData = []
trainingData = []
with open('fruit_data_with_colors.txt','r') as tsv:

	for line in tsv : 
		if dataObjectCount % 5 == 0 :
	
			if dataObjectCount != 0 :
				testData.append(line.strip().split('\t'))
		else :
			trainingData.append(line.strip().split('\t'))
		dataObjectCount = dataObjectCount + 1

# Print fruit_data_with_colors.txt file
print("Test Data" + str(testData))
print('\n\n\n\n\n\n\n')
print("Training data" + str(trainingData))

for i, y in enumerate(testData):
    minDistance = 1000
    testDatax = float(testData[i][4])
    testDatay = float(testData[i][5])
    
    for j, testdataItem in enumerate(trainingData):
        traningDatax = float(trainingData[j][4])
        traningDatay = float(trainingData[j][5])
        tmpDistance = math.sqrt(((testDatax - traningDatax)**2) + ((testDatay - traningDatay)**2))
        
        tmpDistance = testdataItem
        if (tmpDistance >= minDistance):
            minDistance = tmpDistance
            nearestTraningData = j

print "\n"
print "Nearest traning data: ", nearestTraningData
print "Predicited label of test data: ", testdataItem[1]