# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 03:29:53 2018

@author: nyzc
"""
#plot node
import matplotlib.pyplot as plt

decision_node = dict(boxstyle="square", fc="w")
leaf_node = dict(boxstyle="circle", fc="w")

def plotNode(nodeText, centreNode, ParentNode, nodeType):
    createPlot.ax1.annotate(nodeText, xy = ParentNode, xycoords = 'axes fraction', \
                            xytext = centreNode, textcoords = 'axes fraction',\
                            va = 'center', ha = 'center', bbox = nodeType,\
                            arrowprops = dict(arrowstyle = '<-')) #here is tricky: xytext is the place where we put text, we want ->XXX not XXX->

def getNumleaf(genTree):
    numLeaf = 0
    if type(genTree) == dict:
        for key in genTree.keys():
            subTree = genTree[key]
            numLeaf += getNumleaf(subTree)
        return numLeaf
    else: 
        return 1

def getTreeDepth(genTree):
    maxDepth = 0
    Depth = 0
    for key in genTree.keys():
        if (type(genTree[key]) == dict) :
            if len(genTree) == 1:
                Depth = 1 + getTreeDepth(genTree[key])
            else:
                Depth = 0 + getTreeDepth(genTree[key])
        if maxDepth < Depth:
            maxDepth = Depth
    return maxDepth
    
def textNode(ParentNode, centreNode, branchValue):
    x = (centreNode[0] + ParentNode[0])/2.0
    y = (centreNode[1] + ParentNode[1])/2.0
    createPlot.ax1.text(x, y, branchValue)

def TreePlotter(genTree, ParentNode, branchValue):
    numLeaf = getNumleaf(genTree)
    depth = getTreeDepth(genTree)
    firststr = list(genTree.keys())[0]
    secondDict = genTree[firststr]
    centreNode = (TreePlotter.xOff + (1 + numLeaf)/2/TreePlotter.Wd,\
             TreePlotter.yOff)
    textNode(centreNode, ParentNode, branchValue)
    plotNode(firststr, centreNode, ParentNode, decision_node)
    TreePlotter.yOff = TreePlotter.yOff - 1/TreePlotter.Ht
    for key in secondDict.keys():
        if type(secondDict[key]) == dict:
            TreePlotter(secondDict[key], centreNode, str(key))
        else:
            TreePlotter.xOff = TreePlotter.xOff + 1/TreePlotter.Wd
            plotNode(secondDict[key], (TreePlotter.xOff, TreePlotter.yOff), centreNode, leaf_node)
            textNode((TreePlotter.xOff, TreePlotter.yOff), centreNode, str(key))
            
    TreePlotter.yOff = TreePlotter.yOff + 1/TreePlotter.Ht
    
def createPlot(genTree):
    fig = plt.figure()
    createPlot.ax1 = fig.add_subplot(111, frameon = False)
    TreePlotter.Wd = float(getNumleaf(genTree))
    TreePlotter.Ht = float(getTreeDepth(genTree))
    TreePlotter.xOff = -0.5/TreePlotter.Wd
    TreePlotter.yOff = 1.0
    TreePlotter(genTree, (0.5, 1.0), '')
    plt.show()
    
       
    

    
