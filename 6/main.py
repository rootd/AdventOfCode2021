#!/usr/bin/env python

import copy

def nextOceanDay(ocean):
	newOcean = [0] * 9
	for fishCounter in range(len(ocean) - 1):
		newOcean[fishCounter] = ocean[fishCounter + 1]
	newOcean[6] += ocean[0]
	newOcean[8] = ocean[0]

	return newOcean

def partOne(ocean, days):
	for day in range(0,days):
		ocean = nextOceanDay(ocean)

	print("There are " + str(sum(ocean)) + " lanternfishes in the ocean.")

def partTwo(ocean, days):
	for day in range(0,days):
		ocean = nextOceanDay(ocean)

	print("There are " + str(sum(ocean)) + " lanternfishes in the ocean.")

if __name__ == "__main__":
	print("AdventOfCode - Day 6")
	print("********************")
	
	with open("input.txt") as f:
		lanternFishes = map(int, f.read().split(","))
		ocean = [0] * 9
		for lanternFish in lanternFishes:
			ocean[lanternFish] += 1

	print("\nPart one")
	print("========")
	partOne(copy.deepcopy(ocean), 80)
	
	print("\nPart two")
	print("========")
	partTwo(copy.deepcopy(ocean), 256)