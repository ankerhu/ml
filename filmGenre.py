import kNN
group,labels=kNN.createDataSet()
predictResult=kNN.classify0([0,0],group,labels,3)
print(predictResult)