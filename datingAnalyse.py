import matplotlib
import matplotlib.pyplot as plt
import kNN
from numpy import array
datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
'''
print(datingDataMat)
print(datingLabels[0:20])

fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()

normMat,ranges,minVals=kNN.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)
kNN.datingClassTest()
'''
kNN.classifyPerson()