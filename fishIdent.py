import trees
myDat,labels=trees.createDataSet()
#myShannonEnt=trees.calcShannonEnt(myDat)
#print(myDat)
#print(myShannonEnt)
print(trees.chooseBestFeatureToSplit(myDat))



