from numpy import *
import bayes
listOPosts,listClasses=bayes.loadDataSet()
myVocalList=bayes.createVocabList(listOPosts)
trainMat=[]
for postinDoc in listOPosts:
	trainMat.append(bayes.setOfWords2Vec(myVocalList,postinDoc))
print(trainMat)
p0v,p1v,pab=bayes.trainNB0(trainMat,listClasses)
print(p0v)
print(p1v)
print(pab)