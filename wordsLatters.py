#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:05:59 2018

@author: Kyle_hall
"""

from basicgraph import *
from bfs import *

# return True if there should be an edge between nodes for word1 and word2
# in the word graph. Return False otherwise
#
def shouldHaveEdge(word1, word2):
    numDifferentLetters = 0
    for x in range(len(word1)):
        if(word1[x] != word2[x]):
            numDifferentLetters = numDifferentLetters + 1
    if(numDifferentLetters == 1):
        return True
    return False

# Give a file of words, return a graph with
# - one node for each word
# - an edge for every pair of words, w1 and w2,
#      where shouldHaveEdge(w1, w2) is True.
#


def buildWordGraph(wordsFile = "words5.text"):
    numEdges = 0
    numNodes =0
    node1 = None
    node2 = None
    d = {}
    wordGraph = Graph()

    inFile = open(wordsFile, encoding = "utf-8")
    for line in inFile:
        singleLine = line.split()
        newNode = Node(str(singleLine))
        wordGraph.addNode(newNode)
        numNodes = numNodes + 1
       
    #I got this from online documentation given in class
    inFile = open(wordsFile, encoding = "utf-8")
    for line in inFile:
        word2 = line[:]
        #The below line is messing it up
        word = line[:-1]
        #sprint(word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
                
    for i in range(len(word2)):
        bucket = word2[:i] + '_' + word2[i+1:]
        if bucket in d:
            d[bucket].append(word2)
        else:
            d[bucket] = [word2]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if(word1 != word2):
                    for node in wordGraph.nodes:
                        if(node.getName() == "['"+ word1+"']"):
                            node1 = wordGraph.getNode("['"+ word1+ "']")
                        if(node.getName() == "['"+ word2+ "']"):                                                   
                            node2 = wordGraph.getNode("['"+ word2+ "']")
                    
                    if(node1 != None and node2 != None):                       
                        if(node2 not in wordGraph.adjacencyLists[node1]):
                            wordGraph.addEdge(node1,node2)
                            numEdges = numEdges + 1
    #print(d)
    #print(wordGraph)
                           
    return wordGraph, numNodes,numEdges

# Assumption: (modified) breadth first search has already been executed.
#
# Thus, parent values have been set in all nodes reached by bfs.
# Now, work backwards from endNode (end word) to build a list of words
# representing a ladder between the start word and end word.
#
# For example, if the start word was "cat" and the end word was "dog", after bfs
# we might find that "dog"'s parent was "dot" and then that "dot"'s parent was
# "cot" and finally that "cot"'s parent was "cat" (which has no parent).  Thus,
# a ladder from "cat" to "dog" is ["cat", "cot", "dot", "dog"]
#
# Return [] if the endNode has no parent.  If the end node has no parent, the
# the breadth first search could not reach it from the start node. Thus, there
# is no word ladder between the start and end words.
#
def extractWordLadder(endNode):
    distance = 0
    currentNode = endNode
    ladder = []
    ladder.append(currentNode.getName())
    distance = distance + 1
    while(currentNode.getParent() != None):
        ladder.append(currentNode.getParent())
        currentNode = currentNode.getParent()
        distance = distance + 1
 
    flipLadder = []
    x = len(ladder) -1
    while(x>=0):
        flipLadder.append(ladder[x])
        x = x-1
    return flipLadder, distance

def wordLadders(wordsFile = "words5.text"):
    # 1. read the words file
    # 2. build a graph based on the words file
    # 3. user interaction loop:
    #    - request user to enter either two words (start and end word)
    #      or one word (start word) or 'q' (to quit)
    #    - check that the give word or words are in the dictionary
    #    - execute breadth first search from the start word's node
    #      (Note: you need to slightly modify the original bfs in bfs.py
    #      to set and update distance and parent properties of Nodes.  This also
    #      requires modification of the Node class in basicgraph.py to add
    #      those properties.)
    #    - if an end word was given, extract word ladder from
    #      start to that endword
    #    - if an end word was not given, find the node in the graph
    #      with the largest distance value and extract the ladder between
    #      the start node and that node.
    #    - print appropriate information - the extracted ladder and its length

    # code for 1. and 2. above goes here
    graph,nodes,edges = buildWordGraph(wordsFile)
    # code for 3. goes inside the while loop below
    print("Created word graph with "+str(nodes)+ " nodes and "+str(edges)+" edges")
    userInput = input("Enter start and end words OR start word OR 'q' to quit: ")
    words = userInput.split()
    
    while (words[0] != 'q'):
        wordsLen = len(words)
        counter = 0
        for x in words:
            for node in graph.nodes:
                if(node.getName() == "['"+ str(x)+"']"):
                    counter = counter + 1
                    
        if(wordsLen == counter):
            bfs(graph,graph.getNode("['"+ words[0]+"']"))
            if(wordsLen == 1):
                maximumNum = 0
                for node in graph.nodes:
                    if node.getDist() >= maximumNum:
                        maximumNode = node
                        maximumNum  = node.getDist()
                lad,dist = extractWordLadder(graph.getNode(maximumNode.getName()))
                print(maximumNode.getName()+" is maximally distant ("+str(dist)+" steps) from "+ words[0])
                print(lad)
            if(wordsLen == 2):
                lad,dist = extractWordLadder(graph.getNode("['"+ words[1]+"']"))
                print("Shortest ladder from "+words[0]+" to "+ words[1] +" is length "+str(dist)+":")
                print(lad)
                
            
        else:
            print("Word/Words are not in dictionary")
            
        userInput = input("Enter start and end words OR start word OR 'q' to quit: ")
        words = userInput.split()
        
        

        
        


 
