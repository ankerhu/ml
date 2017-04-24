import bayes
listOPostes,listClasses=bayes.loadDataSet()
myVocabList=bayes.createVocabList(listOPostes)
print(myVocabList)
result1=bayes.setOfWords2Vec(myVocabList,listOPostes[0])
result2=bayes.setOfWords2Vec(myVocabList,listOPostes[3])
print(result1)
print(result2)