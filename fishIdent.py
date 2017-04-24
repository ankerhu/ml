import trees
import treePlotter

#myDat,labels=trees.createDataSet()
#myShannonEnt=trees.calcShannonEnt(myDat)
#print(myDat)
#print(myShannonEnt)
#print(trees.chooseBestFeatureToSplit(myDat))
#myTree=trees.createTree(myDat,labels)
#print(myTree)

#treePlotter.createPlot()
#myTree=treePlotter.retrieveTree(0)
#myTree['no surfacing'][3]='maybe'
#treePlotter.createPlot(myTree)
myDat,labels=trees.createDataSet()
myTree=treePlotter.retrieveTree(0)
result1=trees.classify(myTree,labels,[1,0])
result2=trees.classify(myTree,labels,[1,1])
trees.storeTree(myTree,'classifierStorage.txt')
stroedTree=trees.grabTree('classifierStorage.txt')
print(stroedTree)
print(myDat)
print(labels)
print(myTree)
print(result1)
print(result2)
