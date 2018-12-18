# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 04:28:07 2018

@author: nyzc
"""
#function to sort the class order refer to the frequence
#return the class label 
#classifier 
def classify(genTree, featlabels, testVec):
    firstr = list(genTree.keys())[0]
    secondDict = genTree[firstr]
    featIndex = featlabels.index(firstr)#for the first feature in the tree, the index of it in featurelabel
    for key in secondDict.keys():
        if key == testVec[featIndex]:
            if type(secondDict[key]) == dict:
                classLabel = classify(secondDict[key], featlabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
    
#fnd the label which has the lagest amount
import operator
def Majority(classList):
    classCount  = {}
    for class_ in classList:
        if class_ not in classCount.keys(): 
            classCount[class_] = 0
        classCount[class_]  += 1
    sortClass = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortClass[0][0]
    
#function that create a dataset
def creatDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 0, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

#function that calculate Shannon Entropy
#return entropy
from math import log
def calcShannonEnt(dataset):
    numEntry = len(dataset)
    labelCounts = {}
    for feat in dataset:
        label = feat[-1]
        if label not in labelCounts.keys():
            labelCounts[label] = 0
        labelCounts[label] += 1
    shannonEnt = 0.0
    for key in labelCounts.keys():
        prob = float(labelCounts[key]/numEntry)
        shannonEnt += -prob*log(prob, 2)
    return shannonEnt

#function that partition a dataset
#return partitioned dataset
def splitDataSet(dataset, axis, value):
    redataset = []
    for feat in dataset:
        if feat[axis] == value:
            redufeat = feat[:axis]
            redufeat.extend(feat[axis+1:])
            redataset.append(redufeat)
    return redataset

#choose the best feature to split the dataset
#return bestfeature
def chooseBestFeatureToSplit(dataSet):
    num_feat = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    baseinfoGain = 0.0
    baseFeature = -1
    for i in range(num_feat):
        featList = [example[i] for example in dataSet]
        uniquevalue = set(featList)
        newEntropy = 0.0
        for value in uniquevalue:
            subdataSet = splitDataSet(dataSet, i, value)
            prob = len(subdataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subdataSet)
        inforGain = baseEntropy - newEntropy 
        if(inforGain > baseinfoGain):
            baseinfoGain = inforGain
            baseFeature = i
    return baseFeature

#create decision tree
def createTree(dataSet, labels):
    labels_copy = labels[:]
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return Majority(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestLabel = labels_copy[bestFeat]
    featvalue = [example[bestFeat] for example in dataSet]
    uniquevalue = set(featvalue)
    genTree = {bestLabel : {}}
    del labels_copy[bestFeat]
    for value in uniquevalue:
        subLabels = labels_copy[:]
        genTree[bestLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return genTree
