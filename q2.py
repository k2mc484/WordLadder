#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
I think the mathematical relationship between the length of the longest heads 
for a given number of coins follows a log. I think it follows this because the plot 
of Average Longest Streak vs. Number of Flips shows a straight line on a semi-log
graph. The standard deviation graph also shows a curve that appears to be a log, but
 I am unsure of this corrolation.

"""
import random
import math

def stdDev(values):
    mean = float(sum(values))/len(values)
    diffsum = 0.0
    for item in values:
        diff = item - mean
        diffsum = diffsum + diff*diff
    return math.sqrt(diffsum/len(values))

# simulate flipping a coin numFlips times.
# return tuple (number of heads, number of tails)
#
def doNCoinFlips(numFlips):
    currentStreak = 0
    longestStreak = 0
    flipNum = 0
    while flipNum < numFlips:
        value = random.randint(1,2)
        if value == 1:
            currentStreak = currentStreak + 1
        else:
            if(currentStreak > longestStreak):
                longestStreak = currentStreak
            currentStreak = 0
        flipNum = flipNum + 1
    
    if(currentStreak > longestStreak):
        longestStreak = currentStreak

    return (longestStreak)

# Do numTrials coin flip simulations with numCoins each time.
# For each trial compute ratio of number of heads to number of trials.
# Compute average and standard deviation of the ratios over all trials.
# Print summary and
# return tuple (average heads/tails ratio, standard devation of ratio)
# 
def doCoinFlipTrials(numTrials, numCoins):
    longestStreaks = []
    for trial in range(numTrials):
        nlongestStreak = doNCoinFlips(numCoins)
        #print("Trial #{}: numHeads = {}, numTails = {}".format(trial, nHeads, nTails))
        # NOTE: This code *can* crash - it's unlikely but nTails can, of course, be 0 
        longestStreaks.append(nlongestStreak)
        
    avg = sum(longestStreaks)/len(longestStreaks)
    standDev = stdDev(longestStreaks)
    
    print("# of flips = {}: avg longest run: {} (SD: {})".format(numCoins, avg, standDev))
    return (numCoins, avg, standDev)

    
#
#
# Create figure with two subplots, one showing avg. head/tail ratios for different numbers of
# coin flips, the other showing standard deviation of head/tail ratios.
#
def plotResults(results):
    numFlips, ratios, ratioSDs = tuple(zip(*results))

    pylab.figure(1)
    pylab.clf()
    pylab.subplot(121)
    pylab.title("Longest Streak")
    pylab.xlabel("Number of flips")
    pylab.ylabel("Average Longest Streak")
    pylab.semilogx()
    pylab.plot(numFlips, ratios, 'ro-') 
    
    pylab.subplot(122)
    pylab.title("Std dev. of Longest Streak")
    pylab.xlabel("Number of flips")
    pylab.ylabel("Standard deviation")
    pylab.semilogx()
    pylab.plot(numFlips, ratioSDs, 'ro-')
  
# Execute doCoinFlipTrials for different numbers of coins (and given number of trials),
# starting with minCoins and increasing by factor until number exceeds maxCoins.
# Return list of results returned by the calls to doCoinFlipTrials.
# Thus, results will be of form [(minCoins, ..ratio.., ...std...), (factor*minCoins, ..ratio.., ...std..), ...]
#
    
def doCoinFlipExperiment(minCoins, maxCoins, factor, numTrials=20):
    numCoins = minCoins
    results = []
    while numCoins <= maxCoins:
        results.append(doCoinFlipTrials(numTrials, numCoins ))
        numCoins = numCoins * factor
    return results

import pylab

results = doCoinFlipExperiment(16, 2**12, 2,1000)
plotResults(results)
pylab.show()

