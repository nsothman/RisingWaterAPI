import numpy as np
import os
import os.path
import math
matrixFile = np.loadtxt('C:\\Python Projects\\LearningFlask\\output_srtm.asc', skiprows = 6)
outFile = open('C:\\Python Projects\\LearningFlask\\output_srtmOUT.asc', 'w')

def latCalc(i):
    return (math.sqrt(0.0008333333333333333333333333) * i + 40.688749999997)
def longCalc(j):
    return (math.sqrt(0.0008333333333333333333333333) * j + 28.082361111139)

outFile.write('[\n')
for i in range(0, 3141, 3):
    outFile.write('[')
    for j in range(0, 6939, 3):
        if matrixFile[i][j] != 0:
            outFile.write('{\"alt\":' + str(matrixFile[i][j]) + ',\"lat\":' + str(latCalc(i)) + ',\"long\":' + str(longCalc(j)) + ',\"flooded\": false}, ')
        else:
            outFile.write('{\"alt\":' + str(matrixFile[i][j]) + ',\"lat\":' + str(latCalc(i)) + ',\"long\":' + str(longCalc(j)) + ',\"flooded\": true}, ')
    outFile.write('{\"alt\":' + str(matrixFile[i][6939]) + ',\"lat\":' + str(latCalc(i)) + ',\"long\":' + str(longCalc(6939)) + ',\"flooded\": true}')
    outFile.write('], ')
    outFile.write('\n')
if matrixFile[3141][6939] != 0:
    outFile.write('{\"alt\":' + str(matrixFile[3141][6939]) + ',\"lat\":' + str(latCalc(3141)) + ',\"long\":' + str(longCalc(6939)) + ',\"flooded\": false}]\n')
else:
    outFile.write('{\"alt\":' + str(matrixFile[3141][6939]) + ',\"lat\":' + str(latCalc(3141)) + ',\"long\":' + str(longCalc(6939)) + ',\"flooded\": true}]\n')
outFile.write(']')
