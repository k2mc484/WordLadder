#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:07:41 2018

@author: Kyle_hall
"""

from queue1210 import *
from basicgraph import *

#####
#
# classic Breadth First Search
#
# See, e.g., http://en.wikipedia.org/wiki/Breadth-first_search
#

def bfs(graph, startNode):
    for n in graph.nodes:
        n.setStatus('unseen')
        n.setDist(0)
        n.setParent(None)
    startNode.setStatus('seen')
    #print("Initializing queue with: ", startNode.name)
    queue = Queue()
    queue.enqueue(startNode)
    while queue.size() != 0:
        #print(queue)
        currentNode = queue.dequeue()
       # print("removed {} from queue. Processing neighbors".format(currentNode.name))
        for node in graph.neighborsOf(currentNode):
            if node.getStatus() == 'unseen':
                node.setStatus('seen')
                node.setParent(currentNode)
                node.setDist(currentNode.getDist() + 1)
                queue.enqueue(node)
        currentNode.setStatus('processed')
        
