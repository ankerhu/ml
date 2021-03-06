from numpy import *
#生成测试数据
def loadDataSet():
	postingList=[['my','dog','has','flea','problems','help','please'],
				['maybe','not','take','him','to','dog','park','stupid'],
				['my','dalmation','is','so','cute','I','love','him'],
				['stop','posting','stupid','worthless','garbage'],
				['mr','licks','ate','my','steak','how','to','stop','him'],
				['quit','buying','worthless','dog','food','stupid']]
	classVec=[0,1,0,1,0,1]
	return postingList,classVec

#格式化数据为列表
def createVocabList(dataSet):
	vacabSet=set([])
	for document in dataSet:
		vacabSet=vacabSet | set(document)
	return list(vacabSet)

#转换数据为向量，出现了就是1，没出现就是0
def setOfWords2Vec(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]=1
		else:
			print('the word:%s is not in my Vocabulary!'%word)
	return returnVec

#用已有数据训练，找到所有词的概率
def trainNB0(trainMatrix,trainCategory):
	numTrainDocs=len(trainMatrix)
	numWords=len(trainMatrix[0])
	print(numWords)
	pAbusive=sum(trainCategory)/float(numTrainDocs)
	p0Num=ones(numWords)
	p1Num=ones(numWords)
	p0Denom=2.0
	p1Denom=2.0
	for i in range(numTrainDocs):
		if trainCategory[i]==1:
			p1Num+=trainMatrix[i]
			p1Denom+=sum(trainMatrix[i])
		else:
			p0Num+=trainMatrix[i]
			p0Denom+=sum(trainMatrix[i])
	p1Vect=log(p1Num/p1Denom)
	p0Vect=log(p0Num/p0Denom)
	return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vect,p1Vect,pClass1):
	p1=sum(vec2Classify*p1Vect)+log(pClass1)
	p0=sum(vec2Classify*p0Vect)+log(1.0-pClass1)
	if p1>p0:
		return 1
	else:
		return 0
def testingNB():
	listOPosts,listClasses=loadDataSet()
	myVocabList=createVocabList(listOPosts)
	trainMat=[]
	for postinDoc in listOPosts:
		trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
	p0V,p1V,pAb=trainNB0(array(trainMat),array(listClasses))
	testEntry=['love','my','dalmation']
	thisDoc=array( (myVocabList,testEntry))
	print(testEntry,'classifyed as: ',classifyNB(thisDoc,p0V,p1V,pAb))
	testEntry=['stupid','garbage']
	thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
	print(testEntry,'classifyed as: ',classifyNB(thisDoc,p0V,p1V,pAb))
def bagOfWords2VecMN(vocabList,inputSet):
	returnVec=[0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)]+=1
	return returnVec