__author__ = 'rika'

import numpy as np
import operator

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # for dataSet = np.array([[1., 1.1], [1., 1.], [0, 0], [0, .1]]), dataSet.shape is (4, 2)
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    # tile result:
    # array([[ 1.5,  0.5],
    #   [ 1.5,  0.5],
    #   [ 1.5,  0.5],
    #   [ 1.5,  0.5]])
    sqDiffMat = diffMat ** 2 # element wise power
    #array([[ 0.25,  0.36],
    #   [ 0.25,  0.25],
    #   [ 2.25,  0.25],
    #   [ 2.25,  0.16]])
    sqDistance = sqDiffMat.sum(axis = 1)
    # axis = 1 results in array([ 0.61,  0.5 ,  2.5 ,  2.41])
    # axis = 0 results in array([ 5.  ,  1.02])
    distance = sqDistance ** .5
    sortedDistance = distance.argsort()
    # argsort(a, axis=-1, kind='quicksort', order=None)
    # kind : {'quicksort', 'mergesort', 'heapsort'}, optional Sorting algorithm.
    # returns an array of indices of the same shape as `a` that index data along the given axis in sorted order.
    classCount = {}
    for i in range(k):
        label = labels[sortedDistance[i]]
        classCount[label] = classCount.get(label, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]




if __name__ == "__main__":
    dataSet = np.array([[1., 1.1], [1., 1.], [0, 0], [0, .1]])
    labels = ['a', 'a', 'b', 'b']
    inX = [1.5, 0.5]
    for k in range(1, 4):
        print classify(inX, dataSet, labels, k)
